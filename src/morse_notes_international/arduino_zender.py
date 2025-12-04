import pyvisa


# rm = pyvisa.ResourceManager("@py")


def list_resources():
    """List of ports.

    Gives the list containing the ports that are used by the arduino.

    Returns:
        str: multiple ports in the form of ASRL{}::INSTR.
    """
    # print(pyvisa.ResourceManager("@py").list_resources())

    return pyvisa.ResourceManager("@py").list_resources()


class ArduinoVISADevice:
    """User can communicate with the arduino."""

    def __init__(self, port):
        """Initializes the instance based on the port.

        Args:
            port (str): This is the port used to connect with the arduino.


        Attributes:
                device: Activates arduino by reading it's given port.
        """

        self.device = pyvisa.ResourceManager("@py").open_resource(
            port, read_termination="\r\n", write_termination="\n"
        )

    def get_identification(self):
        """Gives the identification string of the arduino.

        Returns:
             str: This string gives the version of the connected arduino.
        """

        identification = self.device.query("*IDN?")
        return identification

    def set_output_value(self, value):
        """User gives a value for the output.

        Here, the user puts in a value (e.g. 828) for the output in channel 0 to see
        wether the lamp will turn on or not. From this we conclude that this method works.

        Args:
            value (int): The ADC value.

        Returns:
            str: The given output value.
        """
        self.lamp = self.device.query(f"OUT:CH0 {value}")
        return self.lamp

    def get_output_value(self):
        """Checks the output value.

        The user checks wether the output value is the same as the input value.
        Both are used for channel 0.

        Returns:
            str: The given output value.
        """
        self.lamp_out = self.device.query(f"OUT:CH0?")
        return self.lamp_out

    def get_input_value(self, ch):
        """Requesting the voltage as ADC value on a given channel.

        Here, the user request the ADC value on a certain channel. The channel is
        detemined by the build of the circuit containing the arduino.

        Args:
            ch (str): Here the only two channels requested are channel 1 and channel 2.
                     Channel 1 gives the voltage over the diode and de resistance.
                     Channel 2 gives the voltage over the resistance only.

        Returns:
            int: The voltage over the given channel in ADC (so not in Volt!).
        """

        self.ADC_ch = int(self.device.query(f"MEAS:CH{ch}?"))

        return self.ADC_ch

    def get_input_voltage(self, ch):
        """requesting the voltage of the channel in Volt.

        The ADC value returned in get_input_value can be converted to the voltage in Volt.
        get_input_voltage and get_input_value should there give the same value.

        Args:
            ch (str): Here the only two channels requested are channel 1 and channel 2.
                     Channel 1 gives the voltage over the diode and de resistance.
                     Channel 2 gives the voltage over the resistance only.


        Returns:
            float: Gives the real voltage in Volt.
        """

        self.voltage = (self.get_input_value(ch) / 1023) * 3.3

        return self.voltage


def converting_ADC(V_value):
    ADC_value = int((1023 * V_value) / 3.3)

    return ADC_value


print(list_resources())
