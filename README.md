# Image Generation from EEG Signals using Deep Learning Models

This research project was carried out during an internship at the University of Insubria.

## Abstract

This project investigates the generation of digit images from EEG signals using deep learning. The goal is to learn whether neural activity can be mapped into visual representations and whether a two-stage pipeline can produce meaningful reconstructions from brain signals.

The workflow combines a GAN-based generator for low-resolution digit synthesis with a super-resolution model to improve the final output quality.

## Research approach

The project follows a two-step pipeline:

1. Low-resolution generation: a GAN creates a coarse 32×32 image from EEG features. The GAN experiments documented in this repository were trained on digits only.
2. Super-resolution enhancement: an EDSR-based model upsamples the generated image to 128×128 pixels.

The repository also contains exploratory scripts and dataset utilities for character and image tasks. Those materials should not be interpreted as evidence that the GAN was trained or evaluated on those tasks.

## Project structure

- [src/gan](src/gan): GAN notebooks and supporting code for digit generation from EEG features.
- [src/super_resolution](src/super_resolution): EDSR implementation and dataset-preparation scripts.
- [eeg_raw_dataset/README.md](eeg_raw_dataset/README.md): reference and instructions for obtaining the raw EEG data locally. The EDF files are not included.
- [thoughtvizdataset/README.md](thoughtvizdataset/README.md): reference for the processed ThoughtViz dataset. The dataset files are not included.

The repository does not include the raw EEG, MNIST, DIV2K, benchmark or processed ThoughtViz datasets. Download and prepare them locally according to the relevant instructions before running the experiments.

## Scope of the published GAN results

The GAN experiments reported here were trained on digit data only. The repository also contains exploratory notebooks for character and image tasks, but they are not part of the reported digit results and should not be interpreted as validated models for those tasks.

## Technical details

### EDSR

The super-resolution module is based on the Enhanced Deep Residual Network (EDSR), a well-known architecture for single-image super-resolution. It uses residual learning to improve reconstruction quality while preserving image structure.

### Training configuration

- Loss function: L1 loss
- Epochs: 200
- Dataset: DIV2K
- Scale factor: 4×

### Evaluation metrics

- PSNR: peak signal-to-noise ratio
- SSIM: structural similarity index measure

The best performance was observed around the 188th training epoch.
