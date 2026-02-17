import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('can_data.csv')

# clean the data
df.dropna(inplace=True)
df["timestamp"] = pd.to_datetime(df["timestamp"])

# visualize the data
plt.figure()
plt.title("RPM over time")
plt.plot(df["timestamp"], df["RPM"])
plt.xlabel("Timestamp")
plt.ylabel("RPM")
plt.savefig("graphs/RPM.png")

plt.figure()
plt.title("Wheel speed over time")
plt.plot(df["timestamp"], df["Driven Wheel Speed #1"])
plt.xlabel("Timestamp")
plt.ylabel("Driven Wheel Speed #1")
plt.savefig("graphs/WheelSpeed.png")

plt.figure()
plt.title("RPM vs wheel speed")
plt.plot(df["RPM"], df["Driven Wheel Speed #1"], 'o')
plt.xlabel("RPM")
plt.ylabel("Driven Wheel Speed #1") 
plt.savefig("graphs/RPM_WheelSpeed.png")

plt.show()