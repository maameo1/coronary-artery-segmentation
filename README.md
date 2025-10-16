# Coronary Artery Segmentation

Data-efficient deep learning for automated coronary artery segmentation from CT Coronary Angiography (CTCA).

Part of my PhD research at University of Lincoln investigating minimum training data requirements for clinical AI deployment.

## Project Overview

This project investigates how much training data is actually needed for clinically-acceptable coronary artery segmentation performance. We test various transfer learning approaches (ImageNet, RadImageNet, CT-FM) on limited training data (5-30 cases).

## Methods

- **Architecture:** U-Net with encoder-decoder structure
- **Framework:** PyTorch + MONAI
- **Dataset:** ASOCA (Automated Segmentation of Coronary Arteries)
- **Approach:** Transfer learning from pretrained models
- **Evaluation:** 5-fold cross-validation

## Preliminary Results

*Work in progress - results coming soon*

- Baseline U-Net (random init): Dice ~0.XX
- ImageNet pretrained: Dice ~0.XX
- CT-FM pretrained: Dice ~0.XX

## 🛠️ Installation
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
├── src/
│   ├── models/          # Model architectures
│   ├── data/            # Data loading and preprocessing
│   └── utils/           # Utility functions
├── notebooks/           # Jupyter notebooks for exploration
├── configs/             # Configuration files
├── requirements.txt     # Python dependencies
└── README.md           # This file
```

## 📚 Dependencies

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
