# Text-Summarization-Tool

*COMPANY: CODTECH IT SOLUTIONS

*NAME: MOHAMMAD IZHAN RA

INTERN ID: CT04DH406

DOMAIN: AI

*DURATION: 4 WEEEKS

MENTOR: NEELA SANTOSH

DESCRIPTION OF TASK

This task involves building a simple Natural Language Processing (NLP) tool that can automatically summarize long articles or paragraphs into short, concise summaries using deep learning.

The project uses the Hugging Face Transformers library, specifically the pre-trained DistilBART model (sshleifer/distilbart-cnn-12-6), which is fine-tuned for summarization tasks. The goal is to reduce the length of input text while preserving its core meaning.

🔧 Technologies Used
Python – for backend programming

Flask – for building a lightweight web interface

HTML/CSS – for creating the user input form and display

Hugging Face Transformers – for using pre-trained summarization models

🛠 Features
Users can enter or paste long text in a textbox on the webpage.

On clicking the "Summarize" button, the input is sent to the Flask backend.

The backend processes the text using the summarization model and returns a concise summary.

The summary is displayed on the same page dynamically.

⚙️ How It Works
The user opens the web app and enters/pastes a lengthy article.

Flask receives the input and passes it to the pre-trained summarization model.

The model returns a short summary (40–150 words) that captures the main points.

Flask renders the summary along with the original text on the HTML page.
