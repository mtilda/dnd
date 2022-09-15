from typing import Optional

from mixins.logging import LoggingMixin


class Base(LoggingMixin):
    _ignored_attrs = {
        "description",
    }

    def __init__(self, name: str = None, description: Optional[str] = None):
        self.name = name
        self.description = description

    def __repr__(self):
        attrs = [
            "%s=%s" % (k, repr(v))
            for (k, v) in self.__dict__.items()
            if k not in self._ignored_attrs
        ]
        attrs.sort()
        classname = self.__class__.__name__
        return "<%s: %s>" % (classname, " ".join(attrs))
