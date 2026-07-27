# 🎬 Movie Information Extractor

A Streamlit application that uses **Mistral AI**, **LangChain**, and **Pydantic** to extract structured movie information from unstructured text.

## 📌 Problem Statement

Movie details are often written as long paragraphs, making it difficult to extract key information like the title, genre, director, cast, rating, and summary manually.

## 💡 Solution

This application uses **Mistral AI** with **LangChain's Pydantic Output Parser** to automatically convert movie descriptions into structured JSON, making the data easy to read, validate, and integrate into other applications.

## ✨ Features

- 🤖 AI-powered movie information extraction
- 📄 Converts unstructured text into structured JSON
- ✅ Pydantic schema validation
- 🔐 Secure Mistral API authentication
- 🎯 Simple Streamlit interface

## 📊 Extracted Information

- Movie Title
- Release Year
- Genre
- Director
- Cast
- Rating
- Summary

## 🛠️ Tech Stack

- Python
- Streamlit
- LangChain
- Mistral AI
- Pydantic
- python-dotenv

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/virtual-arin/movie-information-extractor.git
cd movie-information-extractor
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

## ▶️ Usage

1. Launch the application.
2. Enter your **Mistral API Key**.
3. Paste a movie description.
4. Click **Extract Information**.
5. View the structured JSON output.

## 📁 Project Structure

```
movie-information-extractor/
│── app.py              # Streamlit application
│── raw.py              # CLI version
│── requirements.txt    # Dependencies
│── .gitignore
│── LICENSE
└── README.md
```

## 📦 Requirements

Install all required packages:

```bash
pip install -r requirements.txt
```

## 📄 License

This project is licensed under the **MIT License**.

## 🙌 Acknowledgements

- LangChain
- Mistral AI
- Streamlit
- Pydantic