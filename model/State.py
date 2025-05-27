from enum import Enum

# declare classes
class SoundState(Enum):
    PLAYING = 1
    PAUSE = 0

    def toggle(self) -> 'SoundState':
        """
        Toggle between PLAYING and PAUSE states.
        :return: SoundState
        """
        return SoundState.PAUSE if self == SoundState.PLAYING else SoundState.PLAYING

class ModeState(Enum):
    DEFAULT_MODE = 0
    MULTIPLE_MODE = 1

    def toggle(self) -> 'ModeState':
        """
        Toggle between SINGLE and MULTIPLE modes.
        :return: ModeState
        """
        return ModeState.MULTIPLE_MODE if self == ModeState.DEFAULT_MODE else ModeState.DEFAULT_MODE