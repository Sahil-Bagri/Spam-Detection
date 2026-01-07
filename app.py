import streamlit as st
import pickle

# Page config
st.set_page_config(
    page_title="Spam Or Not Spam Emails",
    page_icon🗑️",
    layout="centered"
)

# Load model
@st.cache_resource
def load_model():
    with open("model.pkl", "rb") as f:
        model = pickle.load(f)
    return model

model = load_model()

# App title
st.title("🗑️ Spam Or Not Spam Emails")
st.write("Enter text or headline to classify it as **spam** or **ham**.")

# Text input
user_input = st.text_area(
    "✍️ Enter Email Text Here:",
    height=200,
    placeholder="Type or paste news email..."
)

# Prediction
if st.button("🔍 Predict"):
    if user_input.strip() == "":
        st.warning("Please enter some text!")
    else:
        prediction = model.predict([user_input])[0]

        if prediction == 1 or prediction == "REAL":
            st.success("✅ This news looks **ham**")
        else:
            st.error("🚨 This news looks **spam**")

# Footer
st.markdown("---")
st.markdown("Developed by **Sahil Bagri** 🚀")
