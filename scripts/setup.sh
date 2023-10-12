#!/bin/sh
set -e
set -x
wget https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.1-GGUF/resolve/main/mistral-7b-instruct-v0.1.Q4_K_M.gguf
test -d llama-cpp-python || git clone https://github.com/abetlen/llama-cpp-python
python -m venv venv
. venv/bin/activate
cd llama-cpp-python
git submodule init
git submodule update
pip install .
cd ..
pip install .
