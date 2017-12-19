import wx
import time
from pykeyboard import PyKeyboardEvent
from pymouse import PyMouseEvent

class KeyBoardEventListener(PyKeyboardEvent):
    def __init__(self):
        self.end = False
        self.pressed_c = False
        super(KeyBoardEventListener, self).__init__()

    def tap(self, keycode, character, press):  # press is boolean; True for press, False for release
        if character == 'q':
            self.end = True

        elif character == 'c':
            self.pressed_c = True


class MouseClickEventListener(PyMouseEvent):
    def __init__(self):
        self.clicked_positions = []
        self.clicked = False
        self.clicked_time = time.time()
        super(MouseClickEventListener, self).__init__()

    def click(self, x, y, button, press):
        if len(self.clicked_positions) < 2 and (x, y) not in self.clicked_positions:
            print('[E] Mouse Event: click, x: {}, y: {}'.format(x, y))
            self.clicked_positions.append((x, y))
        self.clicked = True
        self.clicked_time = time.time()


def main():
    # Our IO event listeners
    keyevents = KeyBoardEventListener()
    mouseevents = MouseClickEventListener()
    keyevents.start()
    mouseevents.start()



    count = 10
    start = time.time()
    app = wx.App()
    screen = wx.ScreenDC()
    for i in xrange(count):
        bmp = wx.Bitmap(100,100)
        mem = wx.MemoryDC(bmp)
        mem.Blit(0, 0, 100, 100, screen, 0, 0)
        del mem
        bmp.SaveFile('endlesslake.png', wx.BITMAP_TYPE_PNG)

    assert isinstance(start, object)
    print time.time() - start


if __name__ == '__main__':
    main()