# Configuration Files

This directory contains configuration files for different experimental setups.

## Structure

- `base_config.yaml` - Base configuration with default parameters
- `data_regimes/` - Configurations for different training data sizes
- `models/` - Model-specific configurations (ImageNet, RadImageNet, CT-FM pretraining)

## Data Regimes

The data regime configurations test model performance with limited training data:

- `regime_5.yaml` - 5 training cases
- `regime_10.yaml` - 10 training cases
- `regime_20.yaml` - 20 training cases
- `regime_30.yaml` - 30 training cases
- `regime_50.yaml` - 50 training cases
- `regime_100.yaml` - 100 training cases
- `regime_200.yaml` - 200 training cases
- `regime_full.yaml` - All available training data

## Usage

Configurations can be loaded and merged using OmegaConf or similar tools:

```python
from omegaconf import OmegaConf

# Load base config
config = OmegaConf.load('configs/base_config.yaml')

# Override with specific regime
regime_config = OmegaConf.load('configs/data_regimes/regime_20.yaml')
config = OmegaConf.merge(config, regime_config)
```

## Modifying Configurations

To run experiments with different settings:

1. Copy an existing config file
2. Modify the parameters
3. Save with a descriptive name
4. Reference in your training script

## Key Parameters

### Data
- `num_samples`: Number of training cases to use
- `spatial_size`: Patch size for training
- `pixdim`: Target voxel spacing

### Model
- `architecture`: Model architecture (unet, unet++, etc.)
- `pretrained`: Pretrained weights (null, imagenet, radimagenet, ctfm)

### Training
- `epochs`: Number of training epochs
- `learning_rate`: Initial learning rate
- `loss`: Loss function (dice, ce, dice_ce)
