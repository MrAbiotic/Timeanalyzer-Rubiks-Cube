import json
from matplotlib import pyplot as plt

x = []
b1 = []
b2 = []
oe = []
le = []
tot = []

target = [4, 6, 4, 6]

# filename = "cstimer_roux_split_times.json"
filename = "data/cstimer_20250211_234827.txt"
with open(filename) as f:
    session = json.load(f)

    count = 0
    for solve in session["session5"]:
        count += 1

        local_b1 = solve[0][4]
        local_b2 = solve[0][3]-local_b1
        local_oe = solve[0][2]-local_b2-local_b1
        local_le = solve[0][1]-local_oe-local_b2-local_b1
        
        x.append(count)
        b1.append(local_b1/1000)
        b2.append(local_b2/1000)
        oe.append(local_oe/1000)
        le.append(local_le/1000)
        tot.append(solve[0][1]/1000)

plt.style.use("dark_background")

plt.subplot(2, 3, 1)
plt.plot(x, b1)
plt.plot(x, [target[0] for _ in x])
plt.title("Block 1")

plt.subplot(2, 3, 2)
plt.plot(x, b2)
plt.plot(x, [target[1] for _ in x])
plt.title("Block 2")


plt.subplot(2, 3, 4)
plt.plot(x, oe)
plt.plot(x, [target[2] for _ in x])
plt.title("Orient Corners")

plt.subplot(2, 3, 5)
plt.plot(x, le)
plt.plot(x, [target[3] for _ in x])
plt.title("Last 6 Edges")

plt.subplot(1, 3, 3)
plt.plot(x, tot)
plt.plot(x, [sum(target) for _ in x])
plt.title("Total time")

plt.show()
