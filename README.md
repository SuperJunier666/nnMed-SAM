
## The SAM trained on 2D natural images used by nnsam has limited improvement for 3D medical images. Therefore, using Med SAM, which is pre-trained on medical image datasets, is better suited to the task of segmenting medical images.

## checkpoint for Med SAM 3D: [SAM-Med3D-Turbo](https://drive.google.com/file/d/1MuqYRQKIZb4YPtEraK8zTKKpp-dUQIR9/view?usp=sharing)

## Our entire code is built based on nnUNet, and you can follow the nnUNet instructions exactly.


```bash
conda create -n nnsam python=3.9
conda activate nnsam
pip install git+https://github.com/ChaoningZhang/MobileSAM.git
pip install timm
pip install git+https://github.com/SuperJunier666/nnMed-SAM.git
```

It is important to input "set MODEL_NAME=nnsam" before using it.
```bash
set MODEL_NAME=nnsam
```

```bash
nnUNetv2_plan_and_preprocess -d DATASET_ID --verify_dataset_integrity

nnUNetv2_train DATASET_NAME_OR_ID UNET_CONFIGURATION FOLD [additional options, see -h]

nnUNetv2_train DATASET_NAME_OR_ID UNET_CONFIGURATION FOLD --val --npz

nnUNetv2_train DATASET_NAME_OR_ID 2d FOLD

nnUNetv2_train DATASET_NAME_OR_ID 3d_fullres FOLD

nnUNetv2_predict -i INPUT_FOLDER -o OUTPUT_FOLDER -d DATASET_NAME_OR_ID -c CONFIGURATION --save_probabilities
```


## How to get started?
Read these:
- [Dataset conversion](documentation/dataset_format.md)
- [Usage instructions](documentation/how_to_use_nnunet.md)

Additional information:
- [Region-based training](documentation/region_based_training.md)
- [Manual data splits](documentation/manual_data_splits.md)
- [Pretraining and finetuning](documentation/pretraining_and_finetuning.md)
- [Intensity Normalization in nnU-Net](documentation/explanation_normalization.md)
- [Manually editing nnU-Net configurations](documentation/explanation_plans_files.md)
- [Extending nnU-Net](documentation/extending_nnunet.md)
- [What is different in V2?](documentation/changelog.md)


