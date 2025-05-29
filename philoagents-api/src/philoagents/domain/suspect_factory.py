from philoagents.domain.exceptions import (
    SuspectNameNotFound,
    SuspectDescriptionNotFound,
    SuspectTraitNotFound,
)
from philoagents.domain.suspect import Suspect

SUSPECT_NAMES = {
    "scarlet": "Miss Scarlet",
    "mustard": "Colonel Mustard",
    "white": "Mrs. White",
    "green": "Reverend Green",
    "peacock": "Mrs. Peacock",
    "plum": "Professor Plum",
}

SUSPECT_PERSPECTIVES = {
    "scarlet": "A cunning femme fatale with a mysterious past.",
    "mustard": "A decorated military man with a short temper.",
    "white": "A devoted housekeeper who knows all the secrets.",
    "green": "A shifty clergyman with questionable motives.",
    "peacock": "A glamorous socialite with a sharp wit.",
    "plum": "An absent-minded professor with a knack for trouble.",
}

SUSPECT_STYLES = {
    "scarlet": "charming and manipulative",
    "mustard": "brave and aggressive",
    "white": "observant and loyal",
    "green": "sly and persuasive",
    "peacock": "elegant and calculating",
    "plum": "intelligent and distracted",
}

AVAILABLE_SUSPECTS = list(SUSPECT_NAMES.keys())


class SuspectFactory:
    @staticmethod
    def get_suspect(id: str) -> Suspect:
        """Creates a suspect instance based on the provided ID.

        Args:
            id (str): Identifier of the suspect to create

        Returns:
            Suspect: Instance of the suspect

        Raises:
            ValueError: If suspect ID is not found in configurations
        """
        id_lower = id.lower()

        if id_lower not in SUSPECT_NAMES:
            raise SuspectNameNotFound(id_lower)

        if id_lower not in SUSPECT_PERSPECTIVES:
            raise SuspectDescriptionNotFound(id_lower)

        if id_lower not in SUSPECT_STYLES:
            raise SuspectTraitNotFound(id_lower)

        return Suspect(
            id=id_lower,
            name=SUSPECT_NAMES[id_lower],
            perspective=SUSPECT_PERSPECTIVES[id_lower],
            style=SUSPECT_STYLES[id_lower],
        )

    @staticmethod
    def get_available_suspects() -> list[str]:
        """Returns a list of all available suspect IDs.

        Returns:
            list[str]: List of suspect IDs that can be instantiated
        """
        return AVAILABLE_SUSPECTS