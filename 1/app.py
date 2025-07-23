from flask import Flask, request, render_template
from transformers import pipeline

app = Flask(__name__)

# Load the Hugging Face summarization pipeline
summarizer = pipeline("summarization")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/summarize", methods=["POST"])
def summarize_text():
    input_text = request.form["article"]

    # Hugging Face summarization
    summary = summarizer(input_text, max_length=150, min_length=40, do_sample=False)

    return render_template("index.html", original=input_text, summary=summary[0]['summary_text'])

if __name__ == "__main__":
    app.run(debug=True)
