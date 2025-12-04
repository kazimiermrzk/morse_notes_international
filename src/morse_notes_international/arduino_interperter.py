"""the controler module for communicating with an Arduino device via VISA protocol."""

import pyvisa


def resource_list():
    """prints ports that have something connected to the computer

    Returns:
        ports(string): ports of devices that are connected to computer
    """
    rm = pyvisa.ResourceManager("@py")
    ports = rm.list_resources()
    return ports


class ArduinoVISADevice:
    """This class communicates with the Arduino, measures and sets requested voltages.
    The voltages are set and measured in ADC values. The ADC to Voltage conversion is done in the method get_input_voltage.
    And is returned in the form of a float.
    The total range of the ADC is [0, 1023] which corresponds to a voltage range of [0V, 3.3V].
    """

    def __init__(self, port):
        """Opens communications with arduino

        Args:
            port (string): The port to which the Arduino is connected.
        """
        self.rm = pyvisa.ResourceManager("@py")
        self.device = self.rm.open_resource(
            port, read_termination="\r\n", write_termination="\n"
        )

    def get_identification(self):
        """Queries the device for its identification string.

        Returns:
            str: The identification string of the device.
        """
        return self.device.query("*IDN?")

    def set_output_value(self, value):
        """Sets the output value on channel 0.

        Args:
            value (int): The output value to set on channel 0, in the range [0, 1023].
        """
        self.ch0_output_value = value
        self.device.query(f"OUT:CH0 {value}")

    def get_output_value(self):
        """gives set output value in ADC of channel zero

        Returns:
            int: voltage in ADC over channel 0
        """
        return self.ch0_output_value

    def get_input_value(self, channel):
        """_summary_

        Args:
            channel (int): The input channel number to measure.

        Returns:
            int: The measured voltage in ADC units at the specified channel.
        """
        return self.device.query(f"MEAS:CH{channel}?")

    def turn_off(self):
        """turns light off"""
        self.set_output_value(0)
