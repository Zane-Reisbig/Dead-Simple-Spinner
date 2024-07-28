import time
from sys import stdout, argv
from os import system
from typing import IO


from threading import Thread
from itertools import cycle


class Spinner:
    def __init__(
        self,
        frames: list = ["|", "/", "-", "\\"],
        delay: int = 0.1,
        outIO: IO = stdout,
    ) -> None:
        self.out: IO = outIO
        self.frames = frames
        self.delay = delay

    def __writeFrame__(self, frameChar: str):
        def writeFlush(this):
            self.out.write(this)
            self.out.flush()

        writeFlush(frameChar)
        writeFlush("\b" * len(frameChar))

    def spin(self):

        for frame in cycle(self.frames):
            self.__writeFrame__(frame)
            time.sleep(self.delay)


useThis = Spinner()

if len(argv) == 2:
    useThis.frames = argv[1].split(",")
elif len(argv) > 2:
    raise AssertionError(f"{repr(argv[1:])} is not a SINGLE comma seperated string")

useThis.spin()
