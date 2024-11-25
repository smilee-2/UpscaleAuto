import time
import pywinauto
from pywinauto import Application, findwindows
import psutil


class MainPage:

    _SELECT_IMAGE = 'Select Image'
    _OPEN = 'Открыть'
    _UPSCAYL = 'Upscayl'
    _ADDRESS = 'Адрес'

    def __init__(self, app=None):
        self.app = app

    def start_upscayl(self, image: str):
        for process in psutil.process_iter():
            if process.name() == 'Upscayl.exe':
                self.upscayl(image, status=True)
                break
        else:
            self.upscayl(image)

    def upscayl(self, image: str, status: bool = False):

        if not status:
            self.app = Application(backend="uia").start(fr"C:\Program Files\Upscayl\Upscayl.exe", wait_for_idle=False,
                                                        timeout=10)
            self.app = Application(backend="uia").connect(best_match="Upscayl", timeout=5)
        else:
            try:
                self.app = Application(backend="uia").connect(best_match="Upscayl", timeout=5)
            except:
                self.app.kill()
                return
        self.app.top_window().wait("enabled", timeout=5)
        self.app.top_window().child_window(title=self._SELECT_IMAGE).click()
        time.sleep(1)
        file_dlg = self.app.window(title_re="Select Image")
        file_dlg.child_window(title=f"{image}").select()
        time.sleep(1)
        file_dlg.child_window(title=self._OPEN, control_type="Button", found_index=2).click()
        self.app.top_window().child_window(title=self._UPSCAYL, found_index=2).click()

    def close_upscayl(self, cmd):
        if cmd == "отключить upscayl":
            self.app.kill()
