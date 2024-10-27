from dataclasses import dataclass


@dataclass
class CarKeysParams:
    acceleration: float
    handbrake: float
    steer: float
    retro: bool
