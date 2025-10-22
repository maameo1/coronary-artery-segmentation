"""
Base dataset class for coronary artery segmentation.
"""
import os
from typing import Optional, Callable, List, Dict, Any
from pathlib import Path

import torch
from torch.utils.data import Dataset
import numpy as np
import nibabel as nib
from monai.transforms import Compose


class BaseCoronaryDataset(Dataset):
    """
    Base dataset class for coronary artery segmentation from CTCA.

    Args:
        data_dir: Root directory containing the dataset
        transform: Optional transform to be applied on a sample
        split: Dataset split ('train', 'val', 'test')
        num_samples: Optional limit on number of samples to use (for data regime experiments)
    """

    def __init__(
        self,
        data_dir: str,
        transform: Optional[Callable] = None,
        split: str = "train",
        num_samples: Optional[int] = None,
    ):
        self.data_dir = Path(data_dir)
        self.transform = transform
        self.split = split
        self.num_samples = num_samples

        # To be populated by child classes
        self.image_paths: List[Path] = []
        self.label_paths: List[Path] = []

    def __len__(self) -> int:
        return len(self.image_paths)

    def __getitem__(self, idx: int) -> Dict[str, Any]:
        """
        Load and return a sample from the dataset.

        Returns:
            Dictionary containing:
                - 'image': CT volume (numpy array)
                - 'label': Segmentation mask (numpy array)
                - 'image_path': Path to image file
                - 'label_path': Path to label file
        """
        image_path = self.image_paths[idx]
        label_path = self.label_paths[idx]

        # Load image and label
        image = self._load_volume(image_path)
        label = self._load_volume(label_path)

        # Create sample dictionary
        sample = {
            'image': image,
            'label': label,
            'image_path': str(image_path),
            'label_path': str(label_path),
        }

        # Apply transforms if provided
        if self.transform:
            sample = self.transform(sample)

        return sample

    def _load_volume(self, path: Path) -> np.ndarray:
        """
        Load a medical imaging volume from file.

        Supports: .nii, .nii.gz formats
        """
        if path.suffix in ['.nii', '.gz']:
            img = nib.load(str(path))
            volume = img.get_fdata()
        else:
            raise ValueError(f"Unsupported file format: {path.suffix}")

        return volume.astype(np.float32)

    def get_stats(self) -> Dict[str, Any]:
        """
        Compute and return dataset statistics.
        """
        return {
            'num_samples': len(self),
            'split': self.split,
            'data_dir': str(self.data_dir),
        }
