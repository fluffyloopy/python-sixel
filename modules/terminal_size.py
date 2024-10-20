import os
import platform


class TerminalSize:
    def __init__(self):
        if platform.system() == "Windows":
            self.get_size = self._get_size_windows
        elif 'ANDROID_ROOT' in os.environ:
            self.get_size = self._get_size_android
        else:
            self.get_size = self._get_size_x11

    def _get_size_windows(self):
        import ctypes
        from ctypes import wintypes

        kernel32 = ctypes.WinDLL("kernel32", use_last_error=True)

        class CONSOLE_SCREEN_BUFFER_INFO(ctypes.Structure):
            _fields_ = [
                ("dwSize", wintypes._COORD),
                ("dwCursorPosition", wintypes._COORD),
                ("wAttributes", wintypes.WORD),
                ("srWindow", wintypes.SMALL_RECT),
                ("dwMaximumWindowSize", wintypes._COORD),
            ]

        hConsole = kernel32.GetStdHandle(-11)
        csbi = CONSOLE_SCREEN_BUFFER_INFO()
        res = kernel32.GetConsoleScreenBufferInfo(hConsole, ctypes.byref(csbi))
        if not res:
            return None

        width = (csbi.srWindow.Right - csbi.srWindow.Left + 1) * 8
        height = (csbi.srWindow.Bottom - csbi.srWindow.Top + 1) * 16

        return width, height
    
    def _get_size_android(self):
        try:
            import subprocess

            result = subprocess.run(["stty", "size"], capture_output=True, text=True)
            rows, cols = map(int, result.stdout.split())
            height = int(rows * 26.375)
            width = int(cols * 13.34)
            return width, height
        
        except Exception as e:
            print(f"Error importing subprocess: {e}")
            return None

    def _get_size_x11(self):
        try:
            import Xlib
            import Xlib.display

            display = Xlib.display.Display()
            root = display.screen().root
            window_id = root.get_full_property(
                display.intern_atom("_NET_ACTIVE_WINDOW"), Xlib.X.AnyPropertyType
            ).value[0]

            window = display.create_resource_object("window", window_id)
            geometry = window.get_geometry()

            width = geometry.width
            height = geometry.height

            display.close()

            return width, height

        except Exception as e:
            print(f"Error getting terminal size: {e}")
            return None

    def get_terminal_size_pixels(self):
        return self.get_size()

# # example use of the module:

# from modules.terminal_size import TerminalSize

# term_size = TerminalSize()
# size = term_size.get_terminal_size_pixels()
# width, height = size
# print(f"Terminal size: {width}x{height}")