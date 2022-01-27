from src.lectio import Lectio
import json


lec = Lectio("21Epsilon27", "Kaya7601", "523")
# Print out your exercises


ohye = (str(lec.getSchedule()))

anan = ohye.replace("\'", "\"")

x = json.loads(anan)

y = x[0]
z = y.keys()

print(y['Team'])
