import pdb
from src.Ticket import Ticket
from src.LLMresponse import LLMresponse
from src.AgentInterpreter import AgentInterpreter
from src.AgentDirector import AgentDirector
from src.AgentPlanner import AgentPlanner
from AgentExecutor import AgentExecutor
from src.AgentPlan import AgentPlan
from src.AgentAdvisor import AgentAdvisor
from src.AgentRegistry import AgentRegistry

class AgentGraph:
    def __init__(self) -> None:
        self._database : AgentRegistry = None
        self._interpreter : AgentInterpreter = None
        self._director : AgentDirector = None
        self._planner : AgentPlanner = None
        self._executor : AgentExecutor = None
        self._advisor : AgentAdvisor = None

    def setup(self, configs : dict) -> None:
        self._database = AgentRegistry()
        self._database.setup(configs["registry"])

        if "interpreter" in configs:
            self._interpreter = AgentInterpreter()
            self._interpreter.setup(configs["interpreter"])

        if "director" in configs:
            self._director = AgentDirector()
            self._director.setup(configs["director"])
        
        if "planner" in configs:
            self._planner = AgentPlanner()
            self._planner.setup(configs["planner"])

        if "executor" in configs:
            self._executor = AgentExecutor()
            self._executor.setup(configs["executor"])

        if "advisor" in configs:
            self._advisor = AgentExecutor()
            self._advisor.setup(configs["advisor"])
    
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

        task_queue : list[dict] = ticket.tasks
        plan_queue : list[AgentPlan] = []

        # TODO: Process Queue concurrently
        for task in task_queue:
            response : LLMresponse = self._planner.plan(task)
            ticket.set_planner_response(response)

            plan : AgentPlan = AgentPlan()
            plan.set(task, response)

            plan_queue.append(plan)

        # TODO: Process Solution Concurrently
        solution_report : list[str] = []
        for plan in plan_queue:
            solution : LLMresponse = self._executor.execute(plan)
            ticket.set_executor_response(solution)
            solution_report.append(solution.response)

        # Generate Interaction
        response : LLMresponse = self._advisor.generate_interaction(solution_report)
        ticket.set_advisor_response(response)

        # Publish Data
        self._database.publish(ticket)