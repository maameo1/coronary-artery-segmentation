# Coronary Artery Segmentation

Data-efficient deep learning for automated coronary artery segmentation from CT Coronary Angiography (CTCA).

Part of my PhD research at University of Lincoln investigating minimum training data requirements for clinical AI deployment.

## Project Overview

This project investigates how much training data is actually needed for clinically-acceptable coronary artery segmentation performance. We test various transfer learning approaches (ImageNet, RadImageNet, CT-FM) on limited training data (5-30 cases).

## Methods

- **Architecture:** U-Net with encoder-decoder structure
- **Framework:** PyTorch + MONAI
- **Datasets:** ImageCAS (primary), ASOCA (validation), Rotterdam (exploratory)
- **Approach:** Transfer learning from pretrained models (ImageNet, RadImageNet, CT-FM)
- **Data Regimes:** Testing with 5, 10, 20, 30, 50, 100, 200+ training cases
- **Evaluation:** 5-fold cross-validation

## Datasets

### Primary Dataset: ImageCAS
- **Cases:** 1000 3D CTA volumes
- **Annotations:** Coronary artery lumen segmentation labels
- **Source:** Kaggle (publicly available)
- **Access:** Free download, no restrictions
- **Usage:** Main training and testing for learning curve experiments across multiple data regimes

### Validation Dataset: ASOCA
- **Cases:** 40 (20 normal, 20 diseased)
- **Annotations:** Voxel-wise lumen segmentation, centrelines, vessel meshes, calcification
- **Source:** UK Data Service (Gharleghi et al. 2023)
- **Access:** Permission requested
- **Usage:** Established benchmark for direct comparison with literature

### Exploratory Dataset: Rotterdam Collaboration
- **Purpose:** Pipeline development and feasibility testing only
- **Source:** Available via MUET collaboration
- **Note:** Not used for publication results

## Preliminary Results

*Work in progress - results coming soon*

- Baseline U-Net (random init): Dice ~0.XX
- ImageNet pretrained: Dice ~0.XX
- RadImageNet pretrained: Dice ~0.XX
- CT-FM pretrained: Dice ~0.XX

## Installation
```bash
# Clone repository
git clone https://github.com/[your-username]/coronary-artery-segmentation.git
cd coronary-artery-segmentation

# Install dependencies
pip install -r requirements.txt
```

## Usage
```python
# Example usage (coming soon)
from src.models import UNet
from src.data import CoronaryDataLoader

# Load model
model = UNet(in_channels=1, out_channels=2)

# Train
# ...
```

## Project Structure
```
coronary-artery-segmentation/
├── data/                # Data directory (not tracked in git)
│   ├── imagecas/        # ImageCAS dataset
│   ├── asoca/           # ASOCA dataset
│   └── rotterdam/       # Rotterdam exploratory data
├── src/
│   ├── models/          # Model architectures (U-Net variants)
│   ├── data/            # Data loading and preprocessing
│   ├── training/        # Training loops and utilities
│   └── utils/           # Utility functions
├── notebooks/           # Jupyter notebooks for exploration
├── configs/             # Configuration files for different experiments
│   ├── data_regimes/    # Configs for 5, 10, 20, 30, 50, 100, 200 cases
│   └── models/          # Model configuration files
├── experiments/         # Experiment results and logs
├── requirements.txt     # Python dependencies
└── README.md           # This file
```

## Dependencies

- Python 3.8+
- PyTorch 2.0+
- MONAI
- NumPy
- Pandas
- Matplotlib

## Related Publications

*In preparation:* "Data Requirements for Coronary Artery Segmentation: A Systematic Review and Empirical Analysis" - To be submitted to MIUA 2026

## Author

**Maame Owusu-Ansah**
- PhD Researcher, University of Lincoln
- Email: maameowusu01@gmail.com
- LinkedIn: [linkedin.com/in/maame-owusu-ansah](https://linkedin.com/in/maame-owusu-ansah)

## License

MIT License - see LICENSE file for details

## Acknowledgments

- University of Lincoln
- Lincolnshire Heart Centre
- ASOCA dataset creators
