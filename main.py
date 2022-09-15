import logging

from character import Character
from mixins.logging import LoggingMixin

logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)


class Game(LoggingMixin):
    def __init__(self) -> None:
        m = Character(
            name="Mathilda",
            xp=10000,
            class_name="Fighter",
            race_name="Elf",
            description="A charming slut",
        )
        self.log.info("Now enters " + str(m))
        self.log.info(m.classification)
        # self.log.info(m.classification.primary_ability)


Game()
