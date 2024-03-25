# AI Blog Creator

AI Blog Creator is a Streamlit application that leverages the Google Generative AI model to generate blog content based on user-provided input. With this tool, users can easily create engaging and informative blog posts without extensive writing skills or domain expertise.

## Features
- **Generative AI Model**: Utilizes the Google Generative AI model to generate blog content.
- **Customizable Input**: Allows users to input blog title, keywords, and desired word count.
- **Content Generation**: Generates blog posts based on user-provided input, incorporating specified keywords.
- **Streamlit Interface**: Provides an intuitive interface powered by Streamlit for easy interaction.

## Installation
1. Clone the repository to your local machine.
2. Install the required dependencies by running:
    ```bash
    pip install -r requirements.txt
    ```
3. Obtain the Gemini API key and update `api_key.py` with your key.
4. Run the application using:
    ```bash
    streamlit run app.py
    ```
## Configuration
- The generation configuration and safety settings for the Generative AI model are defined in `app.py`.
- Ensure the `api_key.py` file contains your Gemini API key for authentication.

## Usage
1. Launch the application by running `streamlit run app.py`.
2. Input your blog details in the sidebar, including the blog title, keywords, and desired word count.
3. Click the "Generate a Blog" button to generate the blog post.
4. View the generated blog post on the main page.

## Acknowledgments
- Special thanks to Google for providing access to the Generative AI model.
- Inspired by the need for easily accessible content creation tools using AI technology.


