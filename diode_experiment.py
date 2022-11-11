import matplotlib.pyplot as plt
from arduino_device import ArduinoVISADevice, list_devices

class DiodeExperiment:

    def __init__(self, port):
        self.device = ArduinoVISADevice(port = port)
        return

    def scan(self, start, stop): 

        # oude code 
        # The list for the voltages in the stroomkring with unit Volt
        voltages_U0 = []
        voltages_U1 = []
        voltages_U2 = []
        voltages_Uled = [] 
        current_led = []

        for i in range(start, stop): 

            # ADC_0 = (device.query(f"OUT:CH0 {i}"))
            ADC_0 = self.device.set_output_value(i)
            U_0 = (int(ADC_0) * 3.3)/1023 
            voltages_U0.append(U_0)

            # measure voltages U_1
            # ADC_1 = (device.query(f"MEAS:CH1?"))
            ADC_1 = self.device.get_input_value(1)
            U_1 = (int(ADC_1) * 3.3)/1023 
            voltages_U1.append(U_1)

            # measure voltages U_2
            #ADC_2 = (device.query(f"MEAS:CH2?"))
            ADC_2 = self.device.get_input_value(2)
            U_2 = (int(ADC_2) * 3.3)/1023 
            voltages_U2.append(U_2)

        # calculate voltages over the LED
        for U_1, U_2 in zip(voltages_U1, voltages_U2):
            U_led = U_1 - U_2 
            voltages_Uled.append(U_led)
        
        # calculate current over the LED, the current over the LED is the same as over the resistance because they are in serie
        for U2 in voltages_U2:
            I_led = U2 / 220
            current_led.append(I_led)

        # plot voltage LED against current LED 
        plt.scatter(voltages_Uled, current_led)
        plt.ylabel("current (A)")
        plt.xlabel("voltage (V)")
        plt.show()

        # LED light off 
        self.device.set_output_value(0)
