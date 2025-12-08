import time as t

from morse_notes_international.arduino_interperter import (
    ArduinoVISADevice,
    resource_list,
)


def device_list():
    """creates a list of connected ports
    Returns:
    list: A list of connected ports."""

    ports = resource_list()
    return ports


class PhotoResistor:
    # measures amout of light being absorbd by the Photo resistor

    def __init__(self):
        """Connect with the Arduino.

        Args:
            port (str): The port to which the Arduino is connected.
        """
        self.device = ArduinoVISADevice(port="ASRL11::INSTR")

    def scan(self):
        self.device.set_output_value(value=1023)
        data = self.device.get_input_value(2)
        print(data)
        return data

    def on(self):
        # measure while turned on
        data = []
        i = 0
        while i <= 1000:
            i += 1
            light_score = PhotoResistor.scan(self)
            data.append(light_score)
            t.sleep(0.1)
        return data


print(device_list())
resistor = PhotoResistor()
a = resistor.on()
print(a)
