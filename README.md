# nnMed-SAM 🔬🧠

**nnMed-SAM** is a medical image segmentation project built upon the powerful [nnUNet](https://github.com/MIC-DKFZ/nnUNet) framework. It integrates the medical-domain-specific Segment Anything Model (**MedSAM**) to significantly improve segmentation performance on 3D medical images.

---

## 🔍 Why MedSAM?

The original SAM model was trained on natural images and has limited performance on 3D medical data. In contrast, **MedSAM** is pre-trained on large-scale medical image datasets, making it much more suitable for segmentation tasks in the medical domain.

**Recommended MedSAM checkpoint:**

- 📦 [SAM-Med3D-Turbo Download Link](https://drive.google.com/file/d/1MuqYRQKIZb4YPtEraK8zTKKpp-dUQIR9/view?usp=sharing)

---

## 🚀 Quick Start

### 1. Create and activate the environment

```bash
conda create -n nnMedSam python=3.9
conda activate nnMedSam
```

### 2. Install dependencies

```
pip install git+https://github.com/ChaoningZhang/MobileSAM.git
pip install timm
pip install git+https://github.com/SuperJunier666/nnMed-SAM.git
```

### 3. Set environment variable for model name (Windows)

```bash
set MODEL_NAME=nnsam
```

------

## 🧠 How to Use

This project is fully based on `nnUNet`, so its usage follows the standard `nnUNet` pipeline. You can follow the commands below for training and inference:

### Data Preprocessing

```bash
nnUNetv2_plan_and_preprocess -d <DATASET_ID> --verify_dataset_integrity
```

### Model Training

```bash
nnUNetv2_train <DATASET_NAME_OR_ID> <CONFIGURATION> <FOLD>

# Example: Train a 2D model
nnUNetv2_train <DATASET_NAME_OR_ID> 2d <FOLD>

# Example: Train a 3D model
nnUNetv2_train <DATASET_NAME_OR_ID> 3d_fullres <FOLD>

# Enable validation and save predicted probabilities
nnUNetv2_train <DATASET_NAME_OR_ID> <CONFIGURATION> <FOLD> --val --npz
```

### Model Inference

```bash
nnUNetv2_predict -i <INPUT_FOLDER> -o <OUTPUT_FOLDER> -d <DATASET_NAME_OR_ID> -c <CONFIGURATION> --save_probabilities
```

------

## 📚 How to Get Started?

Read these first:

- 📁 [Dataset conversion](documentation/dataset_format.md) 
- ⚙️ [Usage instructions](documentation/how_to_use_nnunet.md) 

Additional information:

- 🧩 [Region-based training](documentation/region_based_training.md) 
- ✂️ [Manual data splits](documentation/manual_data_splits.md) 
- 🔄 [Pretraining and finetuning](documentation/pretraining_and_finetuning.md) 
- 🌈 [Intensity Normalization in nnU-Net](documentation/explanation_normalization.md) 
- 📝 [Manually editing nnU-Net configurations](documentation/explanation_plans_files.md) 
- 🧠 [Extending nnU-Net](documentation/extending_nnunet.md)
- 🆕 [What is different in V2?](documentation/changelog.md) 

------

## 🤝 Acknowledgements

This project is built upon the following excellent open-source repositories:

- [nnUNet](https://github.com/MIC-DKFZ/nnUNet)
- [MobileSAM](https://github.com/ChaoningZhang/MobileSAM)
- [SAM-Med3D](https://github.com/openmedlab/SAM-Med3D)
