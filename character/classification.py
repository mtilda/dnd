from typing_extensions import Self

from base import Base


class Classification(Base):
    def __str__(self) -> str:
        return "%s: %s" % (self.__class__.__name__, self.__class__.__doc__)
