"""
Filename: deviceParallel.py
Author: Cooper Parlee <cooper.parlee@mma.edu>
Date: 01-03-2026
Description: Basic test of the engine using the fabled magic node.
"""

from src.nodes.nodeManager import NodeManager
from src.nodes.magicNode import MagicNode

from time import sleep

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from collections import deque
import threading

nodeManager = NodeManager()
magicNode = MagicNode(0)
nodeManager.addNode(magicNode)

x_data = deque(maxlen=150)
y_data = deque(maxlen=150)

fig, ax = plt.subplots()
line, = ax.plot([], [], lw=2)
ax.set_ylim(-1, 1)
ax.set_xlim(0, 10)

def update():
    while (True):
        nodeManager.update()
        
        sleep(0.05)

def updateGraph(frame):
    timeSinceStart = magicNode.getTimeSinceStart()

    x_data.append(timeSinceStart)
    y_data.append(magicNode.getTemperature())

    line.set_data(list(x_data), list(y_data))

    if(timeSinceStart > 10):
        ax.set_xlim(timeSinceStart - 10, timeSinceStart)
    return line,

simulationThread = threading.Thread(target=update, daemon=True)
simulationThread.start()

pltAnimation = animation.FuncAnimation(fig, updateGraph, interval=100, blit=False)

plt.show(block=True)


