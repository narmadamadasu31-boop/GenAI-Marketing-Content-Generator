import streamlit as st
import os
from dotenv import load_dotenv
from groq import Groq

# Load API key from .env
load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Page settings
st.set_page_config(page_title="GenAI Marketing Generator", page_icon="🚀")

st.title("🚀 GenAI Marketing Content Generator (FREE AI)")
st.write("Generate ads, captions and marketing text using AI")

# Inputs
topic = st.text_input("Enter product / topic")
tone = st.selectbox("Select tone", ["Professional", "Casual", "Funny", "Luxury"])
length = st.selectbox("Select length", ["Short", "Medium", "Long"])

# Generate button
if st.button("Generate Content"):
    if topic == "":
        st.warning("Please enter a topic")
    else:
        try:
            prompt = f"""
            Write a {length.lower()} marketing content about "{topic}"
            in a {tone.lower()} tone.

            Include:
            • Catchy headline
            • Marketing paragraph
            • Instagram caption
            • 5 hashtags
            """

            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {"role": "system", "content": "You are a marketing expert."},
                    {"role": "user", "content": prompt}
                ]
            )

            output = response.choices[0].message.content

            st.success("✅ Content generated!")
            st.write(output)

            # Download button (for viva demo 😎)
            st.download_button(
                label="📥 Download Content",
                data=output,
                file_name="marketing_content.txt",
                mime="text/plain"
            )

        except Exception as e:
            st.error(f"Error: {e}")