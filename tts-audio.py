from gtts import gTTS
import langs
import os, pygame, signal
import intro
from lib import exit, sound, helper
from model.State import SoundState, ModeState
from typing import Dict

# declare global variable
default_lang: str = 'zh-TW'
dict_langs: Dict[str, str] = langs.lang
current_path: str = os.getcwd()
playing: SoundState = SoundState.PLAYING
mode: ModeState = ModeState.DEFAULT_MODE

#setup logger
logger = helper.setup_logger()

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
        message = f"Set current language to {dict_langs[default_lang]} successfully!!!"
        logger.info(message)
    else:
        match cmd:
            case '/c':
                logger.info("Displayed current configuration")
                print(f'[+] Current language: \033[92m{default_lang} ({dict_langs[default_lang]})\033[0m')
                print(f'[+] Current mode: \033[92m{"One .mp3 file" if mode == ModeState.DEFAULT_MODE else "Multiple .mp3 files"}\033[0m')
                print(f'[+] Current sound mode: \033[92m{"On" if playing == SoundState.PLAYING else "Off"}\033[0m')
            case '/m':
                mode = mode.toggle()
                if mode == ModeState.MULTIPLE_MODE:
                    logger.info("Set current mode to Multiple .mp3 files successfully!!!")
                else:
                    logger.info("Set current mode to One .mp3 files successfully!!!")
            case '/s':
                playing = playing.toggle()
                sound_msg = "Sound on" if playing == SoundState.PLAYING else "Sound off"
                logger.info(sound_msg)
            case _:
                logger.warning(f"Invalid command: {cmd}")
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

        logger.info(f"Input text: {user_text}")
        try:
            tts: gTTS = gTTS(text=user_text, lang=default_lang)
            index = 1
            while True:
                if not os.path.exists(f'audio_{index}.mp3'):
                    break
                index += 1
            tts.save(f'audio_{index}.mp3')
            file_path = os.path.join(current_path, f'audio_{index}.mp3')
            logger.info(f"Saved audio file: {file_path}")
            if playing == SoundState.PLAYING:
                sound.play_sound(file_path)
                logger.info(f"Played audio: {file_path}")
            print("\033[92mGenerating successfully!!!\033[0m")
            print(f"Your file path: {file_path}")
        except AssertionError as e:
            logger.error(f"File generation error: {e}")

    elif mode == ModeState.MULTIPLE_MODE:
        file_path: str = input('Enter your .txt file path to generate audio: ').strip(" '\"")
        if file_path.startswith('/'):
            command(file_path)
            return start()
        if os.path.exists(file_path):
            logger.info(f"Input text file: {file_path}")
            name_file = os.path.splitext(os.path.basename(file_path))[0]
            with open(file_path, 'r', encoding='utf-8') as f:
                for index, line in enumerate(f):
                    text = line.strip()
                    try:
                        tts = gTTS(text=text, lang=default_lang)  # remove line break character
                        logger.info(f"Generated: {name_file}_{index + 1}.mp3 | Text: {text}")
                        tts.save(f'{name_file}_{index + 1}.mp3')
                    except AssertionError as e:
                        logger.error(f"Error generating {name_file}_{index + 1}.mp3: {e}")
            print("\033[92mGenerating successfully!!!\033[0m")
            print(f"Your all audio files are saved in: {os.getcwd()}")
        else:
            logger.warning(f"Invalid file path: {file_path}")
    print("\n")
    start()


if __name__ == '__main__':
    intro.banner()
    logger.info("Application started")
    print(f'[+] Current language: \033[92m{default_lang} ({dict_langs[default_lang]})\033[0m')
    print(f'[+] Current mode: \033[92m{"One .mp3 file" if mode == ModeState.DEFAULT_MODE else "Multiple .mp3 files"}\033[0m')
    print(f'[+] Current sound mode: \033[92m{"On" if playing == SoundState.PLAYING else "Off"}\033[0m')
    start()