import numpy as np


def buck_duty_cycle(Vo, Vin):
    Dt_buck = np.divide(int(Vo), int(Vin))
    return Dt_buck


def boost_duty_cycle(Vo, Vin):
    Dt_boost = np.divide(np.subtract(int(Vo), int(Vin)), int(Vo))
    return Dt_boost
