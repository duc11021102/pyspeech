from enum import Enum

# declare classes
class SoundState(Enum):
    PLAYING = 1
    PAUSE = 0

    def toggle(self):
        """
        This function turn off or turn on
        sound mode
        :param self
        :return: state
        """
        return SoundState.PAUSE if self == SoundState.PLAYING else SoundState.PLAYING

class ModeState(Enum):
    DEFAULT_MODE = 0
    MULTIPLE_MODE = 1

    def toggle(self):
        """
        This function switch mode
        :param self
        :return: state
        """
        return ModeState.MULTIPLE_MODE if self == ModeState.DEFAULT_MODE else ModeState.DEFAULT_MODE