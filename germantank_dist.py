import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams

rcParams["font.family"] = "sans-serif"
rcParams["font.sans-serif"] = ["Arial"]

np.random.seed(1_294_837)

N = 1000
k = 15
Ns = np.linspace(1, N + 1)
iterations = 10000


def sample(Ns, k):
    return np.random.choice(Ns, k, replace=False)


samples = [sample(Ns, k) for _ in range(iterations)]

mle_estimator = [max(s) for s in samples]
min_and_max_estimator = [min(s) + max(s) for s in samples]
mean2_estimator = [sum(s) / len(s) for s in samples]
mvue_estimator = [max(s) + max(s) / k - 1 for s in samples]

