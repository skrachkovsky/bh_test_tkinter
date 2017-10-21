from abc import ABCMeta, abstractmethod
from tkinter import ttk


class BaseFrame(ttk.Frame, metaclass=ABCMeta):
    def __init__(self, master=None):
        ttk.Frame.__init__(self, master)
        self._build_elements()
        self._handle_events()

    @abstractmethod
    def _build_elements(self):
        pass

    @abstractmethod
    def _handle_events(self):
        pass
