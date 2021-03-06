#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

# Create data
x = np.arange(0, 6, 0.1)
y1 = np.sin(x)
y2 = np.cos(x)

# Draw graph
plt.plot(x, y1, label="sin")
plt.plot(x, y2, linestyle = "--", label="cos")
plt.xlabel("x") # label of X axis
plt.ylabel("y") # label of Y axis
plt.title('sin & cos')
plt.legend()
plt.show()
