#!/usr/bin/python3
import matplotlib.pyplot as plt
from math import log2

x = []
y = []
time_sum = 0
time_count = 0

x1 = []
y1 = []
time_sum1 = 0
time_count1 = 0

with open('output', 'rt') as f:
    for line in f.readlines():
        tipe = line.split(' ')[0]
        byte = log2(int(line.split(' ')[1]))
        time = int(line.split(' ')[2])
        if (tipe == '[RCLPY]'):
            x.append(byte)
            y.append(time)
            time_sum += time
            time_count += 1
        if (tipe == '[UNIX]'):
            x1.append(byte)
            y1.append(time)
            time_sum1 += time
            time_count1 += 1

plt.figure(1)

plt.subplot(211)
plt.xlabel('Bytes')
plt.ylabel('Time')
plt.title(f'ROS2 Latency [RCLPY] AVG: {time_sum/time_count}')
plt.plot(x, y)

plt.subplot(212)
plt.xlabel('Bytes')
plt.ylabel('Time')
plt.title(f'ROS2 Latency [UNIX] AVG: {time_sum1/time_count1}')
plt.plot(x1, y1)

plt.show()