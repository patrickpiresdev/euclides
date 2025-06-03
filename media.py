import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Configurações da circunferência
raio = 1
num_pontos = 10  # quanto maior, mais suave a circunferência

# Geração dos ângulos em sentido anti-horário (trigonométrico)
theta = np.linspace(0, 2 * np.pi, num_pontos)

# Coordenadas da circunferência completa
x = raio * np.cos(theta)
y = raio * np.sin(theta)

# Setup da figura
fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.set_xlim(-1.1 * raio, 1.1 * raio)
ax.set_ylim(-1.1 * raio, 1.1 * raio)

# Linha que será atualizada
linha, = ax.plot([], [], 'b', lw=2)

# Função de inicialização
def init():
    linha.set_data([], [])
    return linha,

# Função de atualização da animação
def update(frame):
    linha.set_data(x[:frame], y[:frame])
    return linha,

# Criação da animação
ani = FuncAnimation(fig, update, frames=num_pontos, init_func=init,
                    interval=20, blit=True)

plt.show()
