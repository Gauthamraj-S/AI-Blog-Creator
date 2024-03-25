import streamlit as st
from api_key import GEMINI_API_KEY
import google.generativeai as genai
genai.configure(api_key=GEMINI_API_KEY)

# Set up the model
generation_config = {
  "temperature": 0.9,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 2048,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)


st.set_page_config(layout="wide")
st.title('AI Blog creator')
st.subheader('An easier way to create contents')
blog="Hi! I am a Blog of code"
with st.sidebar:
    st.title('Input your Blog Details')
    st.subheader('Enter details of the Blog you like to generate')

    blog_title=st.text_input("Blog  Title")

    keywords = st.text_area("Keywords (comma-separated)")

    num_words = st.slider("Number of words", min_value=100, max_value=1000, step = 100)

    
    submit_button = st.button("Generate a Blog")
    prompt_parts = [
        f"Write a comprehensive, engaging blog post relevant to the given \{blog_title}\" and keywords \"{keywords}\". Make sure you incorporate these keywords.Blog should be approximately {num_words} in words in english suitable for an online audience. Ensure the content is original, informative, and maintains a consistent tone throughout.\n",
    ]

if submit_button:
    response = model.generate_content(prompt_parts)
    st.title("Your Blog Post: ")
    st.write(response.text)