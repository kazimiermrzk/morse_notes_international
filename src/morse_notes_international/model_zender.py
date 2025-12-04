import numpy as np
from morse_notes_international.arduino_zender import (
    ArduinoVISADevice,
    list_resources,
    converting_ADC,
)  # noqa
# from pythondaq.cli import scan


class DiodeExperiment:
    """Collecting data from diode lamp."""

    def __init__(self, port):
        """Initializes the instance for our arduino.


        This method initializes multiple lists containing data and errors during operation of the
        arduino.

        args:
            U_error_list: Contains the error values on the measured voltage.
            I_error_list: Contains the error values on the measured current.
            U_mean_diode_list: Contains the average values on the measured voltage over multiple
                               executed experiments.
            I_mean_diode_list: Contains the average values on the measured current over multiple
                               executed experiments.
            device: Activates the arduino by opening the port 'ASRL10::INSTR'.


        """

        self.U_error_list = []
        self.I_error_list = []

        self.U_mean_diode_list = []
        self.I_mean_list = []
        self.device = ArduinoVISADevice(port=port)

    def scan(self, start, stop, repeat):
        """Executing the experiment multiple times.

        Here, we run the experiment 3 times for every ADC value. This also calles the turtle method.

        All calculated values are stored in the instance's mean and error lists.

        Returns:
           U_mean_diode_list (float): list of mean voltage values (Volts).
           I_mean_list (float): List of mean current values (Àmpere).
           U_error_list (float): List of error voltage values.
           I_error_list (float): List of error current values.
        """

        resistance = 220  # ohm
        ADC_start = converting_ADC(start)
        ADC_stop = converting_ADC(stop)

        for ADC in range(ADC_start, ADC_stop + 1):
            U_repeat_list = []
            I_repeat_list = []

            for _ in range(0, repeat):
                self.device.set_output_value(ADC)

                voltage_ch2 = self.device.get_input_voltage(ch=2)

                voltage_diode = self.device.get_input_voltage(
                    ch=1
                ) - self.device.get_input_voltage(ch=2)

                current = voltage_ch2 / resistance

                I_repeat_list.append(current)
                U_repeat_list.append(voltage_diode)

            U_error = np.std(U_repeat_list) / np.sqrt(repeat)
            I_error = np.std(I_repeat_list) / np.sqrt(repeat)

            self.U_error_list.append(U_error)
            self.I_error_list.append(I_error)

            U_mean = np.mean(U_repeat_list)
            I_mean = np.mean(I_repeat_list)

            self.U_mean_diode_list.append(U_mean)
            self.I_mean_list.append(I_mean)

        self.device.set_output_value(0)

        return (
            self.U_mean_diode_list,
            self.I_mean_list,
            self.U_error_list,
            self.I_error_list,
        )

    def identification(self):
        a = self.device.get_identification()
        return a
