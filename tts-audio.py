from gtts import gTTS
import langs
import os, pygame, signal
import intro
from lib import exit
from lib import sound
from model.State import SoundState, ModeState
from typing import Dict

# declare global variable
default_lang: str = 'zh-TW'
dict_langs: Dict[str, str] = langs.lang
current_path: str = os.getcwd()
playing: SoundState = SoundState.PLAYING
mode: ModeState = ModeState.DEFAULT_MODE

# smooth Ctrl C, avoid error commands as exit
signal.signal(signal.SIGINT, exit.smooth_exit)

# check environment and set dummy only once when program starts.
try:
    pygame.mixer.init()
    pygame.mixer.quit()  # just test initialization, then shut down immediately
except pygame.error:
    os.environ["SDL_AUDIODRIVER"] = "dummy"
    import pygame  # re-import after setting dummy (safe)

def command(cmd : str) -> int:
    """
    This function handles commands from the user.
    :param cmd: str
    :return: 0
    """
    global default_lang
    global playing
    global mode
    lang: str = cmd[1:]

    if str(lang) in dict_langs:
        default_lang = str(lang)
        print(f"Set current language to \033[92m{dict_langs[default_lang]}\033[0m successfully!!!")
    else:
        match cmd:
            case '/c':
                print(f'[+] Current language: \033[92m{default_lang} ({dict_langs[default_lang]})\033[0m')
                print(f'[+] Current mode: \033[92m{"One .mp3 file" if mode == ModeState.DEFAULT_MODE else "Multiple .mp3 files"}\033[0m')
                print(f'[+] Current sound mode: \033[92m{"On" if playing == SoundState.PLAYING else "Off"}\033[0m')
            case '/m':
                mode = mode.toggle()
                if mode == ModeState.MULTIPLE_MODE:
                    print(f"Set current mode to \033[92m{'Multiple .mp3 files'}\033[0m successfully!!!")
                else:
                    print(f"Set current mode to \033[92m{'One .mp3 file'}\033[0m successfully!!!")
            case '/s':
                playing = playing.toggle()
                if playing == SoundState.PLAYING:
                    print("\033[92mSound on successfully\033[0m")
                else:
                    print("\033[92mSound off successfully\033[0m")
            case _:
                print("\033[91mInvalid command!\033[0m")
    return 0

def start() -> None:
    global default_lang
    if mode == ModeState.DEFAULT_MODE:
        user_text = input('Enter your text to get audio: ').strip()

        if len(user_text) == 0:
            return start()
        if user_text.startswith('/'):
            command(user_text)
            return start()

        print(f"Your text: \033[92m{user_text}\033[0m")
        try:
            tts: gTTS = gTTS(text=user_text, lang=default_lang)
            index = 1
            while True:
                if not os.path.exists(f'audio_{index}.mp3'):
                    break
                index += 1
            tts.save(f'audio_{index}.mp3')
            file_path = os.path.join(current_path, f'audio_{index}.mp3')
            print("Loading...")
            if playing == SoundState.PLAYING:
                print("Playing...")
                sound.play_sound(file_path)
            print("\033[92mGenerating successfully!!!\033[0m")
            print(f"Your file path: {file_path}")
        except AssertionError as e:
            print(f"\033[91mFile: Error ({e})\033[91m\033[0m")

    elif mode == ModeState.MULTIPLE_MODE:
        file_path: str = input('Enter your .txt file path to generate audio: ').strip(" '\"")
        if file_path.startswith('/'):
            command(file_path)
            return start()
        if os.path.exists(file_path):
            print(f"Your .txt file path: \033[92m{file_path}\033[0m")
            name_file = os.path.splitext(os.path.basename(file_path))[0]
            with open(file_path, 'r', encoding='utf-8') as f:
                for index, line in enumerate(f):
                    text = line.strip()
                    try:
                        tts = gTTS(text=text, lang=default_lang)  # remove line break character
                        print(f"Generating file {index + 1}: \033[92m{text}\033[0m")
                        tts.save(f'{name_file}_{index + 1}.mp3')
                    except AssertionError as e:
                        print(f"\033[91mGenerating file {index + 1}: Error ({e})\033[91m\033[0m")
            print("\033[92mGenerating successfully!!!\033[0m")
            print(f"Your all audio files are saved in: {os.getcwd()}")
        else:
            print("\033[91mYou entered an invalid path or not exists!\033[91m\033[0m")
    print("\n")
    start()


if __name__ == '__main__':
    intro.banner()
    print(f'[+] Current language: \033[92m{default_lang} ({dict_langs[default_lang]})\033[0m')
    print(f'[+] Current mode: \033[92m{"One .mp3 file" if mode == ModeState.DEFAULT_MODE else "Multiple .mp3 files"}\033[0m')
    print(f'[+] Current sound mode: \033[92m{"On" if playing == SoundState.PLAYING else "Off"}\033[0m')
    start()