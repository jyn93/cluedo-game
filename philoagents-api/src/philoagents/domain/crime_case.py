from pydantic import BaseModel, Field
from typing import List


class CrimeCase(BaseModel):
    """
    A class representing a crime case in a Cluedo-style investigation.

    Args:
        id (str): Unique identifier for the crime case.
        description (str): Description of the crime case.
        suspects (List[Suspect]): List of suspects involved in the crime case.
        case_description (str): Description of the case.
        summary_case (str): Short summary of the case.
        crime_scene (str): Description of the crime scene.
        victim (str): Name of the victim.
        weapon (str): Name of the weapon.
        location (str): Name of the location.
        culprit (str): Name of the culprit.
    """
    id: str = Field(description="Unique identifier for the crime case")
    case_description: str = Field(description="Description of the case")
    summary_case: str = Field(description="Short summary of the case")
    crime_scene: str = Field(description="Description of the crime scene")
    victim: str = Field(description="Name of the victim")
    weapon: str = Field(description="Name of the weapon")
    location: str = Field(description="Name of the location")
    culprit: str = Field(description="Name of the culprit")

    def __str__(self) -> str:
        return (
            f"CrimeCase(id={self.id}, suspects={self.suspects}, "
            f"case_description={self.case_description}, summary_case={self.summary_case}, "
            f"crime_scene={self.crime_scene}, victim={self.victim}, weapon={self.weapon}, "
            f"location={self.location}, culprit={self.culprit})"
        )
