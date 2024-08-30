from typing import Any, Dict, List

from langchain.callbacks.base import BaseCallbackHandler
from langchain.schema import LLMResult


# Creating the custom callback handler class
class ChatbotHandler(BaseCallbackHandler):
    def __init__(self, queue) -> None:
        super().__init__()
        # we will be providing the streamer queue as an input
        self._queue = queue
        # defining the stop signal that needs to be added to the queue in
        # case of the last token
        self._stop_signal = None
        print("Custom handler Initialized")

        # On the arrival of the new token, we are adding the new token in the

    # queue
    def on_llm_new_token(self, token: str, **kwargs) -> None:
        self._queue.put(token)

        # on the start or initialization, we just print or log a starting message

    def on_llm_start(self, serialized: Dict[str, Any], prompts: List[str], **kwargs: Any) -> None:
        """Run when LLM starts running."""
        print("generation started")

        # On receiving the last token, we add the stop signal, which determines

    # the end of the generation
    def on_llm_end(self, response: LLMResult, **kwargs: Any) -> None:
        """Run when LLM ends running."""
        print("\n\ngeneration concluded")
        self._queue.put(self._stop_signal)
