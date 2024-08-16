from src.LLMdefault import LLMDefault
from src.InstructionReader import InstructionReader

class AgentPlanner:
    def __init__(self) -> None:
        # LLMs
        self._llm_reflection : LLMDefault = None
        self._llm_critic : LLMDefault = None
        self._llm_chain_of_thought : LLMDefault = None
        self._llm_goal_decomp : LLMDefault = None

        # Instruction Files
        self._instructions_reflection : InstructionReader = None
        self._instructions_critic : InstructionReader = None
        self._instructions_chain_of_thought : InstructionReader = None
        self._instructions_goal_decomp : InstructionReader = None

    def setup(self, configs : dict) -> None:
        if "reflection" in configs:
            self._llm_reflection = LLMDefault()
            self._instructions_reflection = InstructionReader()

            self._llm_reflection.set_key(configs["reflection"])
            self._llm_reflection.setup(configs["reflection"])
            self._instructions_reflection.setup(configs["reflection"])

        if "critic" in configs:
            self._llm_critic = LLMDefault()
            self._instructions_critic = InstructionReader()

            self._llm_critic.set_key(configs["critic"])
            self._llm_critic.setup(configs["critic"])
            self._instructions_critic.setup(configs["critic"])

        if "chain-of-thought" in configs:
            self._llm_chain_of_thought = LLMDefault()
            self._instructions_chain_of_thought = InstructionReader()

            self._llm_chain_of_thought.set_key(configs["chain-of-thought"])
            self._llm_chain_of_thought.setup(configs["chain-of-thought"])
            self._instructions_chain_of_thought.setup(configs["chain-of-thought"])

        if "goal-decomposition" in configs:
            self._llm_goal_decomp = LLMDefault()
            self._instructions_goal_decomp = InstructionReader()

            self._llm_goal_decomp.set_key(configs["goal-decomposition"])
            self._llm_goal_decomp.setup(configs["goal-decomposition"])
            self._instructions_goal_decomp.setup(configs["goal-decomposition"])