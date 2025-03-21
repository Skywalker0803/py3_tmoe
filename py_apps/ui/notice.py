"""
A "confirm-only" notice dialog
"""

from textual.app import App, ComposeResult
from textual.widgets import Button, Label


class Notice(App[str]):
    """
    A "confirm-only" notice dialog

    Params:
        str msg: the notice message
        str ok: the ok button content
    """

    CSS_PATH = "notice.tcss"

    def __init__(self, msg: str, ok: str = "OK"):
        super().__init__()
        self.msg = msg
        self.ok = ok

    def compose(self) -> ComposeResult:
        yield Label(f":warning: 注意：{self.msg}")
        yield Button(self.ok, variant="success", id="ok")

    def on_button_pressed(self, event: Button.Pressed):
        """
        Textual built-in method to process button clicks
        """
        self.exit(event.button.id)
