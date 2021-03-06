# -*- coding: utf-8 -*-
"""

Embry-Riddle Aeronautical University
@author: Nicolas Gachancipa

Preliminary Orbit Determination - Ground-based measurements
"""
# Imports
import numpy as np
import math as mt
from math import cos, sin

# Inputs
rho = 668.3
sigma = 62.5
beta = 135.4
rho_der = 2.39
sigma_der = -0.65
beta_der = -0.38
phi = 42.9
gamma = 240.7
planet_radius = 6378    # in Km. (6378 for earth)
location_altitude = 0   # in Km. (0 at sea level).
planet_rotation = 4.178e-3  # in deg/s (4.178e-3 for earth)

# Convert values to radians.
sigma, beta = sigma*mt.pi/180, beta*mt.pi/180
sigma_der, beta_der = sigma_der*mt.pi/180, beta_der*mt.pi/180 
phi *= mt.pi/180
gamma *= mt.pi/180
planet_rotation *= mt.pi/180

# Compute position values in Tropospheric Horizon Frame (SEZ).
rho_s = -rho*cos(sigma)*cos(beta)
rho_e = rho*cos(sigma)*sin(beta)
rho_z = rho*sin(sigma)

# Compute velocity values in SEZ.
rho_s_der = (-rho_der*cos(sigma)*cos(beta) + 
            rho*sigma_der*sin(sigma)*cos(beta) + 
            rho*beta_der*cos(sigma)*sin(beta)) 
rho_e_der = (rho_der*cos(sigma)*sin(beta) -
            rho*sigma_der*sin(sigma)*sin(beta) +
            rho*beta_der*cos(sigma)*cos(beta))
rho_z_der = (rho_der*sin(sigma) + rho*sin(sigma_der)*cos(sigma))

# Commpute r site and rho vectors.
r_site_vec = np.array([0, 0, planet_radius + location_altitude])
rho_vec = np.array([rho_s, rho_e, rho_z])
rho_vec_der = np.array([rho_s_der, rho_e_der, rho_z_der])

# Define transformation matrix from ECI to SEZ. 
rot_1 = np.array([[sin(phi), 0, -cos(phi)], 
                  [0, 1, 0], 
                  [cos(phi), 0, sin(phi)]])
rot_2 = np.array([[cos(gamma), sin(gamma), 0], 
                  [-sin(gamma), cos(gamma), 0], 
                  [0, 0, 1]])
rot_ECI_to_SEZ = np.dot(rot_1, rot_2)
rot_SEZ_to_ECI = rot_ECI_to_SEZ.T

# Obtain r_site_vec, rho_vec, and rho_vec_der in ECI frame.
r_site_vec_ECI = np.dot(rot_SEZ_to_ECI, r_site_vec)
rho_vec_ECI = np.dot(rot_SEZ_to_ECI, rho_vec)
rho_vec_der_ECI = np.dot(rot_SEZ_to_ECI, rho_vec_der)

# Obtain position and velocity vectors in ECI frame.
r_ECI = r_site_vec_ECI + rho_vec_ECI
v_ECI = (rho_vec_der_ECI + 
         np.cross(np.array([0, 0, planet_rotation]), rho_vec_ECI) + 
         np.cross(np.array([0, 0, planet_rotation]), r_site_vec_ECI))

# Print solutions.
print('R (ECI frame): ', r_ECI)
print('V (ECI frame): ', v_ECI)
