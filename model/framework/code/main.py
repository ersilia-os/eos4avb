# imports
import csv
import os
import sys
import tempfile

import torch
import torchvision
from rdkit import Chem

from image_dataloader import ImageData, smiles_to_image

MODEL_CKPT = "ImageMol.pth.tar"
N_FEATURES = 512

# ImageMol stores the ResNet18 trunk as an nn.Sequential called embedding_layer;
# its positions map to these torchvision ResNet18 module names
EMBEDDING_LAYER_NAMES = {
    "0": "conv1",
    "1": "bn1",
    "4": "layer1",
    "5": "layer2",
    "6": "layer3",
    "7": "layer4",
}

# parse arguments
input_file = sys.argv[1]
output_file = sys.argv[2]

# current file directory
root = os.path.dirname(os.path.abspath(__file__))
checkpoints_dir = os.path.abspath(os.path.join(root, "..", "..", "checkpoints"))

# Load ImageMol _model


def load_model():

    _model = torchvision.models.resnet18(weights=None)
    _model.fc = torch.nn.Linear(_model.fc.in_features, 1)
    checkpoint = torch.load(
        os.path.join(checkpoints_dir, MODEL_CKPT), map_location=torch.device("cpu")
    )
    # Load the ResNet18 trunk by name; the pre-training heads (bn, jigsaw and
    # class classifiers) are not part of the embedding and are left out
    model_sd = _model.state_dict()
    loaded = set()
    for ckp_key, value in checkpoint["state_dict"].items():
        parts = ckp_key.split(".")
        if parts[0] != "embedding_layer":
            continue
        cur_key = ".".join([EMBEDDING_LAYER_NAMES[parts[1]]] + parts[2:])
        if model_sd[cur_key].shape != value.shape:
            raise ValueError(f"Shape mismatch for {ckp_key} -> {cur_key}")
        model_sd[cur_key] = value
        loaded.add(cur_key)
    missing = [k for k in model_sd if not k.startswith("fc.") and k not in loaded]
    if missing:
        raise ValueError(f"Checkpoint is missing ResNet18 weights: {missing}")
    _model.load_state_dict(model_sd)

    model_blocks = list(_model.children())
    model = torch.nn.Sequential(*model_blocks[:-1])  # Remove the final classifier head

    # Inference mode: BatchNorm must use the trained running statistics, as upstream
    # ImageMol does; torch.no_grad() alone does not switch this
    model.eval()

    return model


# Generate ImageMol embeddings
def generate_embeddings(smiles):
    model = load_model()

    embeddings = []
    img_processor = ImageData()
    tmp_dir = tempfile.mkdtemp()
    for idx, smi in enumerate(smiles):
        # An invalid SMILES would be drawn as a blank image; return an empty row instead
        if Chem.MolFromSmiles(smi) is None:
            embeddings.append([None] * N_FEATURES)
            continue
        path = f"{tmp_dir}/{idx}.png"
        try:
            smiles_to_image(smi, savePath=path)
            img_tensor = img_processor.get_image(path).to("cpu")
            with torch.no_grad():
                embeddings.append(model(img_tensor).reshape(N_FEATURES).tolist())
        except Exception as err:  # noqa: BLE001 - one bad molecule must not fail the batch
            print(f"Failed for {smi}: {err}", file=sys.stderr)
            embeddings.append([None] * N_FEATURES)
        if os.path.exists(path):
            os.remove(path)
    os.rmdir(tmp_dir)
    return embeddings


# read SMILES from .csv file, assuming one column with header
with open(input_file, "r") as f:
    reader = csv.reader(f)
    next(reader)  # skip header
    smiles_list = [r[0] for r in reader]

# run _model
outputs = generate_embeddings(smiles_list)

# write output in a .csv file
with open(output_file, "w") as f:
    writer = csv.writer(f)
    writer.writerow([f"feat_{i:03d}" for i in range(N_FEATURES)])
    for o in outputs:
        writer.writerow(o)
