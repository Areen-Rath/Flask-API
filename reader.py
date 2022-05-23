import pandas as pd

data = pd.read_csv('final.csv')

id = data["ID"].tolist()
name = data["Name"].tolist()
distance = data["Distance"].tolist()
mass = data["Mass"].tolist()
radius = data["Radius"].tolist()
gravity = data["Gravity"].tolist()

final_data = []
for index in id:
    final_data.append({
        "name": name[index],
        "distance": distance[index],
        "mass": mass[index],
        "radius": radius[index],
        "gravity": gravity[index]
    })

print(final_data)