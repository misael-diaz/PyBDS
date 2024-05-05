#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PyBDS                                             May 05, 2024

source: main.py
author: @misael-diaz

Synopsis:
Implements a minimal Brownian Dynamics Simulator for spheres.

Copyright (c) 2024 Misael Díaz-Maldonado
Copyright (c) 2024 UCF-Research Group
This file is released under the GNU General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

References:
[0] R Johansson, Numerical Python: Scientific Computing and Data
    Science Applications with NumPy, SciPy, and Matplotlib, 2nd edition.
[1] MP Allen and DJ Tildesley, Computer Simulation of Liquids.
[2] S Kim and S Karrila, Microhydrodynamics.
"""

# initializes the position vector components of the sphere
x = 0
y = 0
z = 0

# initializes the Brownian force acting on the sphere
F_x = 0
F_y = 0
F_z = 0
