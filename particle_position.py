import numpy as np
import matplotlib.pyplot as plt


class Particle:
    def __init__(self, q, m, E, B, v0, r0):
        self.q = q
        self.m = m
        self.E = np.array(E)
        self.B = np.array(B)
        self.v0 = np.array(v0)
        self.r0 = np.array(r0)

    def without_magnetic_field(self, dt=0.01, t_max=2):
        num_steps = int(t_max / dt)

        t_values = np.linspace(0, t_max, num_steps)
        r_values = np.zeros((num_steps, 3))
        v_values = np.zeros((num_steps, 3))

        r_values[0] = self.r0
        v_values[0] = self.v0

        a = (self.q / self.m) * self.E

        for i in range(1, num_steps):
            v_values[i] = v_values[i - 1] + a * dt  # Atualiza velocidade
            r_values[i] = r_values[i - 1] + v_values[i - 1] * dt  # Atualiza posição

        plt.figure(figsize=(8, 6))
        plt.plot(r_values[:, 0], r_values[:, 1], label="Trajetória da Partícula")
        plt.xlabel("Posição x (m)")
        plt.ylabel("Posição y (m)")
        plt.title("Movimento sob Campo Elétrico Uniforme")
        plt.legend()
        plt.grid()
        plt.show()

    def with_magnetic_field(self, dt=0.01, t_max=2):
        num_steps = int(t_max / dt)

        t_values = np.linspace(0, t_max, num_steps)
        r_values = np.zeros((num_steps, 3))
        v_values = np.zeros((num_steps, 3))

        r_values[0] = self.r0
        v_values[0] = self.v0

        for i in range(1, num_steps):
            v = v_values[i - 1]

            a = (self.q / self.m) * (self.E + np.cross(v, self.B))

            v_values[i] = v + a * dt
            r_values[i] = r_values[i - 1] + v * dt

        fig = plt.figure(figsize=(8, 6))
        ax = fig.add_subplot(111, projection="3d")
        ax.plot(
            r_values[:, 0],
            r_values[:, 1],
            r_values[:, 2],
            label="Trajetória da Partícula",
        )

        ax.set_xlabel("Posição x (m)")
        ax.set_ylabel("Posição y (m)")
        ax.set_zlabel("Posição z (m)")
        ax.set_title("Movimento sob Campo Eletromagnético")
        ax.legend()
        plt.show()

    def force(self, v):
        return (self.q / self.m) * (self.E + np.cross(v, self.B))

    def runge_kutta(self, dt=0.01, t_max=2):
        num_steps = int(t_max / dt)

        t_values = np.linspace(0, t_max, num_steps)
        r_values = np.zeros((num_steps, 3))
        v_values = np.zeros((num_steps, 3))

        r_values[0] = self.r0
        v_values[0] = self.v0

        for i in range(1, num_steps):
            r = r_values[i - 1]
            v = v_values[i - 1]

            k1_v = self.force(v)
            k1_r = v

            k2_v = self.force(v + 0.5 * dt * k1_v)
            k2_r = v + 0.5 * dt * k1_r

            k3_v = self.force(v + 0.5 * dt * k2_v)
            k3_r = v + 0.5 * dt * k2_r

            k4_v = self.force(v + dt * k3_v)
            k4_r = v + dt * k3_r

            r_values[i] = r + (dt / 6) * (k1_r + 2 * k2_r + 2 * k3_r + k4_r)
            v_values[i] = v + (dt / 6) * (k1_v + 2 * k2_v + 2 * k3_v + k4_v)

        fig = plt.figure(figsize=(8, 6))
        ax = fig.add_subplot(111, projection="3d")
        ax.plot(
            r_values[:, 0],
            r_values[:, 1],
            r_values[:, 2],
            label="Trajetória da Partícula",
        )

        ax.set_xlabel("Posição x (m)")
        ax.set_ylabel("Posição y (m)")
        ax.set_zlabel("Posição z (m)")
        ax.set_title("Movimento sob Campo Eletromagnético (RK4)")
        ax.legend()
        plt.show()


particula = Particle(
    q=1.0,
    m=1.0,
    E=[0, 10, 0],
    B=[0, 0, 1],
    v0=[5, 0, 0],
    r0=[0, 0, 0],
)

# Escolha a função que deseja chamar:
# Para movimento sem campo magnético:
particula.without_magnetic_field()

# Para movimento com campo magnético:
# particula.with_magnetic_field()

# Para movimento com o método de Runge-Kutta:
# particula.runge_kutta()
