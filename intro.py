def banner():
    ascii_art = r"""
    ____        _____                      __  
   / __ \__  __/ ___/____  ___  ___  _____/ /_ 
  / /_/ / / / /\__ \/ __ \/ _ \/ _ \/ ___/ __ \
 / ____/ /_/ /___/ / /_/ /  __/  __/ /__/ / / /
/_/    \__, //____/ .___/\___/\___/\___/_/ /_/ 
      /____/     /_/                                                                                                                                       
    """

    BLUE = "\033[34m"
    RESET = "\033[0m"
    BLUE_GEM = "\033[36m"
    INTRODUCTION = "The text to speech tool using gTTS - Python 3"
    GIT_LINK = "Git Link - https://github.com/duc11021102/pyspeech"
    AUTHOR = "Author - (Hoang Minh Duc [Vietnamese])"
    print(BLUE + ascii_art + RESET)
    print(BLUE_GEM + INTRODUCTION + RESET)
    print(BLUE_GEM + GIT_LINK + RESET)
    print(BLUE_GEM + AUTHOR + RESET)
    print("\n")