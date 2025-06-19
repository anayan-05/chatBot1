# chatBot1
# Local CLI Chatbot using Hugging Face (flan-t5-large)

A fully offline, command-line chatbot built using Hugging Face's `flan-t5-large` model. This bot can answer factual questions (e.g., "What is the capital of France?") using local inference — no internet or APIs required after model download. It runs entirely on CPU, with a simple and clean interface designed for multi-turn conversations.

---

## Features

- Uses `google/flan-t5-large` (instruction-tuned LLM)
- CLI-based interaction with user input loop
- Greedy decoding for stable, factual answers
- Modular codebase (`interface.py`)
- Runs entirely locally on CPU

---

## Setup Instructions:

### 1. System Requirements (if any)

Example: Python 3.8 or higher

Optional: works on CPU, no GPU required

### 2. Installing Dependencies: These are the dependencies that are needed to be installed
pip install transformers torch

### 3. Cloning the Repository or Unzipping the Folder: the code is on github
git clone https://github.com/anayan-05/chatBot1

## How to run:


In the terminal, navigate to the project folder and run:
python interface.py
## Sample Interaction:


Chatbot ready (flan-t5-large). Type /exit to quit.
User: What is the capital of France?
Bot: Paris

User: Who is Elon Musk?
Bot: Elon Musk is the CEO of Tesla and SpaceX.

User: What is the capital of Italy?
Bot: Rome
