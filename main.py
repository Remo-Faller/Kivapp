from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.popup import Popup
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
import os

class Gallery(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.load_images()

    def load_images(self):
        image_dir = "images"
        grid = self.ids.gallery_grid

        for file_name in os.listdir(image_dir):
            if file_name.lower().endswith(('.jpg', '.png', '.jpeg')):
                path = os.path.join(image_dir, file_name)
                btn = Button(
                    background_normal=path,
                    size_hint_y=None,
                    height=200,
                    on_release=lambda btn, path=path: self.show_popup(path)
                )
                grid.add_widget(btn)

    def show_popup(self, path):
        popup = Popup(title="Podgląd", size_hint=(0.9, 0.9))
        popup.content = Image(source=path, allow_stretch=True, keep_ratio=True)
        popup.open()

class GalleryApp(App):
    def build(self):
        return Gallery()

if __name__ == "__main__":
    GalleryApp().run()
