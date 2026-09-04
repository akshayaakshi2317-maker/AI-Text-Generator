# 🤖 AI Text Generator

## 📌 Project Description

This project is a simple AI Text Generation web application built using Streamlit and Hugging Face Transformers.

The application takes a user's input text and generates additional text using a pretrained language model.

## ✨ Features

- ✍️ Enter a text prompt
- 🤖 Generate text using AI
- ⚙️ Adjust maximum new tokens
- 🎨 Adjust creativity level
- 🌐 Simple and user-friendly Streamlit interface
- 🤗 Uses a pretrained Hugging Face model

## 🛠️ Technologies Used

- 🐍 Python
- 🌐 Streamlit
- 🤗 Hugging Face Transformers
- 🔥 PyTorch

## 🤖 AI Model Used

**Model Name:** `EleutherAI/gpt-neo-125M`

**Task:** Text Generation

**Pipeline:** `text-generation`

**Model Parameters:** 125 Million

GPT-Neo 125M is a pretrained Transformer language model used to generate text based on the user's input prompt. It is a relatively lightweight model suitable for this Streamlit application.

### 🎯 Why This Model?

- 🔹 Low parameter count
- 🔹 Suitable for Text Generation
- 🔹 Easy to integrate with Hugging Face Transformers
- 🔹 Suitable for a lightweight Streamlit application

## 📸 Application Screenshot
<img width="1209" height="784" alt="smart ai" src="https://github.com/user-attachments/assets/af3a2682-215a-457f-83d8-395d59b1ec0b" />
<img width="1114" height="535" alt="smart ai output" src="https://github.com/user-attachments/assets/258523cb-fbc7-4bea-9ceb-d9d78b8c6c14" />

## 🔄 Project Workflow

1. 👤 User enters a text prompt.
2. 📝 The prompt is given as input to the application.
3. 🤗 Hugging Face Transformers loads the pretrained GPT-Neo 125M model.
4. ⚙️ The Text Generation pipeline processes the input.
5. 🤖 The AI model generates new text.
6. ✨ The generated text is extracted from the model output.
7. 🌐 The generated text is displayed in the Streamlit web application.

## 🔗 Workflow

```text
👤 User Input
      ↓
📝 Text Prompt
      ↓
🤗 Hugging Face Pipeline
      ↓
🤖 GPT-Neo 125M Model
      ↓
✨ Text Generation
      ↓
🌐 Streamlit Web Application
      ↓
📄 Generated Output
