import numpy as np
from morse_notes_international.arduino_zender import (
    ArduinoVISADevice,
    list_resources,
    converting_ADC,
)
import time


class DiodeExperiment:
    def __init__(self):
        self.device = ArduinoVISADevice(port="ASRL15::INSTR")

    def scan(self):
        # self.device.set_output_value(1000)

        morse_beebs = {
            "a": ".-",
            "b": "-...",
            "c": "-.-.",
            "d": "-..",
            "e": ".",
            "f": "..-.",
            "g": "--.",
            "h": "....",
            "i": "..",
            "j": ".---",
            "k": "-.-",
            "l": ".-..",
            "m": "--",
            "n": "-.",
        }

        for a in morse_beebs.values():
            if a == ".":
                self.device.set_output_value(1000)
                time(1)

            if a == "-":
                self.device.set_output_value(1000)
                time(2)

        self.device.set_output_value(0)

        # self.device.set_output_value(0)
        # self.device.set_output_value(1000)
        # self.device.set_output_value(0)
        # self.device.set_output_value(1000)
        # self.device.set_output_value(0)


def LED():
    test = DiodeExperiment()
    return test.scan()


if __name__ == "__main__":
    LED()
