import logging
from typing import Optional


class LoggingMixin:
    _log: Optional[logging.Logger] = None

    @property
    def log(self) -> logging.Logger:
        if self._log is None:
            self._log = logging.getLogger(
                self.__class__.__module__ + "." + self.__class__.__name__
            )
        return self._log
