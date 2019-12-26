#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np

#求解方程x^2+2x+1=0的根

#方程参数列表抽象成一下形式：

ss = [1, -2, 3, -4, -5,-6]

#求解

np.roots(ss)