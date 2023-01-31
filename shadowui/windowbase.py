
from .section import Section

class WindowBase(Section):    
    """Interface base class for all os level windows."""
    
    def __init__(self, name: str, **kwargs) -> None:
        super().__init__(name, **kwargs)

    def run(self):
        """Run the program main loop
        Needs to be implemented by child classes
        """
        # send load signals from leaf up, children should always be loaded first
        self.emit_signal_recursive_leaf_first("on_load")