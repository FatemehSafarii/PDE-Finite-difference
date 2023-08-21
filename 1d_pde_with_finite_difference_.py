# -*- coding: utf-8 -*-
"""1D PDE with Finite difference .ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QTJwswIMEcVMpEd1FxampQNOnHg1mx8U
"""

import numpy as np
import matplotlib.pyplot as plt


L = 1.0  # Length of the domain
T = 0.1  # Total time
nx = 100  # Number of grid points in the x direction
nt = 1000  # Number of time steps
alpha = 0.1  # Diffusion coefficient

# Calculate the grid spacing and time step
dx = L / (nx - 1)
dt = T / nt


x = np.linspace(0.0, L, nx)


u = np.zeros(nx)


u[:] = 1.0  # Initial value of u(x, 0)

# Get the PDE equation from the user
pde_equation = input("Enter the 1D PDE equation: ")


for n in range(nt):
    un = u.copy()

    # Update the solution at the this time step
    for i in range(1, nx - 1):
        eval_result = eval(pde_equation)
        u[i] = un[i] + eval_result * dt

# Plot the final solution
plt.plot(x, u)
plt.xlabel('x')
plt.ylabel('u(x, t=T)')
plt.title('Solution of the 1D Diffusion Equation using FDM')
plt.show()