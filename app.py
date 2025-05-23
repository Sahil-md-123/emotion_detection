import streamlit as st
import joblib
import re
import string

# Same preprocessing function you used before
def clean_text(text):
    text = text.lower()
    text = re.sub(r'\d+', '', text)
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = re.sub(r'\s+', ' ', text).strip()
    return text

# Streamlit app
st.title("Emotion Detection from Text")

user_input = st.text_area("Enter your sentence here:")

if st.button("Predict Emotion"):
    if user_input.strip() == "":
        st.warning("Please enter some text to predict.")
    else:
        cleaned_input = clean_text(user_input)
        prediction = pipeline.predict([cleaned_input])[0]
        st.success(f"Predicted Emotion: {prediction}")

