import sys

def smooth_exit(signal, frame):
    print("\n")
    print("\nPROGRAM EXITING GRACEFULLY!!!")
    sys.exit(0)