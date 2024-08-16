import pdb
from enums.LLMzoo import LLMzoo
from enums.ResponseFormat import ResponseFormat

class LLMresponse:
    def __init__(self) -> None:
        self._id : str = None
        self._status : int = 404
        self._response : str = None
        self._response_format : ResponseFormat = ResponseFormat.NONE
        self._model : LLMzoo = LLMzoo.NONE
        self._input_tokens : int = 0
        self._input_tokens_cost : float = 0.0
        self._output_tokens : int = 0
        self._output_tokens_cost : float = 0.0
        self._walltime_US : float = 0.0

    def __str__(self) -> str:
        return self._response

    def set_response(self, response, walltime_US : float) -> None:
        self._id = response.id
        self._status = 200
        self._response = response.choices[0].message.content
        self._response_format = ResponseFormat.TEXT
        self._model = response.model
        self._input_tokens = response.usage.prompt_tokens
        self._output_tokens = response.usage.completion_tokens
        self._walltime_US = int(walltime_US)

    def set_error(self, oops : Exception) -> None:
        self._response = f'Error: {str(oops)}'

    @property
    def response(self) -> str:
        return self._response