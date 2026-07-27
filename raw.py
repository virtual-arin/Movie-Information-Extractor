import os
from dotenv import load_dotenv
from pydantic import BaseModel
from typing import List, Optional

from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_mistralai import ChatMistralAI

load_dotenv()

# Create model
model = ChatMistralAI(
    model="mistral-small-2603",
)

# Pydantic Model

class Movie(BaseModel):
    title: str
    release_year: Optional[int] = None
    genre: List[str]
    director: Optional[str] = None
    cast: List[str]
    rating: Optional[float] = None
    summary: str

# Output parser
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

paragraph = input("Enter a movie paragraph:\n")

response = chain.invoke(
    {
        "paragraph": paragraph,
        "format_instructions": parser.get_format_instructions(),
    }
)

print("\nExtracted Information:\n")
print(response.model_dump())