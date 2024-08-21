import pdb
from src.Ticket import Ticket
from src.LLMresponse import LLMresponse
from src.AgentInterpreter import AgentInterpreter
from src.AgentDirector import AgentDirector
from src.AgentPlanner import AgentPlanner
from src.AgentTooling import AgentTooling
from src.AgentMemory import AgentMemory
from src.AgentAction import AgentAction

class Agent:
    def __init__(self) -> None:
        self._interpreter : AgentInterpreter = None
        self._director : AgentDirector = None
        self._planner : AgentPlanner = None
        self._tools : AgentTooling = None
        self._memory : AgentMemory = None
        self._action : AgentAction = None

    def setup(self, configs : dict) -> None:
        if "interpreter" in configs:
            self._interpreter = AgentInterpreter()
            self._interpreter.setup(configs["interpreter"])

        if "director" in configs:
            self._director = AgentDirector()
            self._director.setup(configs["director"])
        
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
    
    def handle_ticket(self, user_id : str, interaction : str) -> str:
        # Create Ticket
        ticket : Ticket = Ticket()
        ticket.create(user_id, interaction)

        # Interpret Interaction
        response : LLMresponse = self._interpreter.interpret(interaction)
        ticket.set_interpreter_response(response)

        # Create Solution Pipeline
        interpreted_interaction : str = ticket.interpreted_interaction
        response : LLMresponse = self._director.break_down(interpreted_interaction)
        ticket.set_director_response(response)

        tasks : list[dict] = ticket.tasks
        for task in tasks:
            plan : LLMresponse = self._planner.plan(task)