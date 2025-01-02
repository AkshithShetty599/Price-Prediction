# Project Title: Data Analysis with Linear Regression

## Overview
This project involves performing a data analysis using Python and linear regression techniques. The analysis is performed using a dataset loaded from a CSV file. The project workflow includes handling missing data, data encoding, model training, and performance evaluation. The aim is to build a predictive model using linear regression and evaluate its performance using metrics such as R² score and Mean Absolute Error (MAE).

## Project Structure
The project is structured as a Jupyter Notebook (`Analysis.ipynb`), which contains code for loading, preprocessing, and analyzing the dataset. The notebook is accompanied by explanations for each step, making it easy to follow the analysis process.

## Key Steps in the Analysis
1. **Loading the Dataset:** The dataset is loaded using the Pandas library.
2. **Data Preprocessing:** This step involves checking for missing values and encoding categorical variables into numerical form using one-hot encoding.
3. **Train-Test Split:** The dataset is split into training and testing sets for model evaluation.
4. **Model Training:** A linear regression model is trained on the training dataset.
5. **Model Evaluation:** The model is evaluated using R² score and MAE on both training and validation sets.
6. **Feature Importance:** The significance of features is assessed by analyzing the model's coefficients.
7. **Residual Analysis:** Residuals are plotted to check for patterns, indicating the model's appropriateness.
8. **Final Model Performance:** The model's performance is assessed on the test dataset.

## How to Use
1. Clone this repository to your local machine:
   ```bash
   git clone <repository-url>
   ```
2. Install the necessary dependencies listed in the `requirements.txt` file:
   ```bash
   pip install -r requirements.txt
   ```
3. Open the Jupyter Notebook (`Analysis.ipynb`) and run the cells in sequence. Detailed explanations are provided after each cell to help understand the analysis.

## Results
The linear regression model built in this project provides an R² score of 0.784 on the test set, indicating a good fit. The model's MAE is 436.5, showing decent predictive accuracy.

## Conclusion
This project demonstrates the use of linear regression for predictive modeling, with a focus on data preprocessing, feature selection, and model evaluation. It highlights the importance of checking model assumptions and assessing feature importance for a successful analysis.

