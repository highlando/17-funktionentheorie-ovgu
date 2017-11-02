import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import factorial
np.set_printoptions(precision=2, suppress=True, linewidth=300)


# define the truncated sine expansion
def sinN(N):
    def evasinN(z):
        sinz = 0
        for k in np.arange(N+1):
            sinz += (-1)**k*z**(2*k+1)/factorial(2*k+1.)
        return sinz
    return evasinN

# the range for the evaluation
trange = np.linspace(0, 10.7, 18)
print('abscissa: ', trange)

# check the sine expansion for varying truncations
Nlist = [0, 1, 3, 5, 9]
plt.figure(2)
for N in Nlist:
    mysinN = sinN(N)
    sint = mysinN(trange)
    print('N={0}: '.format(N), sint)

    # cut off values beyond 5
    cutoff = np.abs(sint) > 5
    sint[cutoff] = None
    plt.plot(trange, sint, label='N={0}'.format(N))


# the "real" function values
sint = np.sin(trange)
plt.figure(2)
print('real sine: '.format(N), sint)
plt.plot(trange, sint, label='sine')
plt.legend()

# show the plot
plt.show()
