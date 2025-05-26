import json
from pathlib import Path
from typing import List

from pydantic import BaseModel, Field


class SuspectExtract(BaseModel):
    """A class representing raw suspect data extracted from external sources.

    This class follows the structure of the suspects.json file and contains
    basic information about suspects before enrichment.

    Args:
        id (str): Unique identifier for the suspect.
        urls (List[str]): List of URLs with information about the suspect.
    """

    id: str = Field(description="Unique identifier for the suspect")
    urls: List[str] = Field(
        description="List of URLs with information about the suspect"
    )

    @classmethod
    def from_json(cls, metadata_file: Path) -> list["SuspectExtract"]:
        with open(metadata_file, "r") as f:
            suspects_data = json.load(f)

        return [cls(**suspect) for suspect in suspects_data]


class Suspect(BaseModel):
    """A class representing a suspect agent with memory capabilities.

    Args:
        id (str): Unique identifier for the suspect.
        name (str): Name of the suspect.
        perspective (str): Description of the suspect's theoretical views
            about AI.
        style (str): Description of the suspect's talking style.
    """

    id: str = Field(description="Unique identifier for the suspect")
    name: str = Field(description="Name of the suspect")
    perspective: str = Field(
        description="Description of the suspect's theoretical views about AI"
    )
    style: str = Field(description="Description of the suspect's talking style")

    def __str__(self) -> str:
        return f"Suspect(id={self.id}, name={self.name}, perspective={self.perspective}, style={self.style})"
