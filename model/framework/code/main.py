# imports
import os
import csv
import sys

import torch
import torchvision

from image_dataloader import smiles_to_image, ImageData

MODEL_CKPT = "ImageMol.pth.tar"

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
    ckp_keys = list(checkpoint["state_dict"])
    cur_keys = list(_model.state_dict())
    model_sd = _model.state_dict()

    # Trim the keys because we are loading this into ResNet18
    ckp_keys = ckp_keys[:120]
    cur_keys = cur_keys[:120]

    for ckp_key, cur_key in zip(ckp_keys, cur_keys):
        model_sd[cur_key] = checkpoint["state_dict"][ckp_key]

    # Fully load the pre-trained model
    _model.load_state_dict(model_sd)

    model_blocks = list(_model.children())
    model = torch.nn.Sequential(*model_blocks[:-1])  # Remove the final classifier head

    return model


# Generate ImageMol embeddings
def generate_embeddings(smiles):
    model = load_model()

    embeddings = []
    img_processor = ImageData()
    for idx, smi in enumerate(smiles):
        path = f"{os.getcwd()}/{idx}.png"
        smiles_to_image(smi, savePath=path)
        img_tensor = img_processor.get_image(path).to("cpu")
        with torch.no_grad():
            embeddings.append(model(img_tensor).reshape(512).tolist())

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
    writer.writerow([f"feat_{i}" for i in range(1, 513)])
    for o in outputs:
        writer.writerow(o)
