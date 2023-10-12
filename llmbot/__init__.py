"""Conversational bot for Delta Chat based on local LLM."""
from llama_cpp import Llama
from deltabot_cli import BotCli, events

cli = BotCli("llmbot", log_level="INFO")
llm = Llama(model_path="mistral-7b-instruct-v0.1.Q4_K_M.gguf")

@cli.on(events.NewMessage(is_info=False))
def reply(event):
    msg = event.message_snapshot

    question = msg.text
    prompt = f"Q: {question}\n\nA:"
    prompt_len = len(llm.tokenize(b" " + prompt.encode("utf-8")))
    max_tokens = 512
    if prompt_len >= max_tokens:
        msg.chat.send_text("TL;DR")
        return
    result = llm(prompt, max_tokens=max_tokens - prompt_len, stop=["Q:"])
    answer = result['choices'][0]['text']
    msg.chat.send_text(answer)


def main() -> None:
    """Run the application."""
    cli.start()
