import streamlit as st
import torch
from diffusers import StableDiffusionPipeline
import random

st.set_page_config(page_title="Image Generator", page_icon=".")
st.title("AI Image Generator")
@st.cache_resource
def load_model():
    pipe=StableDiffusionPipeline.from_pretrained("segmind/tiny-sd", torch_dtype=torch.float32)
    return pipe
pipe = load_model()
st.caption("Model loaded successfully")

st.session_state.setdefault("generated_image", None)
st.session_state.setdefault("generated_prompt", None)

prompt = st.text_input("Enter your prompt here", placeholder="A dog wearing sunglasses")

generate = st.button("Generate Image")

if prompt and generate:
    with st.spinner("Generator image... This might take a while."):
        image = pipe(prompt, num_inference_steps=8).images[0]
    st.session_state.generated_image = image
    st.session_state.generated_prompt = prompt
if st.session_state.generated_image is not None:
    st.image(st.session_state.generated_image, caption = st.session_state.generated_prompt)

surprise_prompt =[
    "a butterfly flying in a garden",
    "a fish jumping from water",
    "a car raceing",
    "sunset in a futuristic city"
]

if st.button("surprise me"):
    st.session_state.surprise_prompt = random.choice(surprise_prompt)

if "surprise_prompt" in st.session_state:
    st.info(f"random prompt:{st,seesion_state.surprise_promt}")