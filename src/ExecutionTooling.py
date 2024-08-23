class ExecutionTooling:
    def __init__(self) -> None:
        self._descriptor : list[str] = None

    def setup(self, configs : dict) -> None:
        pass

    def get_context(self, task : str, step : str) -> dict:
        """
        Use tools defined to retrieve information defined in the task.
        """
        pass