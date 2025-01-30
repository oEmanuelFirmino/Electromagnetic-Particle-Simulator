# Electromagnetic Particle Simulator

## Overview

The **Electromagnetic Particle Simulator** is a Python-based interactive application that simulates the motion of charged particles in electric and magnetic fields. This tool provides a practical way to visualize the effects of electromagnetic fields on particle trajectories, using multiple simulation methods. It's designed for educational purposes, helping users explore fundamental concepts in electromagnetism and numerical methods.

## Features

- Simulate the motion of charged particles in:
  - Electric Field (with or without a magnetic field)
  - Magnetic Field (affecting the particle's trajectory due to the Lorentz force)
  - Runge-Kutta Method (for more accurate trajectory calculations)
- Adjustable particle properties:
  - Charge (q)
  - Mass (m)
  - Initial Position (r₀)
  - Initial Velocity (v₀)
- Interactive input through Streamlit interface for real-time simulation customization

## Physical Concepts

This simulator is based on classical electromagnetism, governed by the following principles:

### Lorentz Force

The motion of a charged particle under the influence of electric and magnetic fields is described by the Lorentz force equation:

```math
\vec{F} = q(\vec{E} + \vec{v} \times \vec{B})
```

Where:

- F⃗ is the force exerted on the particle
- q is the charge of the particle
- E⃗ is the electric field vector
- v⃗ is the velocity vector of the particle
- B⃗ is the magnetic field vector

### Equations of Motion

The equations of motion for the particle are derived from Newton's second law:

```math
\vec{a} = \frac{\vec{F}}{m} = \frac{q}{m}(\vec{E} + \vec{v} \times \vec{B})
```

Where:

- a⃗ is the acceleration of the particle
- m is the mass of the particle

## Mathematical Methods

### 1. Basic Electric Field Simulation

When only an electric field is present, the particle's motion follows:

```math
\vec{r}(t) = \vec{r}_0 + \vec{v}_0t + \frac{1}{2}\frac{q\vec{E}}{m}t^2
```

```math
\vec{v}(t) = \vec{v}_0 + \frac{q\vec{E}}{m}t
```

### 2. Electromagnetic Field Simulation

With both electric and magnetic fields, the motion becomes more complex and requires numerical integration of:

```math
\frac{d\vec{r}}{dt} = \vec{v}
```

```math
\frac{d\vec{v}}{dt} = \frac{q}{m}(\vec{E} + \vec{v} \times \vec{B})
```

### 3. Runge-Kutta Method

The 4th-order Runge-Kutta method solves these equations using:

```math
\vec{y}_{n+1} = \vec{y}_n + \frac{h}{6}(k_1 + 2k_2 + 2k_3 + k_4)
```

Where:

- h is the time step
- k₁, k₂, k₃, k₄ are the intermediate slopes
- y⃗ represents both position and velocity vectors

## Code Structure

### 1. Particle Class

```python
class Particle:
    def __init__(self, q, m, E, B, r0, v0):
        self.q = q      # Charge
        self.m = m      # Mass
        self.E = E      # Electric field
        self.B = B      # Magnetic field
        self.r = r0     # Initial position
        self.v = v0     # Initial velocity
```

### 2. Integration Methods

- `without_magnetic_field(particle)`: Electric field only simulation
- `with_magnetic_field(particle)`: Full electromagnetic simulation
- `runge_kutta(particle)`: Advanced numerical integration

### 3. Visualization

- 2D and 3D trajectory plotting using Matplotlib
- Interactive controls through Streamlit interface

## Setup and Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/Electromagnetic-Particle-Simulator.git
cd Electromagnetic-Particle-Simulator
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the application:

```bash
streamlit run main.py
```

### Requirements

- Python 3.x
- NumPy
- Matplotlib
- Streamlit

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for improvements and bug fixes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
