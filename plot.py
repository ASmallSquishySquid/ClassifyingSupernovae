import pandas as pd
import matplotlib.pyplot as plt

counts = pd.read_csv("counts.csv");
plt.xlim((0, 3))
plt.ylim((0, 6))
plt.xlabel("$H \\alpha / R$")
plt.ylabel("$V/R$")

type_1 = counts[counts["type"] == 1]
type_1 = type_1.reset_index()
ha_r_1 = [type_1.loc[x, "ha_med"] / type_1.loc[x, "r_med"] for x in range(type_1.shape[0])]
v_r_1 = [type_1.loc[x, "v_med"] / type_1.loc[x, "r_med"] for x in range(type_1.shape[0])]

ha_r_max_1 = [type_1.loc[x, "ha_min"] / type_1.loc[x, "r_max"] for x in range(type_1.shape[0])]
ha_r_min_1 = [type_1.loc[x, "ha_max"] / type_1.loc[x, "r_min"] for x in range(type_1.shape[0])]
v_r_max_1 = [type_1.loc[x, "v_min"] / type_1.loc[x, "r_max"] for x in range(type_1.shape[0])]
v_r_min_1 = [type_1.loc[x, "v_max"] / type_1.loc[x, "r_min"] for x in range(type_1.shape[0])]
ha_r_err_1 = [[ha_r_1[x] - ha_r_min_1[x] for x in range(len(ha_r_min_1))], [ha_r_max_1[x] - ha_r_1[x] for x in range(len(ha_r_max_1))]]
v_r_err_1 = [[v_r_1[x] - v_r_min_1[x] for x in range(len(v_r_min_1))], [v_r_max_1[x] - v_r_1[x] for x in range(len(v_r_max_1))]]

plt.errorbar(ha_r_1, v_r_1, c="red", label="Type 1", xerr=ha_r_err_1, yerr=v_r_err_1, fmt="o", capsize=2)

for x in range(type_1.shape[0]):
	plt.annotate(type_1.loc[x, "name"], (ha_r_1[x], v_r_1[x]), textcoords="offset points", xytext=(2,-10))


type_2 = counts[counts["type"] == 2]
type_2 = type_2.reset_index()
ha_r_2 = [type_2.loc[x, "ha_med"] / type_2.loc[x, "r_med"] for x in range(type_2.shape[0])]
v_r_2 = [type_2.loc[x, "v_med"] / type_2.loc[x, "r_med"] for x in range(type_2.shape[0])]

ha_r_max_2 = [type_2.loc[x, "ha_min"] / type_2.loc[x, "r_max"] for x in range(type_2.shape[0])]
ha_r_min_2 = [type_2.loc[x, "ha_max"] / type_2.loc[x, "r_min"] for x in range(type_2.shape[0])]
v_r_max_2 = [type_2.loc[x, "v_min"] / type_2.loc[x, "r_max"] for x in range(type_2.shape[0])]
v_r_min_2 = [type_2.loc[x, "v_max"] / type_2.loc[x, "r_min"] for x in range(type_2.shape[0])]
ha_r_err_2 = [[ha_r_2[x] - ha_r_min_2[x] for x in range(len(ha_r_min_2))], [ha_r_max_2[x] - ha_r_2[x] for x in range(len(ha_r_max_2))]]
v_r_err_2 = [[v_r_2[x] - v_r_min_2[x] for x in range(len(v_r_min_2))], [v_r_max_2[x] - v_r_2[x] for x in range(len(v_r_max_2))]]

plt.errorbar(ha_r_2, v_r_2, c="blue", label="Type 2", xerr=ha_r_err_2, yerr=v_r_err_2, fmt="o", capsize=2)

for x in range(type_2.shape[0]):
	plt.annotate(type_2.loc[x, "name"], (ha_r_2[x], v_r_2[x]), textcoords="offset points", xytext=(2,-10))


type_0 = counts[counts["type"] == 0]
type_0 = type_0.reset_index()
ha_r_0 = [type_0.loc[x, "ha_med"] / type_0.loc[x, "r_med"] for x in range(type_0.shape[0])]
v_r_0 = [type_0.loc[x, "v_med"] / type_0.loc[x, "r_med"] for x in range(type_0.shape[0])]

ha_r_max_0 = [type_0.loc[x, "ha_min"] / type_0.loc[x, "r_max"] for x in range(type_0.shape[0])]
ha_r_min_0 = [type_0.loc[x, "ha_max"] / type_0.loc[x, "r_min"] for x in range(type_0.shape[0])]
v_r_max_0 = [type_0.loc[x, "v_min"] / type_0.loc[x, "r_max"] for x in range(type_0.shape[0])]
v_r_min_0 = [type_0.loc[x, "v_max"] / type_0.loc[x, "r_min"] for x in range(type_0.shape[0])]
ha_r_err_0 = [[ha_r_0[x] - ha_r_min_0[x] for x in range(len(ha_r_min_0))], [ha_r_max_0[x] - ha_r_0[x] for x in range(len(ha_r_max_0))]]
v_r_err_0 = [[v_r_0[x] - v_r_min_0[x] for x in range(len(v_r_min_0))], [v_r_max_0[x] - v_r_0[x] for x in range(len(v_r_max_0))]]

plt.errorbar(ha_r_0, v_r_0, c="black", label="Unknown type", xerr=ha_r_err_0, yerr=v_r_err_0, fmt="o", capsize=2)

for x in range(type_0.shape[0]):
	plt.annotate(type_0.loc[x, "name"], (ha_r_0[x], v_r_0[x]), textcoords="offset points", xytext=(2,-10))

plt.legend()
plt.savefig("plot.png")