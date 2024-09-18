import numpy as np


def get_communicating_states(P, N=20):
    """
    Calculates the equivalence classes/communicating states of states in a Markov chain.

    Input:
        - P, nparray: Transition probability matrix for a markov chain.
    Ouput:
        - com_states, list of tuples: [(state1, state2), ...] returns communicating states
    """
    com_states=set()
    for n in range(1, N+1):
        P_n = np.linalg.matrix_power(P, n)
        for i in range(P_n.shape[0]):
            for j in range(P_n.shape[1]):
                if P_n[i,j] > 0 and P[j, i] > 0:
                    com_states.add((i, j))
    return com_states


def get_limiting_distribution(P, N=100):
    return np.linalg.matrix_power(P, N)[0, :]