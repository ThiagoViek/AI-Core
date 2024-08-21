import pdb
import json
from typing import Union

class ResponseFormat:
    TEXT : str = "TEXT"
    JSON : str = "JSON"
    SLIST : str = "SLIST"
    JLIST : str = "JLIST"
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
    
    @staticmethod
    def to_json_list(text: str) -> list[str]:
        """
        Converts the input text to a list of jsons.
        """
        if text.startswith("[") and text.endswith("]"):
            text = text[1:-1]
        json_items = [item.strip() for item in text.split(",")]
        return [json.loads(item) for item in json_items]

    @classmethod
    def convert(cls, text: str, format: str) -> Union[str, list[str], dict]:
        """
        Converts the input text to the specified format.
        """
        if format == cls.TEXT:
            return text
        elif format == cls.SLIST:
            return cls.to_list(text)
        elif format == cls.JLIST:
            return cls.to_json_list(text)
        elif format == cls.JSON:
            return cls.to_json(text)
        elif format == cls.NONE:
            return text
        else:
            raise ValueError(f"Invalid format: {format}")