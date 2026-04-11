# Author: Chia-Hao Chang
# GitHub Repo: A8-Sprite-Previewer

import math
import sys

from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QFrame, QLabel,
    QVBoxLayout, QHBoxLayout, QPushButton, QSlider
)
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
        self.resize(420, 420)

        # This loads the provided sprite and would need to be changed for your own.
        self.num_frames = 21
        self.frames = load_sprite("spriteImages", self.num_frames)

        # Track which frame is currently displayed
        self.current_frame = 0

        # Current fps value
        self.fps = 1

        # Make the GUI in the setupUI method
        self.setupUI()

    def setupUI(self):
        frame = QFrame()
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(20)

        # Top area: image + slider
        top_layout = QHBoxLayout()
        top_layout.setSpacing(30)

        self.image_label = QLabel()
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.image_label.setFixedSize(180, 180)
        self.show_current_frame()

        self.fps_slider = QSlider(Qt.Orientation.Vertical)
        self.fps_slider.setRange(1, 100)
        self.fps_slider.setValue(self.fps)
        self.fps_slider.setTickPosition(QSlider.TickPosition.TicksBothSides)
        self.fps_slider.setTickInterval(10)
        self.fps_slider.valueChanged.connect(self.update_fps_label)

        top_layout.addWidget(self.image_label)
        top_layout.addWidget(self.fps_slider)

        # FPS labels
        fps_layout = QHBoxLayout()
        fps_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.fps_text_label = QLabel("Frames per second")
        self.fps_text_label.setStyleSheet("font-size: 16px;")

        self.fps_value_label = QLabel(str(self.fps))
        self.fps_value_label.setStyleSheet("font-size: 16px;")

        fps_layout.addWidget(self.fps_text_label)
        fps_layout.addSpacing(10)
        fps_layout.addWidget(self.fps_value_label)

        # Start button
        self.start_button = QPushButton("Start")
        self.start_button.setFixedHeight(40)

        main_layout.addLayout(top_layout)
        main_layout.addLayout(fps_layout)
        main_layout.addWidget(self.start_button)

        frame.setLayout(main_layout)
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
            140,
            140,
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.FastTransformation
        )
        self.image_label.setPixmap(scaled_pixmap)

    def update_fps_label(self, value):
        self.fps = value
        self.fps_value_label.setText(str(value))


def main():
    app = QApplication(sys.argv)
    # Create our custom application
    window = SpritePreview()
    # And show it
    window.show()
    app.exec()


if __name__ == "__main__":
    main()