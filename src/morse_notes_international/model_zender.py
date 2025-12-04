import numpy as np
from morse_notes_international.arduino_zender import (
    ArduinoVISADevice,
    list_resources,
    converting_ADC,
)


class DiodeExperiment:
    def __init__(self):
        self.device = ArduinoVISADevice(port="ASRL13::INSTR")

    def scan(self):
        self.device.set_output_value(1000)
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
