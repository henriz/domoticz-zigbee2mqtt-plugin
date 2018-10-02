import Domoticz
from devices.device import Device

class TemperatureSensor(Device):
    def create_device(self, unit, device_name, options, message):
        return Domoticz.Device(Name=device_name, Unit=unit, TypeName="Temperature", Options=options).Create()

    def get_numeric_value(self, value, device):
        return 0

    def get_string_value(self, value, device):
        return str(value)

    