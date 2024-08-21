from src.LLMresponse import LLMresponse

class AgentPlan:
    def __init__(self) -> None:
        self._task_type : str = None
        self._task_description : str = None
        self._plan : list[str] = None

    def __str__(self) -> str:
        return f"Task Type: {self._task_type}, Description: {self._task_description}, Plan: {self._plan}"

    def set(self, task_dict : dict, plan : LLMresponse) -> None:
        self._task_type = list(task_dict.keys())[0]
        self._task_description : str = task_dict[self._task_type]
        self._plan = plan.response