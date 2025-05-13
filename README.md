# Usual_analysis# Traceology-Based Tool Prediction with Machine Learning

## Project Overview

This project applies machine learning techniques to predict the type of prehistoric tool or weapon responsible for wear marks observed on archaeological artifacts. The work is developed in collaboration with a traceologist who provided a large and well-documented experimental dataset.

---

## Objectives

* Analyze wear marks on archaeological objects (striation patterns, polish intensity, angles, textures...).
* Build a supervised classification model to identify the likely tool (e.g., axe, knife, scraper, etc.).
* Offer a simple interface to test new data and assist experts with predictions.

---

## Data

* Format: CSV (originally converted from Excel files)
* Content:

  * Quantitative variables: geometric measurements, polish intensity, striation orientation...
  * Categorical variables: surface type, analysis method, material worked...
  * Target label: the type of tool or object that caused the traces

> **Note**: Data is not shared in this repository for confidentiality reasons.

---

## Tech Stack

* Python 3.12
* pandas, numpy, scikit-learn
* XGBoost
* SHAP (for model interpretation)
* Streamlit (optional, for a user-friendly interface)

---

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/your-username/traceology-ml.git
   cd traceology-ml
   ```

2. Create a virtual environment and install the required packages:

   ```bash
   python -m venv venv
   source venv/bin/activate  # or `venv\Scripts\activate` on Windows
   pip install -r requirements.txt
   ```

---

## Usage

1. Place your CSV data files into the `data/` directory.
2. Run the notebook `notebooks/train_model.ipynb` to train the model.
3. Model performance metrics (accuracy, confusion matrix, SHAP values, etc.) will be displayed in the notebook.
4. (Optional) To run the Streamlit interface:

   ```bash
   streamlit run app.py
   ```

---

## Project Structure

```
traceology-ml/
├── data/                 # Folder for input CSV files
├── notebooks/            # Jupyter notebooks for exploration and training
│   └── train_model.ipynb
├── models/               # Trained models (saved in joblib or pickle format)
├── app.py                # Streamlit interface (optional)
├── requirements.txt      # Python dependencies
└── README.md
```

---

## Authors & Contributors

* **Adrien Piette** – Data Scientist & Developer
* **\[Name of Archaeologist]** – Traceology Expert

---

## Future Work

* Add active learning with expert feedback to improve model performance.
* Extend the project to cover tools made of bone, metal, or other materials.
* Include image-based analysis (e.g., deep learning on microscope images).

---



## License

This project is licensed under the MIT License. Training data belongs to the original data owners and is not distributed with this repository.

# Random Forest Prediction Report
## Project: Classification of Propulsion Modes in Traceology
**Author**: Adrien Piette  
**Date**: 2025-05-13

---

## 1. Objective

This report presents the performance of a machine learning model trained to predict the **propulsion mode** of archaeological fractures based on traceological variables.

---

## 2. Methodology

- Model used: `RandomForestClassifier` (Scikit-learn)
- Number of trees: `n_estimators = 1000`
- Maximum depth: `max_depth = 10`
- Class weighting: `class_weight = 'balanced'`
- Pipeline includes:
   - Missing value imputation
   - Ordinal encoding of categorical variables
   - Output normalization
- Data split: `80% training / 20% testing`
- All features were used for training the model.

---

## 3. Overall Performance

- **Global Accuracy**: **75%**
- **Macro F1-score**: **72.0%**
- **Weighted Precision**: **77.4%**
- **Macro Recall**: **71.8%**

---

## 4. Performance by Class

| Class           | Precision | Recall | F1-score | Support |
|------------------|-----------|--------|----------|---------|
| **Bow**          | 0.667     | 0.500  | 0.571    | 4       |
| **Spear thrower**| 0.818     | 0.818  | 0.818    | 11      |
| **Throwing**     | 0.615     | 0.889  | 0.727    | 9       |
| **Thrusting**    | 0.889     | 0.667  | 0.762    | 12      |

---

## 5. Analysis of the "Bow" Class (Minority Class)

- Initially poorly detected
- Significant improvement via `class_weight='balanced'`
- Precision is acceptable (66.7%) but recall remains partial (50%)
- Requires monitoring with future datasets

---

## 6. Conclusion

The final Random Forest model demonstrates **good generalization** despite the imbalanced dataset.  
It provides robust predictions for frequent cases while improving detection of rarer classes.

Potential improvements include:
- Creation of new discriminative features (feature engineering)
- Testing alternative sampling approaches
- Comparison with models like XGBoost or LightGBM

---

## 7. Saved Model and Encoder

- `model_rf_final_v1.joblib`
- `label_encoder.joblib`

