import matplotlib.pyplot as plt

arr = [
    [4, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 4, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 4, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 4, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 4, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 4, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 4, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 4, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 4, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 4]
]
b = [6, 10, 8, 10, 7, 6, 7, 10, 7, 5]

x = [1] * 10
losses = []

epoch = 50
for e in range(epoch):
    for i in range(10):
        s = 0
        for j in range(10):
            if i != j:
                s += arr[i][j] * x[j]
        x[i] = (b[i]-s) / arr[i][i]
    
    if (e+1) % 10 == 0:
        print(f"epoch {e+1}")
        for i in range(len(x)):
            print(f"x{i+1}: {x[i]}")
        
    loss = 0
    for i in range(10):
        s = 0
        for j in range(10):
            s += arr[i][j] * x[j]
        loss += b[i] - s
    losses.append(loss)

plt.figure(figsize=(8, 5))
plt.plot(losses, color='royalblue', label='Loss')
plt.title("Convergence of Loss During Iterative Solution", fontsize=16)
plt.xlabel("Epoch", fontsize=14)
plt.ylabel("Total Residual (Loss)", fontsize=14)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()
plt.tight_layout()
plt.show()