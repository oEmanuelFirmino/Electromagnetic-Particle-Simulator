import matplotlib.pyplot as plt
import streamlit as st
import plotly.graph_objects as go


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
    fig = go.Figure(
        data=[
            go.Scatter3d(
                x=r_values[:, 0],
                y=r_values[:, 1],
                z=r_values[:, 2],
                mode="lines",
                marker=dict(size=4, color="orange"),
            )
        ]
    )

    fig.update_layout(
        title="Movimento sob Campo Eletromagnético",
        scene=dict(
            xaxis_title="Posição x (m)",
            yaxis_title="Posição y (m)",
            zaxis_title="Posição z (m)",
        ),
        autosize=True,
    )

    st.plotly_chart(fig)
