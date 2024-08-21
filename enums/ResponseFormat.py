import pdb
import json
from typing import Union

class ResponseFormat:
    TEXT : str = "TEXT"
    LIST : str = "LIST"
    JSON : str = "JSON"
    NONE : str = "NONE"

    @staticmethod
    def to_list(text: str) -> list[str]:
        """
        Converts the input text to a list of strings.
        """
        text = text.strip("[]")
        return [item.strip().strip('"').strip("'") for item in text.split(",")]

    @staticmethod
    def to_json(text: str) -> dict:
        """
        Converts the input text to a JSON format.
        """
        return json.loads(text)

    @classmethod
    def convert(cls, text: str, format: str) -> Union[str, list[str], dict]:
        """
        Converts the input text to the specified format.
        """
        if format == cls.TEXT:
            return text
        elif format == cls.LIST:
            return cls.to_list(text)
        elif format == cls.JSON:
            return cls.to_json(text)
        elif format == cls.NONE:
            return text
        else:
            raise ValueError(f"Invalid format: {format}")