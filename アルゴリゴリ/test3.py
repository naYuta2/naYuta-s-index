import matplotlib.pyplot as plt

def inc(x):
    return 2*x+1

def func(x):
    return x ** 2 + x - 1

N = 20
x = 1.0
losses = []
for _ in range(N):
    a = inc(x)
    fx = func(x)

    x = x - (fx / a)
    losses.append(func(x))

print(x, func(x))

plt.figure(figsize=(8, 5))
plt.plot(losses, color='royalblue', label='Loss')
plt.title("Convergence of Loss During Iterative Solution", fontsize=16)
plt.xlabel("Epoch", fontsize=14)
plt.ylabel("Total Residual (Loss)", fontsize=14)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()
plt.tight_layout()
plt.show()