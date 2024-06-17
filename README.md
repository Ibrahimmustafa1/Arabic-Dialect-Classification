# Dialect Identification Project

This project demonstrates the process of dialect identification using natural language processing techniques. It consists of several Python scripts for data handling, preprocessing, model training, and prediction.
## DEMO : <a href='https://renderapp-nlp.onrender.com/'>Click</a>
## Scripts Overview

### 1. Data Fetching Script (`data_fetching.py`)

This script connects to a SQLite database (`dialects_database.db`), retrieves data from multiple tables, and merges them into a single DataFrame for further processing.

### 2. Data Preprocessing Script (`data_preprocessing.py`)

This script contains functions to clean and preprocess text data, including removing emojis, converting text to lowercase, removing numbers and extra whitespace, and applying Arabic stopwords removal.

### 3. Model Training Script (`model_training.py`)

This script involves the training of a machine learning model (Logistic Regression in this example). It includes functions for text vectorization using TF-IDF, label encoding, model training, and saving trained models (`model.pkl`, `tfidf.pkl`, `label_encoder.pkl`).

### 4. Main Execution Script (`main.py`)

This script integrates the above functionalities in a sequential manner:
- Fetches data using `fetch_data` from `data_fetching.py`.
- Preprocesses the data using `preprocess_dataframe` from `data_preprocessing.py`.
- Trains a model using `train_model` from `model_training.py`.
- Loads the trained model and necessary transformers using `load_model` from `model_training.py`.
- Makes predictions using `predict` from `model_training.py` based on sample input.

## Usage

To run the project:
1. Ensure `dialects_database.db` is accessible and contains relevant data.
2. Install necessary dependencies: pandas, nltk, scikit-learn, tensorflow, etc.
3. Execute `main.py`:
   ```bash
   python main.py
