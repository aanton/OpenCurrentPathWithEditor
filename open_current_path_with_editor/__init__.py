from core.commands import OpenWithEditor
from fman import show_alert
from os.path import exists

class OpenCurrentPathWithEditor(OpenWithEditor):
    def __call__(self):
        path_to_open = self.pane.get_path()

        if exists(path_to_open):
            self._open_with_editor(path_to_open)
        else:
            show_alert('No current path detected!')