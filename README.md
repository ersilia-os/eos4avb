# Molecular representation learning

Representation Learning Framework that utilizes molecule images for encoding molecular inputs as machine readable vectors for downstream tasks such as bio-activity prediction, drug metabolism analysis, or drug toxicity prediction. The approach utilizes transfer learning, that is, pre-training the model on massive unlabeled datasets to help it in generalizing feature extraction and then fine tuning on specific tasks.

## Identifiers

* EOS model ID: `eos4avb`
* Slug: `image-mol-embeddings`

## Characteristics

* Input: `Compound`
* Input Shape: `Single`
* Task: `Representation`
* Output: `Descriptor`
* Output Type: `Float`
* Output Shape: `Matrix`
* Interpretation: ImageMol embeddings of shape [1, 512] reshaped as a Numpy 1D array before serializing. These embeddings can be used as the input features of a fully connected classification or regression layer in a neural network.

## References

* [Publication](https://www.nature.com/articles/s42256-022-00557-6)
* [Source Code](https://github.com/HongxinXiang/ImageMol)
* Ersilia contributor: [DhanshreeA](https://github.com/DhanshreeA)

## Citation

If you use this model, please cite the [original authors](https://www.nature.com/articles/s42256-022-00557-6) of the model and the [Ersilia Model Hub](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff).

## License

This package is licensed under a GPL-3.0 license. The model contained within this package is licensed under a MIT license.

Notice: Ersilia grants access to these models 'as is' provided by the original authors, please refer to the original code repository and/or publication if you use the model in your research.

## About Us

The [Ersilia Open Source Initiative](https://ersilia.io) is a Non Profit Organization ([1192266](https://register-of-charities.charitycommission.gov.uk/charity-search/-/charity-details/5170657/full-print)) with the mission is to equip labs, universities and clinics in LMIC with AI/ML tools for infectious disease research.

[Help us](https://www.ersilia.io/donate) achieve our mission!
