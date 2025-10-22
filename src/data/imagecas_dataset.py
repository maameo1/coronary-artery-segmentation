"""
ImageCAS dataset loader for coronary artery segmentation.
1000 3D CTA volumes with coronary artery lumen segmentation labels.
"""
import os
from typing import Optional, Callable, List
from pathlib import Path
import random

from .base_dataset import BaseCoronaryDataset


class ImageCASDataset(BaseCoronaryDataset):
    """
    ImageCAS dataset (Kaggle) - 1000 3D CTA volumes.

    Expected directory structure:
        imagecas/
        ├── images/
        │   ├── case_001.nii.gz
        │   ├── case_002.nii.gz
        │   └── ...
        └── labels/
            ├── case_001.nii.gz
            ├── case_002.nii.gz
            └── ...

    Args:
        data_dir: Root directory containing ImageCAS dataset
        transform: Optional transform to be applied on a sample
        split: Dataset split ('train', 'val', 'test')
        num_samples: Optional limit on number of samples (for data regime experiments)
        fold: Cross-validation fold number (0-4) for 5-fold CV
        seed: Random seed for reproducible splits
    """

    def __init__(
        self,
        data_dir: str,
        transform: Optional[Callable] = None,
        split: str = "train",
        num_samples: Optional[int] = None,
        fold: int = 0,
        seed: int = 42,
    ):
        super().__init__(data_dir, transform, split, num_samples)

        self.fold = fold
        self.seed = seed

        # Load dataset file paths
        self._load_dataset()

        # Apply sample limit if specified (for data regime experiments)
        if num_samples is not None and num_samples < len(self.image_paths):
            random.seed(seed)
            indices = random.sample(range(len(self.image_paths)), num_samples)
            self.image_paths = [self.image_paths[i] for i in indices]
            self.label_paths = [self.label_paths[i] for i in indices]

    def _load_dataset(self):
        """
        Load image and label file paths and create train/val/test splits.
        """
        images_dir = self.data_dir / "images"
        labels_dir = self.data_dir / "labels"

        if not images_dir.exists():
            raise FileNotFoundError(f"Images directory not found: {images_dir}")
        if not labels_dir.exists():
            raise FileNotFoundError(f"Labels directory not found: {labels_dir}")

        # Get all image files
        image_files = sorted(list(images_dir.glob("*.nii.gz")) + list(images_dir.glob("*.nii")))

        if len(image_files) == 0:
            raise ValueError(f"No image files found in {images_dir}")

        # Create 5-fold cross-validation splits
        total_samples = len(image_files)
        fold_size = total_samples // 5

        # Determine indices for current fold
        val_start = self.fold * fold_size
        val_end = (self.fold + 1) * fold_size if self.fold < 4 else total_samples
        test_start = ((self.fold + 1) % 5) * fold_size
        test_end = ((self.fold + 2) % 5) * fold_size if self.fold < 3 else total_samples

        # Split indices
        all_indices = list(range(total_samples))
        val_indices = set(range(val_start, val_end))
        test_indices = set(range(test_start, test_end))
        train_indices = set(all_indices) - val_indices - test_indices

        # Select indices based on split
        if self.split == "train":
            selected_indices = sorted(train_indices)
        elif self.split == "val":
            selected_indices = sorted(val_indices)
        elif self.split == "test":
            selected_indices = sorted(test_indices)
        else:
            raise ValueError(f"Invalid split: {self.split}. Must be 'train', 'val', or 'test'")

        # Get file paths for selected indices
        for idx in selected_indices:
            image_path = image_files[idx]
            label_path = labels_dir / image_path.name

            if label_path.exists():
                self.image_paths.append(image_path)
                self.label_paths.append(label_path)
            else:
                print(f"Warning: Label not found for {image_path.name}")

    def get_stats(self):
        """
        Get dataset statistics.
        """
        stats = super().get_stats()
        stats.update({
            'dataset': 'ImageCAS',
            'fold': self.fold,
            'seed': self.seed,
        })
        return stats
