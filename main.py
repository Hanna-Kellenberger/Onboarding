import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('can_data.csv')

# clean the data
df.dropna(inplace=True)
df["timestamp"] = pd.to_datetime(df["timestamp"])

# visualize the data
plt.figure()
plt.title("TPS and wheel speed over Time")
plt.plot(df["timestamp"], df["TPS"])
plt.plot(df["timestamp"], df["Driven Wheel Speed #1"])
plt.xlabel("Timestamp")
plt.ylabel("TPS and Driven Wheel Speed #1")
plt.legend(["TPS", "Driven Wheel Speed #1"])

plt.figure()
plt.title("RPM vs TPS")
plt.scatter(df["RPM"], df["TPS"])
plt.xlabel("RPM")
plt.ylabel("TPS") 

plt.figure()
plt.title("RPM vs wheel speed")
plt.plot(df["RPM"], df["Driven Wheel Speed #1"],'o')
plt.xlabel("RPM")
plt.ylabel("Driven Wheel Speed #1") 

plt.show()