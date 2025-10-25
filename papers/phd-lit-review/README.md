# PhD Literature Review

Organized literature review for coronary artery segmentation PhD research.

## Structure

```
phd-lit-review/
├── literature-review.csv    # Main tracking spreadsheet
├── notes/                   # Detailed paper notes (one file per paper)
├── figures/                 # Screenshots, diagrams, architecture images
└── README.md               # This file
```

## Workflow

### 1. Adding a New Paper

1. Add a new row to `literature-review.csv` with:
   - Author (first author surname)
   - Year
   - Title
   - Venue (journal/conference)
   - Topic (e.g., "Coronary Segmentation", "Transfer Learning", "Data Efficiency")
   - Methods (brief description)
   - Dataset (which datasets used)
   - Key Findings (1-2 sentences)
   - Relevance (High/Medium/Low to your research)
   - Status (To Read/Reading/Read/Key Paper)
   - Notes File (filename in notes/ directory)
   - DOI/URL

2. Create detailed notes file in `notes/` with format: `author-year-short-title.md`

### 2. Note-Taking Template

Create files in `notes/` following this structure:

```markdown
# [Paper Title]

**Authors:** [Full author list]
**Year:** [Year]
**Venue:** [Journal/Conference]
**DOI:** [Link]

## Summary

[2-3 sentence overview of the paper]

## Problem Statement

[What problem does this paper address?]

## Methods

- Architecture:
- Training approach:
- Dataset(s):
- Evaluation metrics:

## Key Results

[Main findings, numbers, comparisons]

## Strengths

-
-

## Limitations

-
-

## Relevance to My Research

[How does this relate to your coronary artery segmentation work?]

## Key Takeaways

-
-

## Figures/Architecture

[Save important figures to ../figures/ and reference here]

## Citations to Follow

-
-
```

### 3. Organizing Figures

Save figures/screenshots to `figures/` with descriptive names:
- `chen-2024-architecture.png`
- `wang-2023-results-table.png`
- `dataset-comparison.png`

## CSV Column Guide

- **Author**: First author surname (e.g., "Chen")
- **Year**: Publication year
- **Title**: Full paper title
- **Venue**: Journal or conference name (e.g., "Medical Image Analysis", "MICCAI")
- **Topic**: Research area (Coronary Segmentation, Transfer Learning, U-Net, etc.)
- **Methods**: Brief method description (e.g., "U-Net with attention")
- **Dataset**: Datasets used (e.g., "ASOCA, ImageCAS")
- **Key Findings**: Main result or contribution
- **Relevance**: High/Medium/Low for your research
- **Status**: To Read | Reading | Read | Key Paper
- **Notes File**: Filename in notes/ (e.g., "chen-2024-ai-ccta.md")
- **DOI/URL**: Direct link to paper

## Research Topics for Your Project

Organize papers by these key topics:

1. **Coronary Artery Segmentation**
   - Deep learning methods
   - Traditional approaches
   - Centerline extraction

2. **Data Efficiency**
   - Few-shot learning
   - Small dataset performance
   - Sample size studies

3. **Transfer Learning**
   - ImageNet pretraining
   - RadImageNet
   - CT-FM and medical domain pretraining

4. **Datasets & Benchmarks**
   - ImageCAS
   - ASOCA
   - Other coronary datasets

5. **U-Net Variants**
   - Architecture improvements
   - Encoder modifications
   - Attention mechanisms

## Tips

- Review CSV weekly to track progress
- Tag papers with multiple topics if relevant
- Link related papers in your notes
- Update Status as you progress through reading
- Export CSV to Excel/Google Sheets for easier filtering
- Keep notes concise but capture key insights
- Save representative figures for presentations/thesis

## Quick Stats

Track your progress:
- Papers to read: [Count from CSV]
- Papers read: [Count from CSV]
- Key papers identified: [Count from CSV]
- Notes completed: [Count files in notes/]
