import numpy as np

mu_1 = -3
mu_2 = 2
signma_square_1 = 4
signma_square_2 = 4
p_1 = .5
p_2 = .5
d = 1
x_1 = 0.2
p_i1_given_j1 = (1/((2*np.pi*signma_square_1)**1/2)) * np.exp( (-1/(2*signma_square_1)) * (1.8-mu_1)**2 )
p_i1_given_j2 = (1/((2*np.pi*signma_square_2)**1/2)) * np.exp( (-1/(2*signma_square_2)) * (1.8-mu_2)**2 )
p_j1_given_i1 = p_1 * p_i1_given_j1 / (p_1 * p_i1_given_j1 + p_2 * p_i1_given_j2)
print(p_j1_given_i1)
