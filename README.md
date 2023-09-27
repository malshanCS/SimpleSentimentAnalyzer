# Sentiment Analysis with Streamlit

This repository contains a simple Sentiment Analysis project using Python. In this project, we perform sentiment analysis on a dataset of movie reviews to determine whether the reviews are positive or negative. We use Natural Language Processing (NLP) techniques and machine learning models to accomplish this task.

## Workflow

Here is the high-level workflow of the project:

1. **Install Packages**: We start by installing the necessary Python packages for this project.

2. **Data Cleaning**: We load a dataset of movie reviews and perform initial data cleaning.

3. **Text Preprocessing**: We preprocess the text data by applying various techniques, including text normalization, removing HTML tags, converting to lowercase, and removing stopwords.

4. **Exploratory Data Analysis (EDA)**: We explore the dataset, calculate word counts, character counts, average word lengths, and visualize these statistics.

5. **Model Building**: We split the dataset into training and testing sets, vectorize the text data using TF-IDF (Term Frequency-Inverse Document Frequency), and build a sentiment classification model using a machine learning classifier.

6. **Model Evaluation**: We evaluate the model's performance using metrics like accuracy, precision, recall, F1-score, and visualize the confusion matrix.

7. **Streamlit Web App**: We create a simple Streamlit web application that allows users to input their own text and get sentiment predictions from the trained model.

## Usage

To run the Streamlit web app, follow these steps:

1. Install the required packages by running the following command:

   ```
   pip install -r requirements.txt
   ```

2. Run the Streamlit app using the following command:

   ```
   streamlit run app.py
   ```

3. Open your web browser and access the app at the provided URL (usually http://localhost:8501).

## Models

Two models are included in this project:

1. **Linear Support Vector Classifier (LinearSVC)**: Achieves high accuracy in sentiment classification.

2. **Random Forest Classifier**: Another model for sentiment classification.

## Data Source

The dataset used in this project is the IMDB movie reviews dataset, which is publicly available.

## Note

Please note that this project is for educational purposes and may not represent a production-ready sentiment analysis system. You can further enhance the model and the web app to suit your specific needs.

Feel free to explore the code and adapt it for your own projects or datasets. Enjoy experimenting with sentiment analysis!
