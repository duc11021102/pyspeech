import sys
import types

def smooth_exit(signal: int, frame: types.FrameType | None) -> None:
    print("\n")
    print("\nPROGRAM EXITING GRACEFULLY!!!")
    sys.exit(0)