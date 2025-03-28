from bisect import bisect_right

# Intervals of AQI following the PM 2.5 as the parameter
pm_aqi_intervals = [
    (0.0, 12.0, 0, 50, "good"),
    (12.1, 35.4, 51, 100, "moderate"),
    (35.5, 55.4, 101, 150, "unhealthy-for-sensitive-groups"),
    (55.5, 150.4, 151, 200, "unhealthy"),
    (150.5, 250.4, 201, 300, "very-unhealthy"),
    (250.5, 500.4, 301, 500, "hazardous"),
]


def classify_value(value: float) -> tuple:
    """
    Function to classify value according to AQI intervals
    using the PM 2.5 concentration as a parameter.

    The function receives a PM 2.5 concentration parameter
    and returns a tuple with an interval range that contains the
    value received.
    """
    bounds = [interval[1] for interval in pm_aqi_intervals]

    if value < pm_aqi_intervals[0][0]:
        return pm_aqi_intervals[0]

    if value > pm_aqi_intervals[-1][1]:
        return pm_aqi_intervals[-1]

    idx = bisect_right(bounds, value)
    return pm_aqi_intervals[idx]


def calc_aqi(pm: float) -> tuple[int, str]:
    """
    Function to calculate the AQI value according to a PM 2.5 parameter.

    The function receives the PM 2.5 concentration value as a parameter
    and return the AQI value calculated.
    """
    classification = classify_value(pm)

    low_c, high_c = classification[0], classification[1]
    low_i, high_i = classification[2], classification[3]

    variation = (high_i - low_i) / (high_c - low_c)

    aqi = variation * (float(pm) - low_c) + low_i

    return (int(aqi), classification[4])
