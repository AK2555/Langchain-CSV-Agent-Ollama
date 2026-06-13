# CSV Question Answering App using LangChain + Ollama

A Streamlit application that allows users to upload a CSV file and ask natural language questions about the data using a local Ollama LLM.

## Features

* Upload any CSV file
* Preview uploaded data
* Ask questions in natural language
* Runs completely locally
* Uses Ollama and LangChain
* No OpenAI API key required

---

## Prerequisites

### Install Python

Python 3.10+ recommended.

Check version:

```bash
python --version
```

---

## Install Ollama

Download and install Ollama:

https://ollama.com/download

Verify installation:

```bash
ollama --version
```

---

## Download LLM Model

Pull the model:

```bash
ollama pull llama3.2
```

Verify:

```bash
ollama list
```

Expected output:

```text
llama3.2
```

---

## Clone Repository

```bash
git clone <YOUR_REPO_URL>
cd langChain-csv-tutorial
```

---

## Create Virtual Environment

Mac/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Start Ollama

```bash
ollama serve
```

If you see:

```text
address already in use
```

Ollama is already running.

---

## Run Streamlit Application

```bash
streamlit run main.py
```

Open:

```text
http://localhost:8501
```

---

## Example Questions

* How many rows are present?
* Show top 5 records.
* What is the average salary?
* Which product generated maximum revenue?
* What are the unique values in a column?

---

## Tech Stack

* Python
* Streamlit
* Pandas
* LangChain
* Ollama
* Llama 3.2

---

## Notes

* No OpenAI API key required.
* Data never leaves your machine.
* All inference runs locally through Ollama.
