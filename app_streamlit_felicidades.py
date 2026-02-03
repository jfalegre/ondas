import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# ======================
# Configuración Streamlit
# ======================
st.set_page_config(
    page_title="Movimiento circular → seno + FELICIDADES",
    layout="wide"
)

st.title("Movimiento circular y proyección seno")
st.subheader("...y algo más...")

# ======================
# Parámetros
# ======================
N_FRAMES = 200
t_vals = np.linspace(0, 1, N_FRAMES)

palabra = "FELICIDADES ANA!!"
n_letras = len(palabra)

# ======================
# Controles
# ======================
col_controls, col_button = st.columns([3, 1])

with col_controls:
    n = st.slider("Frecuencia n", min_value=1, max_value=10, value=1)

#velocidad = st.radio(
   # "Velocidad de la animación",
    #["Lenta", "Normal", "Rápida"],
    #horizontal=True
#)

#if velocidad == "Lenta":
 #   frame_step = 1
#elif velocidad == "Normal":
    frame_step = 4
#else:  # Rápida
 #   frame_step = 10
 

with col_button:
    animate = st.button("Animar")

# ======================
# Contenedor gráfico
# ======================
plot_container = st.empty()

# ======================
# Función de dibujo
# ======================
def draw_frame(frame, n):
    t = t_vals[frame]
    theta = 2 * np.pi * n * t_vals

    x = np.cos(theta[frame])
    y = np.sin(theta[frame])

    # Progreso normalizado
    progreso = frame / (N_FRAMES - 1)

    # Letras a mostrar
    k = int(progreso * n_letras)
    k = min(k, n_letras)
    texto = palabra[:k]

    fig, (ax_circ, ax_sin) = plt.subplots(1, 2, figsize=(9, 4))

    # ---- Circunferencia
    ax_circ.set_aspect("equal")
    ax_circ.set_xlim(-1.3, 1.3)
    ax_circ.set_ylim(-1.8, 1.3)
    ax_circ.add_patch(plt.Circle((0, 0), 1, fill=False, color="gray"))

    ax_circ.plot(
        np.cos(theta[:frame+1]),
        np.sin(theta[:frame+1]),
        "r-",
        alpha=0.4
    )

    ax_circ.plot([0, x], [0, y], "k-", lw=2)
    ax_circ.plot(x, y, "ro")

    ax_circ.set_title(rf"$\theta(t)=2\pi \cdot {n} \cdot t$")

    # Texto FELICIDADES 
    ax_circ.text(
        0, -1.5,
        texto,
        ha="center",
        va="center",
        fontsize=16,
        fontweight="bold",
        color="purple"
    )

    # ---- Seno
    ax_sin.set_xlim(0, 1)
    ax_sin.set_ylim(-1.2, 1.2)
    ax_sin.plot(
        t_vals[:frame+1],
        np.sin(theta[:frame+1]),
        "b-"
    )
    ax_sin.plot(t, y, "ro")
    ax_sin.set_xlabel("t")
    ax_sin.set_ylabel("sin(2πnt)")

    fig.subplots_adjust(wspace=0.35)

    return fig

# ======================
# Animación
# ======================
if animate:
    for frame in range(0, N_FRAMES, 10):
        fig = draw_frame(frame, n)
        plot_container.pyplot(fig)
        plt.close(fig)

    # Forzar último frame (t = 1 y palabra completa)
    fig = draw_frame(N_FRAMES - 1, n)
    plot_container.pyplot(fig)
    plt.close(fig)

else:
    fig = draw_frame(0, n)
    plot_container.pyplot(fig)
    plt.close(fig)
