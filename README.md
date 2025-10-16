# Molecular representation learning

Representation Learning Framework that utilizes molecule images for encoding molecular inputs as machine readable vectors for downstream tasks such as bio-activity prediction, drug metabolism analysis, or drug toxicity prediction. The approach utilizes transfer learning, that is, pre-training the model on massive unlabeled datasets to help it in generalizing feature extraction and then fine tuning on specific tasks.

This model was incorporated on 2023-01-25.


## Information
### Identifiers
- **Ersilia Identifier:** `eos4avb`
- **Slug:** `image-mol-embeddings`

### Domain
- **Task:** `Representation`
- **Subtask:** `Featurization`
- **Biomedical Area:** `Any`
- **Target Organism:** `Any`
- **Tags:** `Embedding`

### Input
- **Input:** `Compound`
- **Input Dimension:** `1`

### Output
- **Output Dimension:** `512`
- **Output Consistency:** `Fixed`
- **Interpretation:** ImageMol embeddings of shape [512] reshaped as a Numpy 1D array before serializing. These embeddings can be used as the input features of a fully connected classification or regression layer in a neural network.

Below are the **Output Columns** of the model:
| Name | Type | Direction | Description |
|------|------|-----------|-------------|
| feat_1 | float |  | feature 1 for ImageMol |
| feat_2 | float |  | feature 2 for ImageMol |
| feat_3 | float |  | feature 3 for ImageMol |
| feat_4 | float |  | feature 4 for ImageMol |
| feat_5 | float |  | feature 5 for ImageMol |
| feat_6 | float |  | feature 6 for ImageMol |
| feat_7 | float |  | feature 7 for ImageMol |
| feat_8 | float |  | feature 8 for ImageMol |
| feat_9 | float |  | feature 9 for ImageMol |
| feat_10 | float |  | feature 10 for ImageMol |

_10 of 512 columns are shown_
### Source and Deployment
- **Source:** `Local`
- **Source Type:** `External`
- **DockerHub**: [https://hub.docker.com/r/ersiliaos/eos4avb](https://hub.docker.com/r/ersiliaos/eos4avb)
- **Docker Architecture:** `AMD64`
- **S3 Storage**: [https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos4avb.zip](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos4avb.zip)

### Resource Consumption
- **Model Size (Mb):** `66`
- **Environment Size (Mb):** `1212`
- **Image Size (Mb):** `1332.92`

**Computational Performance (seconds):**
- 10 inputs: `33.18`
- 100 inputs: `34.56`
- 10000 inputs: `976.85`

### References
- **Source Code**: [https://github.com/HongxinXiang/ImageMol](https://github.com/HongxinXiang/ImageMol)
- **Publication**: [https://www.nature.com/articles/s42256-022-00557-6](https://www.nature.com/articles/s42256-022-00557-6)
- **Publication Type:** `Peer reviewed`
- **Publication Year:** `2022`
- **Ersilia Contributor:** [DhanshreeA](https://github.com/DhanshreeA)

### License
This package is licensed under a [GPL-3.0](https://github.com/ersilia-os/ersilia/blob/master/LICENSE) license. The model contained within this package is licensed under a [MIT](LICENSE) license.

**Notice**: Ersilia grants access to models _as is_, directly from the original authors, please refer to the original code repository and/or publication if you use the model in your research.


## Use
To use this model locally, you need to have the [Ersilia CLI](https://github.com/ersilia-os/ersilia) installed.
The model can be **fetched** using the following command:
```bash
# fetch model from the Ersilia Model Hub
ersilia fetch eos4avb
```
Then, you can **serve**, **run** and **close** the model as follows:
```bash
# serve the model
ersilia serve eos4avb
# generate an example file
ersilia example -n 3 -f my_input.csv
# run the model
ersilia run -i my_input.csv -o my_output.csv
# close the model
ersilia close
```

## About Ersilia
The [Ersilia Open Source Initiative](https://ersilia.io) is a tech non-profit organization fueling sustainable research in the Global South.
Please [cite](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff) the Ersilia Model Hub if you've found this model to be useful. Always [let us know](https://github.com/ersilia-os/ersilia/issues) if you experience any issues while trying to run it.
If you want to contribute to our mission, consider [donating](https://www.ersilia.io/donate) to Ersilia!
