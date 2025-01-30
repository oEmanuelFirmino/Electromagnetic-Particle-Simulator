import streamlit as st
import numpy as np
from particle import Particle
from integration import without_magnetic_field, with_magnetic_field, runge_kutta

def interactive_simulation():
    st.title("Simulação de Movimento de Partícula sob Campos Elétrico e Magnético")

    q = st.number_input("Carga (q) da partícula (C)", value=1e-6)
    m = st.number_input("Massa (m) da partícula (kg)", value=1e-3)
    E = st.text_input(
        "Campo elétrico E (em 3 componentes separados por vírgula)", "0, 0, 1"
    )
    B = st.text_input(
        "Campo magnético B (em 3 componentes separados por vírgula)", "0, 0, 1"
    )
    v0 = st.text_input(
        "Velocidade inicial v0 (em 3 componentes separados por vírgula)", "1, 0, 0"
    )
    r0 = st.text_input(
        "Posição inicial r0 (em 3 componentes separados por vírgula)", "0, 0, 0"
    )

    E = np.array(list(map(float, E.split(","))))
    B = np.array(list(map(float, B.split(","))))
    v0 = np.array(list(map(float, v0.split(","))))
    r0 = np.array(list(map(float, r0.split(","))))

    particle = Particle(q, m, E, B, v0, r0)

    simulation_type = st.radio(
        "Escolha o tipo de simulação:",
        ("Sem campo magnético", "Com campo magnético", "Método de Runge-Kutta"),
    )

    if simulation_type == "Sem campo magnético":
        st.write("Simulação com campo elétrico uniforme (sem campo magnético)")
        without_magnetic_field(particle)
    elif simulation_type == "Com campo magnético":
        st.write("Simulação com campos elétrico e magnético")
        with_magnetic_field(particle)
    elif simulation_type == "Método de Runge-Kutta":
        st.write("Simulação usando o método de Runge-Kutta")
        runge_kutta(particle)


if __name__ == "__main__":
    interactive_simulation()
