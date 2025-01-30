import streamlit as st
import numpy as np
from particle import Particle
from integration import without_magnetic_field, with_magnetic_field, runge_kutta


def interactive_simulation():
    st.title("Simulação de Movimento de Partícula sob Campos Elétrico e Magnético")

    q = st.number_input("Carga (q) da partícula (C)", value=1e-6)
    m = st.number_input("Massa (m) da partícula (kg)", value=1e-3)

    input_method = st.radio(
        "Escolha o tipo de input para os campos elétrico e magnético:",
        ("Texto", "Slider"),
    )

    if input_method == "Texto":
        E = st.text_input(
            "Campo elétrico E (em 3 componentes separados por vírgula)", "0, 0, 1"
        )
        B = st.text_input(
            "Campo magnético B (em 3 componentes separados por vírgula)", "0, 0, 1"
        )

        try:
            E = np.array([float(x.strip()) for x in E.split(",")])
            B = np.array([float(x.strip()) for x in B.split(",")])  # O mesmo para B
        except ValueError:
            st.error(
                "Por favor, insira os campos elétrico e magnético no formato correto (exemplo: 0, 0, 1)"
            )

    elif input_method == "Slider":
        E1 = st.slider("Campo Elétrico E1", -10.0, 10.0, 0.0)
        E2 = st.slider("Campo Elétrico E2", -10.0, 10.0, 0.0)
        E3 = st.slider("Campo Elétrico E3", -10.0, 10.0, 1.0)
        B1 = st.slider("Campo Magnético B1", -10.0, 10.0, 0.0)
        B2 = st.slider("Campo Magnético B2", -10.0, 10.0, 0.0)
        B3 = st.slider("Campo Magnético B3", -10.0, 10.0, 1.0)
        E = np.array([E1, E2, E3])
        B = np.array([B1, B2, B3])

    v0_method = st.radio(
        "Escolha o tipo de input para a velocidade inicial:", ("Texto", "Slider")
    )

    if v0_method == "Texto":
        v0 = st.text_input(
            "Velocidade inicial v0 (em 3 componentes separados por vírgula)", "1, 0, 0"
        )
        try:
            v0 = np.array([float(x.strip()) for x in v0.split(",")])
        except ValueError:
            st.error(
                "Por favor, insira a velocidade inicial no formato correto (exemplo: 1, 0, 0)"
            )

    elif v0_method == "Slider":
        v0x = st.slider("Velocidade inicial Vx", -10.0, 10.0, 1.0)
        v0y = st.slider("Velocidade inicial Vy", -10.0, 10.0, 0.0)
        v0z = st.slider("Velocidade inicial Vz", -10.0, 10.0, 0.0)
        v0 = np.array([v0x, v0y, v0z])

    r0_method = st.radio(
        "Escolha o tipo de input para a posição inicial:", ("Texto", "Slider")
    )

    if r0_method == "Texto":
        r0 = st.text_input(
            "Posição inicial r0 (em 3 componentes separados por vírgula)", "0, 0, 0"
        )
        try:
            r0 = np.array([float(x.strip()) for x in r0.split(",")])
        except ValueError:
            st.error(
                "Por favor, insira a posição inicial no formato correto (exemplo: 0, 0, 0)"
            )

    elif r0_method == "Slider":
        r0x = st.slider("Posição inicial X", -10.0, 10.0, 0.0)
        r0y = st.slider("Posição inicial Y", -10.0, 10.0, 0.0)
        r0z = st.slider("Posição inicial Z", -10.0, 10.0, 0.0)
        r0 = np.array([r0x, r0y, r0z])

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
