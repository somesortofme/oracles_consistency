import numpy as np


def consistency_check(oracles, answers):
    """input:
    oracles [nxk] - matrix with k predictions of n oracles,
    answers [k-1] - vector with correct answers for previous k-1 tasks
    output:
    eig of matrix"""
    oracle_count = 0
    coeff = []
    #first step - building of truth_coef for each oracle
    for j in range(0, len(oracles)):
        for i in range(0, len(oracles[j])-1):
            if oracles[j][i] == answers[i]:
                oracle_count += 1
        coeff.append(oracle_count / (len(oracles[j])-1))
        oracle_count = 0
    #now we have in coeff[i] truth coefficien for each oracle[i]
    #need to build consistency matrix C[nxn] where c[i][j]=oracle[i] / oracle[j]
    concicency = np.eye(len(coeff))
    #v = np.zeros()
    #print(coeff[0])
    for i in range(0, len(coeff)):
        for j in range(0, len(coeff)):
            if (i != j) and coeff[j] != 0:
                concicency[i][j] = coeff[i] / coeff[j]
    #now we need to count eig
    return np.linalg.eig(concicency)


if __name__ == '__main__':
    oracles = [[1, 0, 0, 1],
               [0, 0, 1, 0],
               [1, 0, 0, 0],
               [0, 0, 0, 0],
               [1, 1, 1, 1],
               [1, 1, 0, 0]]
    answers = [0, 1, 1]
    evalue, evect = consistency_check(oracles, answers)
    #we have evalue[i] for each oracle
    for i in range(0, len(evalue)):
        print("value for i-th oracle is:")
        print(abs((evalue[i] - len(evalue)) / (len(evalue) - 1)))
    print("The oracle which is closest to 0 is the best")
