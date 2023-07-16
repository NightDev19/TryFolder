import os
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.metrics import inch, dp
from kivy.utils import platform
import pygame

class MusicPlayer(App):
    def build(self):
        self.is_repeating = False
        layout = BoxLayout(orientation='vertical', spacing=10)
        self.label = Label(text='Music Player', size_hint=(1, None), height=50)
        layout.add_widget(self.label)

        self.file_chooser = GridLayout(cols=1, spacing=10, size_hint=(1, None), padding=(10, 10))
        self.file_chooser.bind(minimum_height=self.file_chooser.setter('height'))
        scroll_view = ScrollView(size_hint=(1, 0.7))
        scroll_view.add_widget(self.file_chooser)
        layout.add_widget(scroll_view)

        control_layout = BoxLayout(orientation='horizontal', size_hint=(1, None), height=80)
        control_layout.add_widget(Button(text='<<|', on_press=self.previous_music, size_hint=(0.2, 1)))
        control_layout.add_widget(Button(text='Play', on_press=self.play_pause_music, size_hint=(0.3, 1)))
        control_layout.add_widget(Button(text='|>>', on_press=self.next_music, size_hint=(0.2, 1)))
        # control_layout.add_widget(Button(text='All', on_press=self.shuffle_music, size_hint=(0.15, 1)))
        # control_layout.add_widget(Button(text='∞', on_press=self.repeat_music, size_hint=(0.15, 1)))
        layout.add_widget(control_layout)
        
        

        self.current_file_path = None
        self.load_mp3_files()  # Load MP3 files on app start

        return layout

    def on_start(self):
        # Set the desired screen dimensions in inches
        desired_width_inch = 2.5  # Adjust as needed
        desired_height_inch = 5.0  # Adjust as needed

        # Convert inches to pixels based on the screen's DPI
        dpi = Window.dpi
        desired_width = int(desired_width_inch * dpi)
        desired_height = int(desired_height_inch * dpi)

        # Set the app's width and height in pixels
        Window.size = (dp(desired_width), dp(desired_height))

    @staticmethod
    def is_android():
        return platform == 'android'

    @staticmethod
    def dp(value):
        return Window.dpi * (value / 160.0)

    def load_mp3_files(self):
        mp3_files = self.collect_mp3_files()
        self.file_chooser.clear_widgets()
        for mp3_file in mp3_files:
            if os.path.exists(mp3_file):
                filename = os.path.basename(mp3_file)
                button = Button(text=filename, size_hint=(1, None), height=40, on_press=self.select_music,
                                background_color=(0, 0, 0, 0), background_normal='', background_down='')
                button.bind(size=button.setter('text_size'))
                self.file_chooser.add_widget(button)

    def collect_mp3_files(self):
        mp3_files = []
        for root, dirs, files in os.walk('./'):
            for file in files:
                if file.lower().endswith('.mp3'):
                    mp3_files.append(os.path.join(root, file))
        return mp3_files

    def select_music(self, instance):
        file_path = instance.text
        if os.path.exists(file_path):
            self.current_file_path = file_path
            self.label.text = os.path.basename(file_path)
            
            pygame.mixer.init()
            pygame.mixer.music.load(file_path)
            pygame.mixer.music.play()
        else:
            self.label.text = 'File not found'


    def play_pause_music(self, instance):
        if self.current_file_path:
            if pygame.mixer.music.get_busy():
                pygame.mixer.music.pause()
            else:
                pygame.mixer.music.unpause()
        elif self.file_chooser.children:
            file_path = os.path.join('./', self.file_chooser.children[0].text)
            pygame.mixer.music.load(file_path)
            pygame.mixer.music.play()
            self.current_file_path = file_path
            self.label.text = os.path.basename(file_path)

    def previous_music(self, instance):
        if self.file_chooser.children:
            current_index = self.get_current_file_index()
            if current_index is None:
                return
            previous_index = (current_index - 1) % len(self.file_chooser.children)
            previous_file_path = os.path.join('./', self.file_chooser.children[previous_index].text)
            pygame.mixer.music.load(previous_file_path)
            pygame.mixer.music.play()
            self.current_file_path = previous_file_path
            self.label.text = os.path.basename(previous_file_path)

    def next_music(self, instance):
        if self.file_chooser.children:
            current_index = self.get_current_file_index()
            if current_index is None:
                return
            next_index = (current_index + 1) % len(self.file_chooser.children)
            next_file_path = os.path.join('./', self.file_chooser.children[next_index].text)
            pygame.mixer.music.load(next_file_path)
            pygame.mixer.music.play()
            self.current_file_path = next_file_path
            self.label.text = os.path.basename(next_file_path)


    def get_current_file_index(self):
        if self.current_file_path:
            for index, child in enumerate(self.file_chooser.children):
                if child.text == os.path.basename(self.current_file_path):
                    return index
        return None

    # def shuffle_music(self, instance):
    #     self.label.text = 'Shuffle Music'

    # def repeat_music(self, instance):
    #     if self.current_file_path:
    #         if not self.is_repeating:
    #             self.is_repeating = True
    #             instance.text = "1"  # Update button text to "1"
    #         else:
    #             self.is_repeating = False
    #             instance.text = "All"  # Update button text to "All"
    #     else:
    #         self.is_repeating = False
    #         instance.text = "Repeat"  # Restore button text to "Repeat"

    def on_stop(self):
        pygame.mixer.quit()


if __name__ == '__main__':
    MusicPlayer().run()