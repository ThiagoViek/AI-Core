from src.AgentPlanner import AgentPlanner
from src.AgentTooling import AgentTooling
from src.AgentMemory import AgentMemory
from src.AgentAction import AgentAction

class Agent:
    def __init__(self) -> None:
        # self._interpreter : AgentInterpreter = None
        self._planner : AgentPlanner = None
        self._tools : AgentTooling = None
        self._memory : AgentMemory = None
        self._action : AgentAction = None

    def setup(self, configs : dict) -> None:
        if "planner" in configs:
            self._planner = AgentPlanner()
            self._planner.setup(configs["planner"])

        if "tools" in configs:
            self._tools = AgentTooling()
            self._tools.setup(configs["tools"])

        if "memory" in configs:
            self._memory = AgentMemory()
            self._memory.setup(configs["memory"])

        if "action" in configs:
            self._action = AgentAction()
            self._action.setup(configs["action"])