import streamlit as st
from api_key import GEMINI_API_KEY
import google.generativeai as genai

# Configure the API with Gemini Flash 1.5
genai.configure(api_key=GEMINI_API_KEY)

# Set up the model with Gemini Flash 1.5
generation_config = {
    "temperature": 0.9,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048,
}

safety_settings = {
    "harassment": "BLOCK_MEDIUM_AND_ABOVE",
    "hate_speech": "BLOCK_MEDIUM_AND_ABOVE",
    "sexually_explicit": "BLOCK_MEDIUM_AND_ABOVE",
    "dangerous_content": "BLOCK_MEDIUM_AND_ABOVE",
}

# Initialize the model for Gemini Flash 1.5
model = genai.GenerativeModel(model_name="gemini-flash-1.5",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

st.set_page_config(layout="wide")
st.title('AI Blog Creator')
st.subheader('An easier way to create content')

# Default blog content
blog = "Hi! I am a Blog of code"

with st.sidebar:
    st.title('Input your Blog Details')
    st.subheader('Enter details of the Blog you like to generate')

    blog_title = st.text_input("Blog Title")
    keywords = st.text_area("Keywords (comma-separated)")
    num_words = st.slider("Number of words", min_value=100, max_value=1000, step=100)

    submit_button = st.button("Generate a Blog")

# Prepare prompt
prompt = (
    f"Write a comprehensive, engaging blog post relevant to the given title \"{blog_title}\" "
    f"and keywords \"{keywords}\". Make sure you incorporate these keywords. The blog should be approximately "
    f"{num_words} words in English, suitable for an online audience. Ensure the content is original, informative, "
    "and maintains a consistent tone throughout.\n"
)

if submit_button:
    # Generate the content using the updated method for Gemini Flash 1.5
    response = model.generate(prompt=prompt)
    st.title("Your Blog Post:")
    st.write(response.text)
