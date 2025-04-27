# Mini-Rag-App

## Requirements

- Python 3.12 or later
- MiniConda (for environment management)

## Setup Instructions

### 1. Install MiniConda
Download and install MiniConda from the [official website](https://docs.conda.io/en/latest/miniconda.html).

### 2. Create a New Environment
```bash
conda create -n mini-rag python=3.12 
```

### 3. Activate the invironment

```bash
conda activate mini-rag 
```
## (Optional) Setup you command line interface for better readability

```bash 
export PS1="\[\033[01;32m\]\u@\h:\w\n\[\033[00m\]\$ "
```
## Installation
### Install the required packages
```bash 
$ pip install -r requirements.txt
```
### Setup the environment variables
``` bash
$ cp .env.example .env
```
Set your environment variables in the .env file. Like OPENAI_API_KEY value.

## Run Docker Compose Services
```bash
$ cd docker
$ cp .env.example .env
```
- update .env with your credentials
```bash
$ cd docker
$ sudo docker compose up -d
```
## Run the FastAPI server
```bash
$ uvicorn main:app --reload --host 0.0.0.0 --port 5000
```

