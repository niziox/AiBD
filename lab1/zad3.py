import matplotlib.pyplot as plt
import numpy as np

# funkcja lambda
func = lambda x: x**2 + 5

# przedziały 'x'
x1 = np.arange(-1, 1, 0.1)
x2 = np.arange(-6, 6, 0.1)
x3 = np.arange(0, 5, 0.1)

# subplot
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(9, 5))

# tytuł figury
fig.suptitle('Arkadiusz Kontek')

# wykres pierwszego przedziału wraz z tyłem wykresu i osi
ax1.plot(x1, func(x1), label='x**2+5')
ax1.set_title('x>-1 oraz x<1')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.legend()

# wykres drugiego przedziału wraz z tyłem wykresu i osi
ax2.plot(x2, func(x2), label='x**2+5')
ax2.set_title('x>-6 oraz x<6')
ax2.set_xlabel('x')
ax2.legend()

# wykres trzeciego przedziału wraz z tyłem wykresu i osi
ax3.plot(x3, func(x3), label='x**2+5')
ax3.set_title('x>0 oraz x<5')
ax3.set_xlabel('x')
ax3.legend()

plt.show()
