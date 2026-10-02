# 📊 Infection Control & Health Survey Analysis

Statistical analysis scripts, data processing workflows, and visualization generators for healthcare research surveys.

## 🔬 Overview
This repository contains data processing tools, Python analysis scripts, dataset normalization utilities, and auto-generated chart figures for medical/nursing research surveys:
* **Assessment of Infection Prevention & Control Practices Among Nurses**
* **Intimate Hygiene Practices & Awareness Study**

## 🛠️ Features & Pipeline
- **Dataset Expansion & Normalization:** `expand_dataset.py`, `dataset_103_physical+online.csv`
- **Statistical Analysis:** `run_analysis.py`, `analysis_results.txt`
- **Data Visualization:** `generate_figures.py` (Generates demographic breakdowns, knowledge scores, practice compliance charts, and barrier analyses saved to `figures/`)
- **HTML Research Paper Generator:** `research_paper_complete.html` — Formatted research publication draft with embedded charts and tables.

## 📂 Key Files & Structure
```
survey/
├── run_analysis.py              # Main statistical execution script
├── generate_figures.py          # Seaborn/Matplotlib chart generator
├── dataset_103_physical+online.csv # Survey dataset
├── research_paper_complete.html # HTML Research Paper draft
├── figures/                     # Auto-generated visualization charts (PNG)
└── atiya_research/              # Sub-study: Intimate Hygiene Survey & Analysis
```

## 🚀 Dependencies
```bash
pip install pandas numpy matplotlib seaborn
```
