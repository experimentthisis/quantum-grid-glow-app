import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.special import hermite, factorial

# ---------- BACKGROUND VIDEO ----------
st.markdown("""
<style>
[data-testid="stAppViewContainer"] {
  position: relative;
  overflow: hidden;
}

/* Fullscreen looping video background */
video#bgvid {
  position: fixed;
  right: 0;
  bottom: 0;
  min-width: 100%;
  min-height: 100%;
  z-index: -1;
  object-fit: cover;
  filter: brightness(0.45) blur(1px);
}
</style>

<video autoplay muted loop id="bgvid">
  <source src="wave.mp4" type="video/mp4">
</video>
""", unsafe_allow_html=True)

# ---------- HEADER ----------
st.markdown("<h1 style='text-align:center; color:#FFA500;'>Quantum Systems Visualizer</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#E0E0E0;'>An interactive exploration of quantum mechanical models and their visual representations.</p>", unsafe_allow_html=True)
st.markdown("---")

# ---------- SECTION 1: Quantum Harmonic Oscillator ----------
st.markdown("<h2 style='color:#00FFAA;'>⚙️ Quantum Harmonic Oscillator</h2>", unsafe_allow_html=True)
st.write("Visualize the probability density function of a particle in a harmonic potential well for different energy levels.")

n = st.slider("Select energy level n", 0, 10, 0)
x = np.linspace(-5, 5, 1000)
psi_n = (1.0/np.sqrt(2.0**n * factorial(n) * np.sqrt(np.pi))) * np.exp(-x**2/2) * hermite(n)(x)
prob_density = np.abs(psi_n)**2

fig, ax = plt.subplots()
ax.plot(x, prob_density, color='#FFA500', linewidth=2)
ax.set_xlabel('Position (x)')
ax.set_ylabel('|ψ(x)|²')
ax.set_title(f'Quantum Harmonic Oscillator Probability Density (n={n})', color='white')
ax.set_facecolor("black")
st.pyplot(fig)

st.markdown("---")

# ---------- SECTION 2: Ballistic Expansion of a Condensate ----------
st.markdown("<h2 style='color:#00FFAA;'>🌀 Ballistic Expansion of a Condensate</h2>", unsafe_allow_html=True)
st.write("""
When a trapped Bose–Einstein condensate is released, it expands freely.
The phase of the condensate evolves parabolically over time,
and the scaling parameters describe its axial and radial size.
""")
st.latex(r"b_{\perp} = \sqrt{1 + \tau^2}, \quad b_{\parallel} = 1 + \lambda^2(\tau \arctan(\tau) - \ln\sqrt{1 + \tau^2})")

st.markdown("---")

# ---------- SECTION 3: Particle in a Box ----------
st.markdown("<h2 style='color:#00FFAA;'>📦 Particle in a Box</h2>", unsafe_allow_html=True)
st.write("""
Another foundational quantum model where a particle is confined within
an infinite potential well. You can visualize its stationary wave functions.
""")

# Simple static figure placeholder
x_box = np.linspace(0, 1, 1000)
n_box = 1
psi_box = np.sqrt(2) * np.sin(n_box * np.pi * x_box)
fig2, ax2 = plt.subplots()
ax2.plot(x_box, psi_box**2, color='#00FFAA')
ax2.set_title("Particle in a Box |ψ(x)|²", color='white')
ax2.set_facecolor("black")
st.pyplot(fig2)

st.markdown("---")

# ---------- REFERENCES ----------
st.markdown("""
<h3 style='color:#FFA500;'>📚 References</h3>
<ul style='color:#E0E0E0;'>
<li>Heidelberg Lecture Notes on Bose–Einstein Condensates (2020)</li>
<li>Gross–Pitaevskii Theory – Background Materials (PDF, Dr. S. Chowdhury)</li>
<li>Castin & Dum, PRL 77, 5316 (1996)</li>
</ul>
""", unsafe_allow_html=True)

st.markdown("<p style='text-align:center; color:gray; font-size:12px;'>Developed by Naimah Ishaque | University of Windsor</p>", unsafe_allow_html=True)
