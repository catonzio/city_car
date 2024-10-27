from dataclasses import dataclass


@dataclass
class CarKeysParams:
    delta_acceleration: float
    delta_steer: float
    