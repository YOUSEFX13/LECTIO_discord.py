from src.lectio import Lectio
import os
import json
import datetime
from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
LECNAME = os.getenv('Lectio_name')
LECPASS = os.getenv('Lectio_pass')
SCHOOLID = os.getenv('Lectio_ID')
lec = Lectio(LECNAME, LECPASS, SCHOOLID)


def lectiotime():
    a = datetime.datetime.now()

    global curDay
    curDay = a.strftime("%d")
    if curDay.startswith('0'):
        curDay = curDay.split('0')[1]
        pass

    else:
        pass

    global curMonth
    curMonth = a.strftime("%m")
    if curMonth.startswith('0'):

        curMonth = curMonth.split('0')[1]
        pass

    else:
        pass

    global curYear
    curYear = a.strftime("%Y")

    global curDate
    curDate = (curDay+'/'+curMonth+'-'+curYear)

    global DANUMBA
    DANUMBA = {}
    global thenumba
    thenumba = {}


lectiotime()


# Print out your exercises


skema = (str(lec.getExercises()))

anan = skema.replace("\'", "\"")

x = json.loads(anan)


aa = (int(len(x)))
testm = str(1)


for ad in range(aa):
    global yy
    yy = x[int(ad)]
    ff = str(yy['Id'].split(curYear)[0])
    kk = ff.replace("-", "-"+curYear)

    DANUMBA[str(kk)] = str(ad)

    gg = DANUMBA.get(str(curDate), 'del')
    u = [(gg, {gg: gg})]

    thenumba.update(u)

    if 'del' in thenumba:
        thenumba.pop('del')
    else:
        pass

print(x)
# for l in thenumba:
# print(l)
