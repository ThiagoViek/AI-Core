import pdb
import time
import openai
from src.LLMresponse import LLMresponse

class LLM:
    def __init__(self) -> None:
        self._LLM_client : openai.OpenAI = None
        self._model_id : str = None
        self._max_retries : int = None

    def set_key(self, configs : dict) -> None:
        filepath : str = configs["llm"]["api-key-filepath"]
        with open(filepath,'r') as f:
            key : str = f.read()
            self._LLM_client = openai.Client(api_key=key)
    
    def setup(self, configs : dict) -> None:
        self._max_retries = configs["llm"]["api-max-retries"]
        self._model_id = configs["llm"]["model-id"]

    def queue_attachment(self, message : str, attachment : str) -> dict:
        return {"role": "user", "content": [
            {"type":"text","text":message},
            {"type": "image_url", "image_url": {
                "url": f"data:image/png;base64,{attachment}"}
            }
        ]}

    def queue_message(self, role : str, message : str) -> dict:
        return {"role":role, "content":message}
    
    def request(self, prompt : list, max_tokens : int = 4096, temperature : float = 0.2, top_p : float = 1.0) -> LLMresponse:
        response : LLMresponse = LLMresponse()
        attempts : int = 0
        while attempts < self._max_retries:
            try:
                timestamp_start : time = time.time()
                raw_response = self._LLM_client.chat.completions.create(
                    model=self._model_id,
                    messages=prompt,
                    temperature=temperature,
                    max_tokens=max_tokens
                )
                walltime_US : float = (time.time() - timestamp_start) * 1e6
                response.set_response(raw_response, walltime_US)
                break
            except Exception as oops:
                attempts += 1
                time.sleep(0.1)
                response.set_error(oops)
        return response