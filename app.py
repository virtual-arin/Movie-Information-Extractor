import os
import streamlit as st
from dotenv import load_dotenv
from pydantic import BaseModel
from typing import List, Optional
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_mistralai import ChatMistralAI

load_dotenv()

# ---------------- API Authentication ----------------

if "api_key" not in st.session_state:
    st.session_state.api_key = None

if st.session_state.api_key is None:

    st.title("🔐 Mistral API Authentication")
    st.write("Please enter your Mistral API Key to continue.")

    api_key = st.text_input(
        "Mistral API Key",
        type="password",
        placeholder="Paste your API key here..."
    )

    if st.button("Continue"):
        if api_key.strip():
            st.session_state.api_key = api_key.strip()
            st.rerun()
        else:
            st.error("Please enter a valid API key.")

    st.stop()

# Create model only after authentication
model = ChatMistralAI(
    model="mistral-small-2603",
    api_key=st.session_state.api_key
)

# Pydantic Model
class Movie(BaseModel):
    title: str
    release_year: Optional[int] = None
    genre: List[str]
    director: Optional[str] = None
    cast: List[str]  # Fixed
    rating: Optional[float] = None
    summary: str


parser = PydanticOutputParser(pydantic_object=Movie)

# Prompt
prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
Extract movie information from the paragraph.

{format_instructions}
"""
    ),
    ("human", "{paragraph}")
])

# Create chain
chain = prompt | model | parser

# ---------------- Streamlit UI ----------------

st.set_page_config(page_title="Movie Information Extractor", page_icon="🎬")

st.title("🎬 Movie Information Extractor")

paragraph = st.text_area(
    "Enter your paragraph:",
    height=250,
    placeholder="Paste your paragraph here..."
)

if st.button("Extract Information"):
    if paragraph.strip():
        with st.spinner("Extracting information..."):
            response = chain.invoke(
                {
                    "paragraph": paragraph,
                    "format_instructions": parser.get_format_instructions(),
                }
            )

        st.markdown("## Extracted Information")

        # Display the extracted information
        st.json(response.model_dump())

    else:
        st.warning("Please enter a paragraph.")