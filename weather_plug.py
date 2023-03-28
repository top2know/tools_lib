import numpy as np


def get_temperature():
    return {'temp': np.random.randint(-20, 30)}


def get_weekly_forecast():
    return {'temps': np.random.randint(-20, 30, 7)}