import streamlit as st

# --- QUANTUM GRID GLOW BACKGROUND (orange-on-black) ---
st.markdown("""
<style>
body {
  background-color: #000000;
  background-image:
    radial-gradient(circle at center, rgba(255,140,0,0.15) 0%, transparent 70%),
    linear-gradient(0deg, rgba(255,140,0,0.05) 1px, transparent 1px),
    linear-gradient(90deg, rgba(255,140,0,0.05) 1px, transparent 1px);
  background-size: cover, 60px 60px, 60px 60px;
  animation: glow 10s infinite alternate ease-in-out;
}
@keyframes glow {
  0% {background-color: #000000;}
  100% {background-color: #0a0500;}
}
div[data-testid="stAppViewContainer"] {
  background: radial-gradient(circle at center, rgba(255,165,0,0.08) 0%, rgba(0,0,0,1) 100%);
  color: #ffb347;
}
@keyframes float {
  0% {transform: translateY(0px);}
  50% {transform: translateY(-5px);}
  100% {transform: translateY(0px);}
}
.dot {
  position: absolute;
  background: rgba(255,165,0,0.7);
  border-radius: 50%;
  width: 8px;
  height: 8px;
  box-shadow: 0 0 10px rgba(255,140,0,0.7);
  animation: float 4s ease-in-out infinite;
}
.dot:nth-child(1){top:20%;left:30%;animation-delay:0s;}
.dot:nth-child(2){top:40%;left:70%;animation-delay:1.5s;}
.dot:nth-child(3){top:70%;left:50%;animation-delay:3s;}
.dot:nth-child(4){top:80%;left:10%;animation-delay:2s;}
.dot:nth-child(5){top:10%;left:80%;animation-delay:1s;}
</style>

<div class="dot"></div>
<div class="dot"></div>
<div class="dot"></div>
<div class="dot"></div>
<div class="dot"></div>
""", unsafe_allow_html=True)

# --- HEADER ---
st.markdown("""
<h1 style='text-align:center;
           color:#ffa500;
           text-shadow:0 0 20px #ff8c00;
           font-family:"Orbitron",sans-serif;
           letter-spacing:2px;'>
Quantum Grid Glow Demo
</h1>
""", unsafe_allow_html=True)

st.write(" This is your new high-tech quantum-style app background.")
