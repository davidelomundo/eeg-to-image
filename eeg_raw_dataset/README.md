# eeg_raw_dataset

Reference directory for the raw EEG acquisition dataset used by the preprocessing pipeline.

The EDF files are intentionally **not included in this repository** because they contain raw EEG recordings and may be subject to privacy, ethical, and redistribution restrictions. Obtain the dataset from its official source and place the files locally in this directory before running preprocessing.

## Dataset Overview

**Structure and task labels:**

```text
eeg_raw_dataset/
├── Char/       (A, C, F, H, J, M, P, S, T, Y)
├── Digit/      (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
└── Image/      (Apple, Car, Dog, Gold, Mobile, Rose, Scooter, Tiger, Wallet, Watch)
```

**File naming pattern in the source dataset:**

```text
name<subject_or_session>_<label>.edf
```

Examples:
- Char: `name0_A.edf`, `name10_Y.edf`
- Digit: `name0_0.edf`, `name10_9.edf`
- Image: `name0_Apple.edf`, `name10_Watch.edf`
## Usage

Use the locally obtained EDF files from this folder for preprocessing/conversion scripts. The output should be written to `../thoughtvizdataset` for model training.


## Source

Dataset source: [ThoughtViz dataset on Kaggle](https://www.kaggle.com/datasets/adiwcode/thoughtvizdataset)

Check the dataset's current license and access conditions before downloading or redistributing it. This repository does not redistribute the raw EDF recordings.
