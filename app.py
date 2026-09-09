import streamlit as st
from transformers import pipeline

st.set_page_config(
    page_title="AI Text Generator",
    page_icon="🤖"
)

st.title("🤖 AI Text Generator")
st.write("✨ Enter a sentence and let AI complete it!")

@st.cache_resource
def load_model():
    return pipeline(
        "text-generation",
        model="EleutherAI/gpt-neo-125M"
    )

generator = load_model()

prompt = st.text_area(
    "✍️ Enter your text:",
    placeholder="Artificial Intelligence is..."
)

# Maximum New Tokens
max_tokens = st.slider(
    "📝 Maximum new tokens",
    min_value=10,
    max_value=100,
    value=40,
    step=5
)

# Creativity
temperature = st.slider(
    "🎨 Creativity",
    min_value=0.1,
    max_value=1.5,
    value=0.7,
    step=0.1,
    format="%.1f"
)

if st.button("✨ Generate Text"):

    if prompt.strip():

        with st.spinner("🤖 Generating..."):

            result = generator(
                prompt,
                max_new_tokens=max_tokens,
                num_return_sequences=1,
                do_sample=True,
                temperature=temperature,
                top_p=0.9
            )

        generated_text = result[0]["generated_text"]

        # Remove the original prompt
        new_text = generated_text[len(prompt):].strip()

        st.subheader("📝 Generated Text")

        if new_text:
            st.write(new_text)
        else:
            st.warning("No additional text was generated.")

    else:
        st.warning("⚠️ Please enter some text first!")