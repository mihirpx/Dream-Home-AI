import torch
from diffusers import StableDiffusionPipeline
import os
import streamlit as st

@st.cache_resource  # Cache to avoid reloading model every time
def load_model():
    model_path = os.path.join("models", "stable-diffusion-v1-4")
    pipe = StableDiffusionPipeline.from_pretrained(
        model_path,
        torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32
    )
    pipe = pipe.to("cuda" if torch.cuda.is_available() else "cpu")
    return pipe
