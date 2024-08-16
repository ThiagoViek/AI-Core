from src.AgentPlanner import AgentPlanner
from src.AgentTooling import AgentTooling
from src.AgentMemory import AgentMemory
from src.AgentAction import AgentAction

class Agent:
    def __init__(self) -> None:
        self._planner : AgentPlanner = None
        self._tools : AgentTooling = None
        self._memory : AgentMemory = None
        self._action : AgentAction = None

    def setup(self, configs : dict) -> None:
        pass