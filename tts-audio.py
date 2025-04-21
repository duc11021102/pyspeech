from gtts import gTTS
import langs
import os, pygame, time
import intro


default_lang = 'zh-TW'
dict_langs = langs.lang
current_path = os.getcwd()
playing = 1


def command(cmd):
    global default_lang
    global playing
    lang = cmd[1:]
    if cmd == '/c':
        print(f"Current language is: \033[92m{dict_langs[default_lang]}\033[0m")
    elif cmd == '/s':
        playing = 1 - playing
        if playing:
            print("\033[92mSound on successfully\033[0m")
        else:
            print("\033[92mSound off successfully\033[0m")
    elif str(lang) in dict_langs:
        default_lang = str(lang)
        print(f"Set current language to \033[92m{dict_langs[default_lang]}\033[0m successfully!!!")
    else:
        print("\033[91mInvalid command!\033[0m")

    start()
    return 0


def play_sound(path):
    os.environ["SDL_AUDIODRIVER"] = "dummy"
    pygame.mixer.init()
    pygame.mixer.music.load(path)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        time.sleep(0.1)
    pygame.mixer.music.stop() #stop playing
    pygame.mixer.quit() # release resources
    return

def start():
    user_text = input('Enter your text to get audio: ').strip()

    if user_text.startswith('/'):
        command(user_text)

    print(f"Your text: \033[92m{user_text}\033[0m")
    global default_lang
    tts = gTTS(text=user_text, lang=default_lang)

    index = 1
    while True:
        if not os.path.exists(f'audio_{index}.mp3'):
            break
        index +=1


    tts.save(f'audio_{index}.mp3')
    file_path = os.path.join(current_path, f'audio_{index}.mp3')
    print("Loading...")
    if playing:
        print("Playing...")
        play_sound(file_path)
    print("\033[92mGenerating successfully!!!\033[0m")
    print(f"Your file path: {file_path}")
    start()


if __name__ == '__main__':
    intro.banner()
    print(f'Current language: \033[92m{default_lang}\033[0m')
    print('\033[92mSound On\033[0m' if playing else '\033[92mSound Off\033[0m')
    start()