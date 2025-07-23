# 🔰 Getting Started with Google Gemini AI on Google Colab

Welcome students! This guide will walk you through how to set up and use **Google Colab** to work with **Gemini AI (Google Generative AI)** for:

- 🧠 Text-based chat
- 🖼️ Image analysis
- 📄 PDF document analysis

---

## ✅ Step 1: Open Google Colab

1. Go to [Google Colab](https://colab.research.google.com/)
2. Click **"New Notebook"**.
3. In the top-left corner, click **"Connect"** to connect to the runtime server.
4. You're now ready to paste and run the code!

---

## 🧠 TEXT-BASED AI CHAT (Just like ChatGPT)

Paste the following code into a Colab cell and run it:

```python
from google import genai
from google.genai import types

# Replace with your own API key if needed
client = genai.Client(api_key="AIzaSyCjMsYC-mDTwOr1at1-91EkMwI2O6eOvXg")

response = client.models.generate_content(
    model="gemini-2.5-flash",
    config=types.GenerateContentConfig(
        system_instruction="You are a cat. Your name is Neko."),
    contents="Hello there"
)

print(response.text)
````

📌 **Explanation:**

* The model is instructed to reply like a cat named **Neko**.
* `gemini-2.5-flash` is a lightweight but fast model.

---

## 🖼️ IMAGE ANALYSIS WITH AI

1. Upload an image named `1.png` to Colab (left sidebar > Files > Upload).
2. Then paste and run the following code:

```python
from PIL import Image
from google import genai

client = genai.Client(api_key="AIzaSyCjMsYC-mDTwOr1at1-91EkMwI2O6eOvXg")

image = Image.open("1.png")
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=[image, "what you think in thiss image"]
)

print(response.text)
```

📌 **Explanation:**

* The model "sees" the image and responds to your prompt about it.

---

## 📄 PDF DOCUMENT ANALYSIS

1. Upload your PDF file (e.g., `RC car 1.pdf`) to Colab.
2. Then paste and run the code below:

```python
from google import genai
from google.genai import types
import pathlib

client = genai.Client(api_key="AIzaSyCjMsYC-mDTwOr1at1-91EkMwI2O6eOvXg")

filepath = pathlib.Path('/content/RC car 1.pdf')

prompt = "Tell me each slide info"
response = client.models.generate_content(
  model="gemini-2.5-flash",
  contents=[
      types.Part.from_bytes(
        data=filepath.read_bytes(),
        mime_type='application/pdf',
      ),
      prompt
  ]
)

print(response.text)
```

📌 **Explanation:**

* This will analyze the PDF and extract content slide-by-slide based on your prompt.

---

## 🔐 API Key Note

This project uses an **API key**. Make sure to:

* Keep it private.
* Replace it with your own if you're hitting quota or rate limits.

You can get an API key from the [Google AI Studio](https://aistudio.google.com/app/apikey) if needed.

---

## 🎉 You're All Set!

Use this Colab setup for your experiments with Gemini AI.

* Try different prompts 🧪
* Upload your own images and PDFs 📂
* Get creative with use cases ✨

---


