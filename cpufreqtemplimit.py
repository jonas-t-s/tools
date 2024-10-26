"""
This file is for setting limits to the cpu frequency, when the load is high. (My PC is old and crashes on high temps)
"""
import os
import psutil
from time import sleep


def get_max_cpu_temp():
    temps = psutil.sensors_temperatures()
    cpu_temps = []
    if "coretemp" in temps:
        for temp in temps["coretemp"]:
            cpu_temps.append(temp.current)
        return max(cpu_temps)
    else:
        raise Exception("Coretemp not in temps")


def get_possible_cpu_frequency_range():
    return psutil.cpu_freq().min/1000, psutil.cpu_freq().max/1000


def set_max_cpu_frequency(frequency):
    os.system(f"cpupower frequency-set --max {frequency}GHz")
    pass


def monitor_cpu_temp():
    minfreq, maxfreq = get_possible_cpu_frequency_range()
    curmaxfreq = maxfreq
    while True:
        temp = get_max_cpu_temp()
        if temp > 80:

            set_max_cpu_frequency(max(curmaxfreq/2, minfreq))
            sleep(2)
            curmaxfreq = get_possible_cpu_frequency_range()[1]
        elif temp < 50:
            set_max_cpu_frequency(max(curmaxfreq, maxfreq))
            sleep(2)
            curmaxfreq = get_possible_cpu_frequency_range()[1]
        sleep(40)


if __name__ == "__main__":
    monitor_cpu_temp()
