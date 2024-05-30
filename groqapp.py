import os
import streamlit as st

from gtts import gTTS
from groq import Groq

# Set your Groq API key
api_key = "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"
os.environ["GROQ_API_KEY"] = api_key

# Initialize the Groq client with the API key
client = Groq(api_key=api_key)

# Streamlit app
st.title("AI TUTOR")

# Text input for the topic
topic = st.text_input("Please enter the topic you want to know about:")

if st.button("Generate Explanation"):
    if topic:
        # Create a chat completion request with the user-provided topic
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": f"Explain the importance of {topic} and give a real world example",
                }
            ],
            model="llama3-8b-8192",
        )

        # Get the response from the model
        result = chat_completion.choices[0].message.content
        st.write("Generated Explanation:")
        st.write(result)

        # Convert the response to speech using gTTS
        tts = gTTS(text=result, lang='en', slow=False)
        audio_file = "explanation.mp3"
        tts.save(audio_file)

        # Play the audio file in Streamlit
        audio_bytes = open(audio_file, "rb").read()
        st.audio(audio_bytes, format='audio/mp3')

        # Provide a download link for the audio file
        st.download_button(label="Download Audio", data=audio_bytes, file_name=audio_file, mime='audio/mp3')
    else:
        st.warning("Please enter a topic to generate an explanation.")
