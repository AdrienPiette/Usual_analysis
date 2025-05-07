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
