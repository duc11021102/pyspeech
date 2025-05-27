def banner():
    ascii_art: str = r"""
    ____        _____                      __  
   / __ \__  __/ ___/____  ___  ___  _____/ /_ 
  / /_/ / / / /\__ \/ __ \/ _ \/ _ \/ ___/ __ \
 / ____/ /_/ /___/ / /_/ /  __/  __/ /__/ / / /
/_/    \__, //____/ .___/\___/\___/\___/_/ /_/ 
      /____/     /_/                                                                                                                                       
    """

    BLUE: str = "\033[34m"
    RESET: str = "\033[0m"
    BLUE_GEM: str = "\033[36m"
    INTRODUCTION: str = "The text to speech tool using gTTS - Python 3"
    GIT_LINK: str = "Git Link - https://github.com/duc11021102/pyspeech"
    AUTHOR: str = "Author - (Hoang Minh Duc [Vietnamese])"
    print(BLUE + ascii_art + RESET + '\n'
          + BLUE_GEM + INTRODUCTION + RESET + '\n'
          + BLUE_GEM + GIT_LINK + RESET + '\n'
          + BLUE_GEM + AUTHOR + RESET + '\n')