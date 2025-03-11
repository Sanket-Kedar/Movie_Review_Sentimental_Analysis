from keras.models import load_model
import joblib
from tensorflow.keras.preprocessing.sequence import pad_sequences

model = load_model("lstm_model.h5")
tokenizer = joblib.load("tokenizer.pkl")

def predict_sentiment(review):
  sequences = tokenizer.texts_to_sequences([review])
  padded_sequence = pad_sequences(sequences, maxlen=200)
  prediction = model.predict(padded_sequence)
  sentiment = "positive" if prediction[0][0] > 0.5 else "negative"
  return sentiment, prediction[0][0]
     
import streamlit as st

st.title('IMDB Movie Review Sentiment Analysis')
st.write('Enter a movie review to classify it as positive or negative')

user_input = st.text_area("Movie Review")

if st.button('Classify'):

    sentiment, score = predict_sentiment(user_input)  

    st.write('Sentiment:', sentiment)
    st.write('Prediction Score:', score)

else:
   print('Enter a movie review')

