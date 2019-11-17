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

estimator_value = [max(s) + max(s) / k - 1 for s in samples]
mean = np.mean(estimator_value)

plt.figure(figsize=(10, 5))

plt.style.use("bmh")
plt.hist(estimator_value, bins=20, rwidth=0.95)
plt.axvline(mean, color="r", linewidth=3, linestyle=":", label="mean")
plt.axvline(N, color="k", linewidth=3, linestyle="-", label="N")

plt.legend()

min_ylim, max_ylim = plt.ylim()

plt.title(f"Minimum Variance Unbiased Estimator\nN={N}, k={k}")

plt.gcf().text(0.40, 0.0, "mean={:.2f}".format(np.mean(estimator_value)), fontsize=12)
plt.gcf().text(0.56, 0.0, "sd={:.2f}".format(np.std(estimator_value)), fontsize=12)
plt.xlabel("Estimated Number of Tanks (n)")
plt.ylabel("Frequency")
plt.savefig("estim.png", dpi=300)
plt.show()
