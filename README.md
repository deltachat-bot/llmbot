# LLM bot for Delta Chat

Based on [llama.cpp](https://pypi.org/project/llama-cpp-python/)
and JSON-RPC bindings for Delta Chat ([deltachat-rpc-client](https://pypi.org/project/deltachat-rpc-client/), [https://pypi.org/project/deltachat-rpc-server/](https://pypi.org/project/deltachat-rpc-server/)),
[deltabot-cli](https://pypi.org/project/deltabot-cli/)

## Installation

Run `scripts/setup.sh`.

## Run

Enter the environment with `. venv/bin/activate`.
Then run `llmbot init <address> <password>` to configure and start the bot with `llmbot serve`.
Do not run `venv/bin/llmbot` without activating the environment, activating the environment is needed to add `venv/bin/deltachat-rpc-server` to the PATH.
