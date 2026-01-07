import streamlit as st
import pickle

# Page configuration
st.set_page_config(
    page_title="Spam Message Classifier",
    page_icon="📩",
    layout="centered"
)

# Load trained model
@st.cache_resource
def load_model():
    with open("spam.pkl", "rb") as file:   # ✅ changed here
        model = pickle.load(file)
    return model

model = load_model()

# App Title
st.title("📩 Spam Message Classifier")
st.subheader("Detect whether a message is **Spam** or **Not Spam**")

st.write("Enter an SMS or text message below:")

# Text input
message = st.text_area(
    "✍️ Message Text",
    height=150,
    placeholder="Congratulations! You have won a free prize..."
)

# Predict button
if st.button("🔍 Check Message"):
    if message.strip() == "":
        st.warning("Please enter a message to classify.")
    else:
        prediction = model.predict([message])[0]

        # Handle labels safely
        if prediction == 1 or prediction == "spam":
            st.error("🚨 This message is **SPAM**")
        else:
            st.success("✅ This message is **NOT SPAM**")

# Footer
st.markdown("---")
st.markdown("Developed by **Sahil Bagri** 🚀")
