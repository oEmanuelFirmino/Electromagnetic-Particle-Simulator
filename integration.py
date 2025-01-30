import numpy as np
from particle import Particle
from plotting import plot_trajectory, plot_3d_trajectory


def without_magnetic_field(particle, dt=0.01, t_max=2):
    num_steps = int(t_max / dt)
    r_values = np.zeros((num_steps, 3))
    v_values = np.zeros((num_steps, 3))

    r_values[0] = particle.r0
    v_values[0] = particle.v0

    a = (particle.q / particle.m) * particle.E

    for i in range(1, num_steps):
        v_values[i] = v_values[i - 1] + a * dt
        r_values[i] = r_values[i - 1] + v_values[i - 1] * dt

    plot_trajectory(
        r_values[:, 0], r_values[:, 1], 
    )


def with_magnetic_field(particle, dt=0.01, t_max=2):
    num_steps = int(t_max / dt)
    r_values = np.zeros((num_steps, 3))
    v_values = np.zeros((num_steps, 3))

    r_values[0] = particle.r0
    v_values[0] = particle.v0

    for i in range(1, num_steps):
        v = v_values[i - 1]
        a = (particle.q / particle.m) * (particle.E + np.cross(v, particle.B))

        v_values[i] = v + a * dt
        r_values[i] = r_values[i - 1] + v * dt

    plot_3d_trajectory(r_values)


def runge_kutta(particle, dt=0.01, t_max=2):
    num_steps = int(t_max / dt)
    r_values = np.zeros((num_steps, 3))
    v_values = np.zeros((num_steps, 3))

    r_values[0] = particle.r0
    v_values[0] = particle.v0

    for i in range(1, num_steps):
        r = r_values[i - 1]
        v = v_values[i - 1]

        k1_v = particle.force(v)
        k1_r = v

        k2_v = particle.force(v + 0.5 * dt * k1_v)
        k2_r = v + 0.5 * dt * k1_r

        k3_v = particle.force(v + 0.5 * dt * k2_v)
        k3_r = v + 0.5 * dt * k2_r

        k4_v = particle.force(v + dt * k3_v)
        k4_r = v + dt * k3_r

        r_values[i] = r + (dt / 6) * (k1_r + 2 * k2_r + 2 * k3_r + k4_r)
        v_values[i] = v + (dt / 6) * (k1_v + 2 * k2_v + 2 * k3_v + k4_v)

    plot_3d_trajectory(r_values)
