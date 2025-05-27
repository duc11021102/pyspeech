import pygame, os, time

def safe_init_audio():
    """
    This function checks if the environment
    can play sound to avoid errors.
    If it doesn't play, run pygame with dummy env
    """
    try:
        pygame.mixer.init()
    except pygame.error as e:
        os.environ["SDL_AUDIODRIVER"] = "dummy"
        pygame.mixer.quit()
        pygame.mixer.init()

def play_sound(path: str):
    """
    This function play sound based on path
    get_busy() avoid running loops too fast which wastes CPU.
    :param path: str
    :return: None
    """
    safe_init_audio()
    pygame.mixer.music.load(path)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(0.1)
    pygame.mixer.music.stop() #stop playing
    pygame.mixer.quit() #release resource
    return