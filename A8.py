# Author: Chia-Hao Chang
# GitHub Repo: A8-Sprite-Previewer

import math
import sys

from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QMainWindow, QFrame, QLabel, QVBoxLayout
from PyQt6.QtCore import Qt


# This function loads a series of sprite images stored in a folder with a
# consistent naming pattern: sprite_# or sprite_##. It returns a list of the images.
def load_sprite(sprite_folder_name, number_of_frames):
    frames = []
    padding = math.ceil(math.log(number_of_frames - 1, 10))
    for frame in range(number_of_frames):
        folder_and_file_name = sprite_folder_name + "/sprite_" + str(frame).rjust(padding, '0') + ".png"
        frames.append(QPixmap(folder_and_file_name))

    return frames


class SpritePreview(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sprite Preview")
        self.resize(400, 400)

        # This loads the provided sprite and would need to be changed for your own.
        self.num_frames = 21
        self.frames = load_sprite("spriteImages", self.num_frames)

        # Track which frame is currently displayed
        self.current_frame = 0

        # Make the GUI in the setupUI method
        self.setupUI()

    def setupUI(self):
        # An application needs a central widget - often a QFrame
        frame = QFrame()
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.image_label = QLabel()
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.image_label.setFixedSize(200, 200)

        self.show_current_frame()

        layout.addWidget(self.image_label)
        frame.setLayout(layout)

        self.setCentralWidget(frame)

    def show_current_frame(self):
        if not self.frames:
            self.image_label.setText("No images found.")
            return

        pixmap = self.frames[self.current_frame]

        if pixmap.isNull():
            self.image_label.setText("Image failed to load.")
            return

        scaled_pixmap = pixmap.scaled(
            150,
            150,
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.FastTransformation
        )
        self.image_label.setPixmap(scaled_pixmap)


def main():
    app = QApplication(sys.argv)
    # Create our custom application
    window = SpritePreview()
    # And show it
    window.show()
    app.exec()


if __name__ == "__main__":
    main()