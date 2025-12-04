import numpy as np
from morse_notes_international.arduino_zender import (
    ArduinoVISADevice,
    list_resources,
    converting_ADC,
)  # noqa
# from pythondaq.cli import scan


class DiodeExperiment:
    def __init__(self, port):
        self.device = ArduinoVISADevice(port="ASRL6::INSTR")

    def LED(self, start, stop):
        resistance = 220  # ohm
        ADC_start = converting_ADC(start)
        ADC_stop = converting_ADC(stop)

        self.device.set_output_value(1000)

        # for ADC in range(ADC_start, ADC_stop + 1):
        #     self.device.set_output_value(ADC)

        #     voltage_ch2 = self.device.get_input_voltage(ch=2)

        #     voltage_diode = self.device.get_input_voltage(
        #         ch=1
        #     ) - self.device.get_input_voltage(ch=2)

        #     current = voltage_ch2 / resistance

        # self.device.set_output_value(3.3)
