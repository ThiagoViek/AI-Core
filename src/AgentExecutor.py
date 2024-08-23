import pdb

from src.LLM import LLM
from ExecutionMemory import ExecutionMemory
from ExecutionTooling import ExecutionTooling
from src.AgentPlan import AgentPlan
from src.LLMresponse import LLMresponse
from src.InstructionReader import InstructionReader

class AgentExecutor:
    def __init__(self) -> None:
        self._llm : LLM = None
        self._tools : ExecutionTooling = None
        self._memory : ExecutionMemory = None
        self._instruction : InstructionReader = None

    def setup(self, configs : dict) -> None:
        self._llm = LLM()
        self._instruction = InstructionReader()

        self._llm.set_key(configs["llm"]["api-key-filepath"])
        self._llm.setup(configs["llm"]["model-specs"])
        self._instruction.setup_template_files(configs["instructions"])

        self._tools.setup(configs["tools"])
        self._memory.setup(configs["memory"])

    def execute(self, plan : AgentPlan) -> LLMresponse:
        type : str = plan.task_type
        task : str = plan.task_description
        steps : list[str] = plan.task_list

        execution_report : LLMresponse = None
        step_documentation : list[dict] = []
        for step in steps:
            tooling_context : dict = self._tools.get_context(task, step)
            memory_context : dict = self._memory.get_context(task, step)
            step_solution : dict = self._solve(task, step)
            step_documentation.append({
                "task-step":step,
                "tools":tooling_context,
                "memory":memory_context,
                "solution":step_solution
            })

        if type == "CONTRIBUTION":
            status : bool = self._upsert(step_documentation)
            
        execution_report : LLMresponse = self._report(step_documentation, status)
        return execution_report
    
    def _solve(self, task : str, step : str) -> dict:
        pass

    def _upsert(self, documentation : list[dict]) -> bool:
        pass

    def _report(self, documentation : list[dict], status : bool) -> LLMresponse:
        pass