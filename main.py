import tkinter as tk
import pygame
import os

class MusicPlayer:
    def __init__(self, window):
        self.window = window
        self.window.title("Music Player")
        self.window.geometry("300x200")
        self.window.configure(bg="#1f1f1f")
        self.window.resizable(False, False)

        # Initialize Pygame mixer
        pygame.mixer.init()

        self.button_font = ("Arial", 12)

        # Create label for music name
        self.music_label = tk.Label(window, text="Play something", fg="#ffffff", bg="#1f1f1f", font=("Arial", 14))
        self.music_label.pack(pady=10)

        # Create buttons
        self.previous_button = tk.Button(window, text="⏮ Previous", command=self.play_previous, font=self.button_font, bg="#1f1f1f", fg="#ffffff")
        self.previous_button.pack(pady=5)

        self.play_pause_button = tk.Button(window, text="▶ Play", command=self.toggle_play_pause, font=self.button_font, bg="#1f1f1f", fg="#ffffff")
        self.play_pause_button.configure(width=8)
        self.play_pause_button.pack(pady=10)

        self.next_button = tk.Button(window, text="⏭ Next", command=self.play_next, font=self.button_font, bg="#1f1f1f", fg="#ffffff")
        self.next_button.pack(pady=5)

        self.current_song_index = 0
        self.song_list = [
            "Slayer - Delusions of Saviour.mp3",
            "Derek And The Dominos - Layla.mp3",
            "Don McLean - American Pie.mp3"
        ]
        
        #Load up the first song
        self.play_song()
        self.pause_song()
        

    def toggle_play_pause(self):
        if pygame.mixer.music.get_busy():
            self.pause_song()
        else:
            self.unpause_song()

    def play_song(self):
        pygame.mixer.music.load(self.song_list[self.current_song_index])
        pygame.mixer.music.play()
        self.play_pause_button.configure(text="⏸")
        self.update_music_label(os.path.splitext(os.path.basename(self.song_list[self.current_song_index]))[0])

    

    def unpause_song(self):
        pygame.mixer.music.unpause()
        self.play_pause_button.configure(text="⏸")

    def pause_song(self):
        pygame.mixer.music.pause()
        self.play_pause_button.configure(text="▶")

    def play_previous(self):
        if self.current_song_index > 0:
            self.current_song_index -= 1
        else:
            self.current_song_index = len(self.song_list) - 1

        self.stop_song()
        self.play_song()

    def play_next(self):
        if self.current_song_index < len(self.song_list) - 1:
            self.current_song_index += 1
        else:
            self.current_song_index = 0

        self.stop_song()
        self.play_song()

    def stop_song(self):
        pygame.mixer.music.stop()
        self.is_playing = False
        self.play_pause_button.configure(text="▶")
        self.update_music_label("Stopped")

    def update_music_label(self, text):
        self.music_label.configure(text=text)

if __name__ == "__main__":
    window = tk.Tk()
    window.configure(bg="#1f1f1f")
    music_player = MusicPlayer(window)
    window.mainloop()

