from abc import ABCMeta, abstractmethod, ABC
from collections.abc import Iterable
from typing import Iterator

from dateutil.parser import parse


class DeadlinedMetaReminder(Iterable, metaclass=ABCMeta):

    @abstractmethod
    def is_due(self):
        pass

class DeadlinedReminder(Iterable, ABC):

    @abstractmethod
    def is_due(self):
        pass

class DateReminder(DeadlinedReminder):

    def __init__(self, text, date):
        self.date = parse(date, dayfirst=True)
        self.text = text

    def is_due(self):
        pass

    def __iter__(self):
        pass