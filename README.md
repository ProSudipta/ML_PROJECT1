# Real Estate Price Prediction Using Machine Learning

Welcome to the "Real Estate Price Prediction Using Machine Learning" project repository. This project demonstrates a machine learning-based web application for predicting real estate property prices. It utilizes a trained machine learning model to make predictions based on various features.

## Table of Contents
- [About](#about)
- [Features](#features)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [License](#license)
- [Visualizations](#visualizations)

## About
This project showcases the application of machine learning in predicting real estate property prices. It utilizes a Random Forest Regressor model to estimate property prices based on features such as crime rate, zoning information, nitric oxide concentration, and more.

## Features
- Web application interface for inputting property features and obtaining price predictions.
- Proper data preprocessing, including handling missing values.
- Model training using machine learning algorithms.
- Evaluation of model performance with Root Mean Square Error (RMSE).
- Saving the trained model for future use.

## Getting Started
To run the project locally, follow these steps:

1. Clone this repository to your local machine.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Run the Flask web application using `python app.py`.
4. Access the web interface by navigating to `http://localhost:5000` in your web browser.

## Usage
1. Access the web interface by opening the provided link.
2. Input various property features into the respective fields.
3. Click the "Predict" button to see the estimated property price.

## Technologies Used
- Python
- Flask (Web Framework)
- HTML/CSS (Frontend)
- Pandas and NumPy (Data Processing)
- Scikit-Learn (Machine Learning)
- Matplotlib (Data Visualization)
- Joblib (For model saving)
- GitHub (Version Control)

## Project Structure
The project's directory structure is as follows:

- `app.py`: Main Flask application file.
- `random_forest_model.joblib`: Trained machine learning model.
- `templates/`: Directory containing HTML templates.
  - `index.html`: Webpage for input and prediction display.
- `static/`: Directory containing CSS styles.
  - `styles.css`: Styles for formatting the webpage.
- `README.md`: Project documentation.



## Visualizations
![image](https://github.com/ProSudipta/ML_PROJECT1/assets/105074592/d4b91f1b-5f99-4d79-b9ef-8bca532d8498)


The scatter matrix visualizes the pairwise relationships between important attributes, helping to understand data patterns and trends.

![image](https://github.com/ProSudipta/ML_PROJECT1/assets/105074592/e6d5fc40-d524-4bda-9059-d2cc55aaab88)


This scatter plot illustrates the relationship between the average number of rooms per dwelling (RM) and the median property value (MEDV).

*Note: The visualizations are available in the `visualization/` directory.*

