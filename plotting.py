import matplotlib.pyplot as plt
import streamlit as st


def plot_trajectory(x, y, title):
    plt.figure(figsize=(8, 6))
    plt.plot(x, y, label="Trajetória da Partícula")
    plt.xlabel("Posição x (m)")
    plt.ylabel("Posição y (m)")
    plt.title(title)
    plt.legend()
    plt.grid()
    st.pyplot(plt)


def plot_3d_trajectory(r_values):
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection="3d")
    ax.plot(
        r_values[:, 0], r_values[:, 1], r_values[:, 2], label="Trajetória da Partícula"
    )

    ax.set_xlabel("Posição x (m)")
    ax.set_ylabel("Posição y (m)")
    ax.set_zlabel("Posição z (m)")
    ax.set_title("Movimento sob Campo Eletromagnético")
    ax.legend()
    st.pyplot(fig)
