import streamlit as st
from transformers import pipeline

# ⚙️ Page Configuration
st.set_page_config(
    page_title="Smart AI Writer",
    page_icon="🧠",
    layout="centered"
)

# 🏠 Application Title
st.title("🧠 Smart AI Writer")
st.caption("✨ Generate creative text using a pretrained AI model")

# 🤖 Load AI Model
@st.cache_resource
def get_text_generator():
    return pipeline(
        task="text-generation",
        model="openai-community/gpt2"
    )

generator = get_text_generator()

# ✍️ User Input
st.subheader("✍️ Enter Your Idea")

user_text = st.text_area(
    "💬 Type something to begin:",
    placeholder="🌟 Once upon a time..."
)

# 🎛️ Generation Settings
st.subheader("⚙️ Generation Settings")

max_tokens = st.slider(
    "📝 Maximum new tokens",
    min_value=20,
    max_value=60,
    value=40
)

creativity = st.slider(
    "🎨 Creativity",
    min_value=0.5,
    max_value=1.0,
    value=0.7
)

# 🚀 Generate Button
if st.button("🚀 Generate", use_container_width=True):

    if user_text.strip():

        with st.spinner("🤖 AI is creating your text..."):

            output = generator(
                user_text,
                max_new_tokens=max_tokens,
                temperature=creativity,
                do_sample=True,
                num_return_sequences=1
            )

        # 📄 Get Generated Result
        full_text = output[0]["generated_text"]

        # ✂️ Remove Original Input
        generated_part = full_text[len(user_text):].strip()

        st.success("✨ Text generated successfully!")

        st.subheader("📖 AI Generated Text")

        if generated_part:
            st.write(generated_part)
        else:
            st.write(full_text)

    else:
        st.warning("⚠️ Please enter some text before generating!")

# ℹ️ Model Information
with st.expander("🤖 Model Information"):
    st.write("**Model:** openai-community/gpt2")
    st.write("**Task:** Text Generation")
    st.write("**Library:** Hugging Face Transformers")
    st.write("**Framework:** Streamlit")