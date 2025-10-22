"""
Data preprocessing and augmentation transforms for coronary artery segmentation.
Uses MONAI for medical imaging specific transforms.
"""
from typing import Optional, Tuple

from monai.transforms import (
    Compose,
    LoadImaged,
    EnsureChannelFirstd,
    Orientationd,
    Spacingd,
    ScaleIntensityRanged,
    CropForegroundd,
    RandCropByPosNegLabeld,
    RandRotate90d,
    RandFlipd,
    RandAffined,
    RandGaussianNoised,
    RandGaussianSmoothd,
    RandScaleIntensityd,
    ToTensord,
)


def get_train_transforms(
    spatial_size: Tuple[int, int, int] = (96, 96, 96),
    a_min: float = -200.0,
    a_max: float = 300.0,
    pixdim: Tuple[float, float, float] = (1.0, 1.0, 1.0),
) -> Compose:
    """
    Get training transforms with data augmentation.

    Args:
        spatial_size: Target spatial size for cropped patches
        a_min: Minimum HU value for intensity windowing
        a_max: Maximum HU value for intensity windowing
        pixdim: Target spacing in mm

    Returns:
        Composed transform for training
    """
    transforms = Compose([
        # Ensure correct orientation and spacing
        EnsureChannelFirstd(keys=["image", "label"]),
        Orientationd(keys=["image", "label"], axcodes="RAS"),
        Spacingd(
            keys=["image", "label"],
            pixdim=pixdim,
            mode=("bilinear", "nearest"),
        ),

        # Intensity normalization (CT-specific HU windowing)
        ScaleIntensityRanged(
            keys=["image"],
            a_min=a_min,
            a_max=a_max,
            b_min=0.0,
            b_max=1.0,
            clip=True,
        ),

        # Crop foreground to focus on anatomy
        CropForegroundd(
            keys=["image", "label"],
            source_key="image",
            margin=10,
        ),

        # Random crop patches (balanced positive/negative samples)
        RandCropByPosNegLabeld(
            keys=["image", "label"],
            label_key="label",
            spatial_size=spatial_size,
            pos=1,  # Probability of crop centered on foreground
            neg=1,  # Probability of crop from anywhere
            num_samples=2,  # Number of crops per volume
        ),

        # Data augmentation
        RandRotate90d(
            keys=["image", "label"],
            prob=0.5,
            spatial_axes=(0, 1),
        ),
        RandFlipd(
            keys=["image", "label"],
            prob=0.5,
            spatial_axis=0,
        ),
        RandFlipd(
            keys=["image", "label"],
            prob=0.5,
            spatial_axis=1,
        ),
        RandFlipd(
            keys=["image", "label"],
            prob=0.5,
            spatial_axis=2,
        ),
        RandAffined(
            keys=["image", "label"],
            prob=0.2,
            rotate_range=(0.1, 0.1, 0.1),
            scale_range=(0.1, 0.1, 0.1),
            mode=("bilinear", "nearest"),
        ),

        # Intensity augmentation
        RandGaussianNoised(keys=["image"], prob=0.15, mean=0.0, std=0.01),
        RandGaussianSmoothd(
            keys=["image"],
            prob=0.15,
            sigma_x=(0.5, 1.0),
            sigma_y=(0.5, 1.0),
            sigma_z=(0.5, 1.0),
        ),
        RandScaleIntensityd(keys=["image"], factors=0.1, prob=0.15),

        # Convert to tensor
        ToTensord(keys=["image", "label"]),
    ])

    return transforms


def get_val_transforms(
    a_min: float = -200.0,
    a_max: float = 300.0,
    pixdim: Tuple[float, float, float] = (1.0, 1.0, 1.0),
) -> Compose:
    """
    Get validation/test transforms (no augmentation).

    Args:
        a_min: Minimum HU value for intensity windowing
        a_max: Maximum HU value for intensity windowing
        pixdim: Target spacing in mm

    Returns:
        Composed transform for validation/testing
    """
    transforms = Compose([
        # Ensure correct orientation and spacing
        EnsureChannelFirstd(keys=["image", "label"]),
        Orientationd(keys=["image", "label"], axcodes="RAS"),
        Spacingd(
            keys=["image", "label"],
            pixdim=pixdim,
            mode=("bilinear", "nearest"),
        ),

        # Intensity normalization
        ScaleIntensityRanged(
            keys=["image"],
            a_min=a_min,
            a_max=a_max,
            b_min=0.0,
            b_max=1.0,
            clip=True,
        ),

        # Convert to tensor
        ToTensord(keys=["image", "label"]),
    ])

    return transforms


def get_inference_transforms(
    a_min: float = -200.0,
    a_max: float = 300.0,
    pixdim: Tuple[float, float, float] = (1.0, 1.0, 1.0),
) -> Compose:
    """
    Get inference transforms (image only, no labels).

    Args:
        a_min: Minimum HU value for intensity windowing
        a_max: Maximum HU value for intensity windowing
        pixdim: Target spacing in mm

    Returns:
        Composed transform for inference
    """
    transforms = Compose([
        EnsureChannelFirstd(keys=["image"]),
        Orientationd(keys=["image"], axcodes="RAS"),
        Spacingd(
            keys=["image"],
            pixdim=pixdim,
            mode="bilinear",
        ),
        ScaleIntensityRanged(
            keys=["image"],
            a_min=a_min,
            a_max=a_max,
            b_min=0.0,
            b_max=1.0,
            clip=True,
        ),
        ToTensord(keys=["image"]),
    ])

    return transforms
