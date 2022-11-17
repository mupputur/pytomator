# from PIL import ImageGrab

import os


class ImageGrab:
    pass


class CaptureScreenShot:

    @classmethod
    def save(self, filename):
        snapshot = ImageGrab.grab()
        save_path = "C:\\Users\\training\\PycharmProjects\\pythonProject1\\Upputuri\\lawsonium\\ScreenCaptures"
        path = os.path.join(save_path, filename + '.png')
        snapshot.save(path)


if __name__ == "__main__":
    CaptureScreenShot.save('test')
