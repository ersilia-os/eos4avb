# Molecular representation learning

ImageMol turns a rendered picture of a molecule into 512 features, learning from pixels rather than from a molecular graph. A ResNet18 encoder was pretrained by Zeng and colleagues on ten million unlabelled drug-like PubChem molecules through five self-supervised pretext tasks covering local substructures, global shape and image rationality, and the resulting representation transferred across 51 benchmark datasets spanning metabolism, brain penetration, toxicity and target binding. Individual dimensions are not chemically interpretable and are meant to feed downstream models.

This model was incorporated on 2023-01-25.Last packaged on 2026-08-31.

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
- **Interpretation:** 512 ImageMol features encoding molecular structure, suitable as input for downstream models.

Below are the **Output Columns** of the model:
| Name | Type | Direction | Description |
|------|------|-----------|-------------|
| feat_000 | float |  | feature 0 for ImageMol |
| feat_001 | float |  | feature 1 for ImageMol |
| feat_002 | float |  | feature 2 for ImageMol |
| feat_003 | float |  | feature 3 for ImageMol |
| feat_004 | float |  | feature 4 for ImageMol |
| feat_005 | float |  | feature 5 for ImageMol |
| feat_006 | float |  | feature 6 for ImageMol |
| feat_007 | float |  | feature 7 for ImageMol |
| feat_008 | float |  | feature 8 for ImageMol |
| feat_009 | float |  | feature 9 for ImageMol |

_10 of 512 columns are shown_
### Source and Deployment
- **Source:** `Local`
- **Source Type:** `External`
- **DockerHub**: [https://hub.docker.com/r/ersiliaos/eos4avb](https://hub.docker.com/r/ersiliaos/eos4avb)
- **Docker Architecture:** `AMD64`
- **S3 Storage**: [https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos4avb.zip](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos4avb.zip)

### Resource Consumption
- **Model Size (Mb):** `66`
- **Environment Size (Mb):** `1194`
- **Image Size (Mb):** `1432.26`

**Computational Performance (seconds):**
- 10 inputs: `24.89`
- 100 inputs: `17.2`
- 10000 inputs: `193.85`

### References
- **Source Code**: [https://github.com/HongxinXiang/ImageMol](https://github.com/HongxinXiang/ImageMol)
- **Publication**: [https://doi.org/10.1038/s42256-022-00557-6](https://doi.org/10.1038/s42256-022-00557-6)
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
