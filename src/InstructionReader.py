class InstructionReader:
    def __init__(self) -> None:
        self._sys_instruction_filepath : str = None
        self._user_instruction_filepath : str = None

        self._sys_instruction : str = None
        self._user_instruction : str = None

    def setup_template_files(self, configs : dict) -> None:
        self._sys_instruction_filepath : str = configs["instructions"]["sys-instruction"]
        self._user_instruction_filepath : str = configs["instructions"]["user-instruction"]

    def set_sys_template(self) -> str:
        with open(self._sys_instruction_filepath,"r") as f:
            self._sys_instruction = f.read()

    def set_user_template(self) -> str:
        with open(self._user_instruction_filepath,"r") as f:
            self._user_instruction = f.read()