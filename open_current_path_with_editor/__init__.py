from core.commands import OpenWithEditor
from fman import show_alert
from fman.url import as_human_readable
from os.path import exists

class OpenCurrentPathWithEditor(OpenWithEditor):
    def __call__(self):
        path_to_open = self.pane.get_path()

        if exists(as_human_readable(path_to_open)):
            super().__call__(path_to_open)
        else:
            show_alert('No current path detected!')
