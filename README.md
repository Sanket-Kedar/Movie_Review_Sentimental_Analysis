<h1>Movie Review Sentiment Analysis</h1>

<h2>Overview</h2>

This project performs sentiment analysis on IMDB movie reviews using Deep Learning. It classifies reviews as either positive or negative using an LSTM-based neural network. The project also includes a Streamlit web application that allows users to input their own reviews and get real-time sentiment classification.

<h2>Dataset</h2>

The dataset used is the IMDB Dataset of 50K Movie Reviews from Kaggle, which contains:

Link : https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews

50,000 movie reviews labeled as positive or negative.

Balanced dataset (25,000 positive & 25,000 negative reviews).

Preprocessed by tokenization and padding to maintain uniform input size.

<h2>Installation & Setup</h2>

## How to Run the Application

To run the movie_review sentiment analyzer:

1. Clone this repository to your local machine and ``cd`` into the project directory.
    ``` bash
    git@github.com:Sanket-Kedar/Movie_Review_Sentimental_Analysis
    ```
2. Set up a Python environment with necessary dependencies listed in `requirements.txt`.
    ``` bash
    pip install -r requirements.txt
    ```
3. Run the application using Streamlit:
    ```bash
    streamlit run main.py
    ```
4. Enter review and check the sentiment along with prediction score.

## Reults:
<img width="745" alt="image" src="https://github.com/user-attachments/assets/cb330196-ad7e-4bcc-b740-7d05a82ffff7" />

<img width="713" alt="image" src="https://github.com/user-attachments/assets/d5602b6e-7026-4ee3-bd00-9cbb37273dc2" />


