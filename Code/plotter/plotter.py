#!/usr/bin/python3
import matplotlib.pyplot as plt
import sys

x = []
y = []
time_sum = 0
time_count = 0

x1 = []
y1 = []
time_sum1 = 0
time_count1 = 0

if len(sys.argv) < 2:
    print(f"Usage: {sys.argv[0]} filename1 [filename2]", file=sys.stderr)
    sys.exit(1)
elif len(sys.argv) == 2:
    filename1 = None
else:
    filename1 = sys.argv[2]

filename = sys.argv[1]

with open(filename, 'rt') as f:
    for line in f.readlines():
        tipe = line.split(' ')[0]
        byte = int(line.split(' ')[1])
        time = int(line.split(' ')[2])
        if (tipe == '[RCLPY]'):
            x.append(byte)
            y.append(time)
            time_sum += time
            time_count += 1
        if (tipe == '[UNIX]' and filename1 == None):
            x1.append(byte)
            y1.append(time)
            time_sum1 += time
            time_count1 += 1

if filename1 != None:
    with open(filename1, 'rt') as f:
        for line in f.readlines():
            tipe = line.split(' ')[0]
            byte = int(line.split(' ')[1])
            time = int(line.split(' ')[2])
            if (tipe == '[RCLPY]'):
                x1.append(byte)
                y1.append(time)
                time_sum1 += time
                time_count1 += 1

plt.figure(1)

plt.subplot(211)
plt.xlabel('Bytes')
plt.ylabel('Time (ns)')
name = filename.split('/')[-1]
plt.title(f'[{name}] ROS2 Latency [RCLPY] AVG: {time_sum/time_count}')
#plt.ylim([0, 700000])     # Set y limit
#plt.xlim([0, 2000000])  # 1048576
plt.plot(x, y)

plt.subplot(212)
plt.xlabel('Bytes')
if filename == None:
    plt.ylabel('Time (ms)')
else:
    plt.ylabel('Time (ns)')
    
if filename1 == None:
    name = filename.split('/')[-1]
else:
    name = filename1.split('/')[-1]
plt.title(f'[{name}] ROS2 Latency [UNIX] AVG: {time_sum1/time_count1}')
#plt.ylim([0, 700])    # Set y limit
#plt.xlim([0, 2000000])
plt.plot(x1, y1)

plt.show()