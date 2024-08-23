import uuid
from src.LLMresponse import LLMresponse

class Ticket:
    def __init_(self) -> None:
        self._id : str = None
        self._user_id : str = None
        self._user_interaction : str = None
        self._interpreter_response : LLMresponse = None
        self._director_response : LLMresponse = None
        self._planner_responses : list[LLMresponse] = None
        self._executor_responses : list[LLMresponse] = None
        self._advisor_response : LLMresponse = None
        self._parent_ticket : Ticket = None
    
    def create(self, user_id : str, interaction : str) -> None:
        self._id = uuid.uuid4()
        self._user_id = user_id
        self._user_interaction = interaction
        self._planner_responses = []

    def set_interpreter_response(self, response : LLMresponse) -> None:
        self._interpreter_response = response

    def set_director_response(self, response : LLMresponse) -> None:
        self._director_response = response

    def set_planner_response(self, response : LLMresponse) -> None:
        self._planner_responses.append(response)

    def set_executor_response(self, response : LLMresponse) -> None:
        self._executor_responses.append(response)

    def set_advisor_response(self, response : LLMresponse) -> None:
        self._advisor_response = response

    @property
    def interpreted_interaction(self) -> str:
        return self._interpreter_response.response["message"]
    
    @property
    def tasks(self) -> str:
        return self._director_response.response