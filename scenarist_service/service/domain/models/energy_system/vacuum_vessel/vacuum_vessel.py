from service.utils.json_serializable import IJsonSerializable


class VacuumVessel(IJsonSerializable):
    def __init__(self, name: str = "vacuum_vessel") -> None:
        self.name = name

        self.is_on = False
        self.alarm = False
        self.durability = 100.0

        self.pressure = 0.0
        self.input_current = 0.0
        self.input_voltage = 0.0
        self.input_power = 0.0

    def start(self) -> None:
        self.is_on = True

    is_on: bool
    alarm: bool

    durability: float

    pressure: float

    input_current: float
    input_voltage: float
    input_power: float
