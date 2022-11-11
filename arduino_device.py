# excersize 3.5 
import pyvisa

# vraagt poort aan
def list_devices():
    rm = pyvisa.ResourceManager("@py")
    ports = rm.list_resources()
    print(ports)
    return ports

class ArduinoVISADevice:

    # define device
    def __init__(self, port):
        rm = pyvisa.ResourceManager("@py")
        self.device = rm.open_resource(port, read_termination = "\r\n", write_termination="\n")
        return
    
    def get_identification(self):
        return self.device.query("*IDN?")

    def set_output_value(self,value):
        return self.device.query(f"OUT:CH0 {value}")

    def get_output_value(self):
        return self.device.query(f"OUT:CH0?")

    def get_input_value(self, channel): 
        return self.device.query(f"MEAS:CH{channel}?")

    def get_input_voltage(self, channel): 
        return (float(self.device.query(f"MEAS:CH{channel}?"))) *(3.3 / (1023))

