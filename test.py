from logging.config import listen
from sre_constants import RANGE
from tkinter.messagebox import YES
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
    global a
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
    global Weekbefore
    Weekbefore = a - datetime.timedelta(days=7)

    global WeekBFFIX
    WeekBFFIX = (str(Weekbefore.day)+'/' +
                 str(Weekbefore.month)+'-'+str(Weekbefore.year))

    global maxweek
    maxweek = a + datetime.timedelta(days=7)

    global DANUMBA
    DANUMBA = {}
    global thenumba
    thenumba = {}
    global liste
    liste = {}
    global opgavekeys
    opgavekeys = {}


# Print out your exercises
lectiotime()
skema = (str(lec.getExercises()))

anan = skema.replace("\'", "\"")

xx = json.loads(anan)


aa = (int(len(xx)-14))


for ad in range(aa):
    global yy
    yy = xx[int(ad+14)]
    ff = str(yy['Frist'].split(curYear)[0])
    kk = ff.replace("-", "-"+curYear)
    fff = str(yy['Id'])
    # das = str(ad+14)
    # intdas = int(ad+14)

    liste.update({kk: fff})
opgavekeys = list(liste.keys())


for keynum in range(len(opgavekeys)):

    na = str(opgavekeys[keynum])
    keyyear = int(na.split("-")[1])
    keymonth = int((na.split("/")[1]).split("-")[0])
    keyday = int((na.split("-")[0]).split("/")[0])
    keydate = datetime.datetime(keyyear, keymonth, keyday)

    if keydate >= Weekbefore and keydate >= a and keydate < maxweek:

        print(xx[keynum+14])
    else:
        pass
