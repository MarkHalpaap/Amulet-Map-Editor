import wx
from amulet_map_editor.api.wx.ui.mc.block.define.widget import (
    demo as block_define_demo,
)
from amulet_map_editor.api.wx.ui.mc.block.define.button import (
    demo as block_define_button_demo,
)


def demo():
    """
    Show a demo version of the UI.
    An app instance must be created first.
    """
    block_define_demo()
    block_define_button_demo()


if __name__ == "__main__":

    def main():
        app = wx.App()
        demo()
        app.MainLoop()

    main()