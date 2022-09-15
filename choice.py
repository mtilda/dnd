import random

import inquirer
from typing_extensions import Self

from mixins.logging import LoggingMixin


class Choice(LoggingMixin):
    """
    Represents a choice to be made
    """

    def __init__(self, quota: int, *options):
        self.quota = quota
        self.options = list(options)

    def __call__(self, topic: str):
        self.log.info(
            "User must chose %s from a set of %s with %s duplicate(s)"
            % (
                self.quota,
                len(self.options),
                len(self.options) - len(set(self.options)),
            )
        )

        remaining = self.options
        chosen = []
        while len(chosen) < self.quota:
            choice = inquirer.prompt(
                [
                    inquirer.List(
                        topic,
                        "Chose a %s" % topic,
                        ["random", *set(remaining)],
                        carousel=True,
                    )
                ]
            )[topic]
            if choice == "random":
                chosen.extend(random.sample(remaining, k=self.quota - len(chosen)))
                break
            remaining.remove(choice)
            chosen.append(choice)

        return chosen


class ChosableFieldsMeta(type):
    def __new__(cls: type[Self], name: str, bases: tuple[type], attrs: dict) -> Self:
        for field_key, field_name in attrs.items():
            field_value = attrs.get(field_key)
            if isinstance(field_value, Choice):
                field_value = field_value(field_name or field_key)
                print(field_value)
            attrs[field_key] = field_value
        return super().__new__(cls, name, bases, attrs)
