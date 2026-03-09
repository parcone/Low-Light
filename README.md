# Low-Light

This folder contains a collection of low-light image enhancement datasets for research and development in computer vision and image processing.

## Included Datasets

### DICM
- Path: `DICM/`
- Content: 44 low-light images (`.jpg/.JPG`)

### ExDark
- Path: `ExDark/`
- Structure:
  - `images/` (organized by category)
  - `Annnotations/` (corresponding annotations)
- Categories: Bicycle, Boat, Bottle, Bus, Car, Cat, Chair, Cup, Dog, Motorbike, People, Table

### LIME
- Path: `LIME/`
- Content: 10 low-light images (`.bmp`)

### LOL (Low-Light)
- Path: `LOL/`
- Structure:
  - `our485/low` + `our485/high` (train)
  - `eval15/low` + `eval15/high` (eval)
- Paired dataset for supervised enhancement

### MEF (Multi-Exposure Fusion)
- Path: `MEF/`
- Content: multi-exposure images (`.png`)

### NPE (Natural Photo Enhancement)
- Path: `NPE/`
- Content: mixed-format photos (`.jpg/.jpeg/.bmp`)

### SICE
- Path: `SICE/`
- Structure:
  - `Dataset_Part1/Lowlight_img` + `Dataset_Part1/Lowlight_img_Label`
  - `Dataset_Part2/Lowlight_img` + `Dataset_Part2/Lowlight_img_Label`
  - train/val lists: `train_list.txt`, `val_list.txt`
- Scripts: `dataset_make.py`, `dataset_txt.py`, `test_data.py`, `test_data_resize.py`

### VV
- Path: `VV/`
- Content: 25 low-light images (`.jpg`)

## Notes
- Some datasets are paired (e.g., LOL, SICE) and can be used for supervised training.
- ExDark includes annotations for low-light detection/classification research.

## License / Citation
Please follow the original dataset licenses and cite their original papers when used in research.
