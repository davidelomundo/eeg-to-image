# thoughtvizdataset

Processed dataset used by the EEG-to-image training pipeline.

This folder contains:
- EEG data serialized as `.pkl` files (one for each task: char, digit, image)
- Ground-truth image datasets split into `train`, `val`, and `test`

## Purpose

`thoughtvizdataset` is the **model-ready dataset** (processed version), not the raw EDF acquisition folder.

- Raw acquisition data: `../eeg_raw_dataset`
- Processed/training-ready data: `./thoughtvizdataset`

## Structure

```text
thoughtvizdataset/
├── eeg/
│   ├── char/data.pkl
│   ├── digit/data.pkl
│   └── image/data.pkl
├── charimages/
│   ├── train/{a,c,f,h,j,m,p,s,t,y}/
│   ├── val/{a,c,f,h,j,m,p,s,t,y}/
│   └── test/{a,c,f,h,j,m,p,s,t,y}/
└── images/
	├── train/{apple,car,dog,...}/
	├── val/{apple,car,dog,...}/
	└── test/{apple,car,dog,...}/
```

## Label sets

### Char task
- `a, c, f, h, j, m, p, s, t, y`

### Digit task
- `0..9`

### Image task
- `apple, car, dog, gold, mobile, rose, scooter, tiger, wallet, watch`

## Source

Dataset source: https://www.kaggle.com/datasets/adiwcode/thoughtvizdataset

