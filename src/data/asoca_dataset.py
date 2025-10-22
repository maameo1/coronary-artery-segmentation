"""
ASOCA dataset loader for coronary artery segmentation.
40 cases (20 normal, 20 diseased) with comprehensive annotations.
"""
import os
from typing import Optional, Callable, List
from pathlib import Path

from .base_dataset import BaseCoronaryDataset


class ASOCADataset(BaseCoronaryDataset):
    """
    ASOCA dataset (UK Data Service) - 40 cases with detailed annotations.

    Expected directory structure:
        asoca/
        ├── normal/
        │   ├── Normal_001/
        │   │   ├── image.nii.gz
        │   │   ├── label.nii.gz
        │   │   ├── centerline.txt
        │   │   └── ...
        │   └── ...
        └── diseased/
            ├── Diseased_001/
            │   ├── image.nii.gz
            │   ├── label.nii.gz
            │   └── ...
            └── ...

    Args:
        data_dir: Root directory containing ASOCA dataset
        transform: Optional transform to be applied on a sample
        split: Dataset split ('train', 'val', 'test', 'all')
        include_diseased: Whether to include diseased cases
        include_normal: Whether to include normal cases
    """

    def __init__(
        self,
        data_dir: str,
        transform: Optional[Callable] = None,
        split: str = "all",
        include_diseased: bool = True,
        include_normal: bool = True,
    ):
        super().__init__(data_dir, transform, split)

        self.include_diseased = include_diseased
        self.include_normal = include_normal

        # Load dataset file paths
        self._load_dataset()

    def _load_dataset(self):
        """
        Load image and label file paths from ASOCA directory structure.
        """
        normal_dir = self.data_dir / "normal"
        diseased_dir = self.data_dir / "diseased"

        # Collect case directories
        case_dirs = []

        if self.include_normal and normal_dir.exists():
            case_dirs.extend(sorted(normal_dir.glob("Normal_*")))

        if self.include_diseased and diseased_dir.exists():
            case_dirs.extend(sorted(diseased_dir.glob("Diseased_*")))

        if len(case_dirs) == 0:
            raise ValueError(f"No cases found in {self.data_dir}")

        # Load image and label paths from each case
        for case_dir in case_dirs:
            image_path = case_dir / "image.nii.gz"
            label_path = case_dir / "label.nii.gz"

            # Alternative naming conventions
            if not image_path.exists():
                image_path = case_dir / f"{case_dir.name}.nii.gz"
            if not label_path.exists():
                label_path = case_dir / f"{case_dir.name}_label.nii.gz"

            if image_path.exists() and label_path.exists():
                self.image_paths.append(image_path)
                self.label_paths.append(label_path)
            else:
                print(f"Warning: Missing files in {case_dir.name}")

        # Apply split if specified (for ASOCA, typically use all for validation)
        if self.split != "all":
            # Simple split: first 70% train, next 15% val, last 15% test
            n = len(self.image_paths)
            if self.split == "train":
                end_idx = int(0.7 * n)
                self.image_paths = self.image_paths[:end_idx]
                self.label_paths = self.label_paths[:end_idx]
            elif self.split == "val":
                start_idx = int(0.7 * n)
                end_idx = int(0.85 * n)
                self.image_paths = self.image_paths[start_idx:end_idx]
                self.label_paths = self.label_paths[start_idx:end_idx]
            elif self.split == "test":
                start_idx = int(0.85 * n)
                self.image_paths = self.image_paths[start_idx:]
                self.label_paths = self.label_paths[start_idx:]

    def get_stats(self):
        """
        Get dataset statistics.
        """
        stats = super().get_stats()
        stats.update({
            'dataset': 'ASOCA',
            'include_diseased': self.include_diseased,
            'include_normal': self.include_normal,
        })
        return stats
