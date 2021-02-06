import PySimpleGUI as sg
from get_file import get_file
import music
import os

sg.theme("DarkPurple4")

settings = music.music_settings()
file = get_file()
file_basename = os.path.basename(file)

try:
    sg.theme(settings['theme'])
except TypeError:
    sg.popup("Oops! Settings loader failed! ")
    exit()


layout = [
        [sg.Button("PLAY",font=("Arial", 12), size=["50", "4"], key='-PLAY-')],
        [sg.Button("PAUSE", font=("Arial", 12),size=["50", "4"], key='-PAUSE-')],
        [sg.Button("UNPAUSE", font=("Arial",12),size=["50", "4"], key='-UNPAUSE-')],
        [sg.Button("RESET", font=("Arial", 12),size=["50", "4"], key="-RESET-")],
        [sg.Text("VOLUME",font=("Arial", 12),size=["10", "0"]),sg.Slider(range=(0, 10), default_value= 5,
        orientation = 'horizontal', key='-VOLUME-', enable_events=True)],
        [sg.Button("EXIT PLAYER", font=("Arial", 12),size=["50", "3"], key="-EXIT_PLAYER-")]
]

window = sg.Window("song", layout)

while True:
    events, values = window.read()

    if events in ('-EXIT_PLAYER-', None):
        music.Exit()

    elif events in ("-PLAY-"):
        music.Play(file)
        music.adjust_volume(settings['volume'])

    elif events in ("-PAUSE-"):
        music.Pause()

    elif events in ('-UNPAUSE-'):
        music.Unpause()

    elif events in ('-RESET-'):
        music.Reset()

    elif events in ('-VOLUME-'):
        volume = values['-VOLUME-']
        music.adjust_volume(volume)

    else:
        sg.popup("Event not recognised")




