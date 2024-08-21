from dataclasses import dataclass

@dataclass
class ResponseFormat:
    TEXT : str = "TEXT"
    JSON : str = "JSON"
    NONE : str = "NONE"