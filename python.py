#!C:\Program Files (x86)\Python37-32\python.exe
from db import *
import asyncio
import json
import logging
import websockets

logging.basicConfig()

BENUTZER = {"value": 0}
USERS = set()


def neuerbenutzer_event():
    return json.dumps({"type": "neuerBenutzer", **BENUTZER})


def users_event():
    return json.dumps({"type": "users", "count": len(USERS)})
    #Wuerde Informationen an die HTML Seite schicken
def anmelden_event():
    return json.dumps({"type": "anmelden", **BENUTZER})

def gruppeneu_event():
    return json.dumps({"type": "gruppe", **BENUTZER})

def termin_event():
    return json.dumps({"type": "termin", **BENUTZER})

async def notify_neuerbenutzer():
    if USERS:  # asyncio.wait doesn't accept an empty list
        message = neuerbenutzer_event()
        print("startnoified")
        await asyncio.wait([user.send(message) for user in USERS])
        print("neuerbenutzernotified")

async def notify_gruppeneu():
    if USERS:  # asyncio.wait doesn't accept an empty list
        message = gruppeneu_event()
        await asyncio.wait([user.send(message) for user in USERS])
        print("gruppenotified")

async def notify_anmelden():
    if USERS:  # asyncio.wait doesn't accept an empty list
        message = anmelden_event()
        await asyncio.wait([user.send(message) for user in USERS])
        print("angemeldet")
        
async def notify_termine():
    if USERS:  # asyncio.wait doesn't accept an empty list
        message = termine_event()
        await asyncio.wait([user.send(message) for user in USERS])
        print("termine")
async def notify_users():
    if USERS:  # asyncio.wait doesn't accept an empty list
        message = users_event()
        await asyncio.wait([user.send(message) for user in USERS])
#Wuerde zaehlen, wieviele User gerade online sind.

async def register(websocket):
    USERS.add(websocket)
    #await notify_users()


async def unregister(websocket):
    USERS.remove(websocket)
    #await notify_users()


async def watch(websocket, path):
    # register(websocket) sends user_event() to websocket
    await register(websocket)
    print("registered")
    try:
        print("hallo")
        async for message in websocket:
            print("message",message)
            data = json.loads(message)
            print("pydata:",data)
            if data["action"] == "neuerBenutzer":
                BENUTZER["value"]=data["inhalt"]
                print("pybenutzer:",BENUTZER["value"][0],BENUTZER["value"][1])
                BENUTZER["value"]=benutzer.hinzufuegen(BENUTZER["value"][0],BENUTZER["value"][1])
                print("pybenutzererg",BENUTZER["value"])
                await notify_neuerbenutzer()
            elif data["action"] == "anmelden":
                BENUTZER["value"]=data["inhalt"]
                print("pyanmeldenm:",BENUTZER["value"][0],BENUTZER["value"][1])
                BENUTZER["value"]=benutzer.anmelden(BENUTZER["value"][0],BENUTZER["value"][1])
                print("anmeldeerg",BENUTZER["value"])
                await notify_anmelden()
            elif data["action"] == "gruppe":
                BENUTZER["value"]=data["inhalt"]
                print("pygruppenm:",BENUTZER["value"][0],BENUTZER["value"][1:len(BENUTZER["value"])])
                BENUTZER["value"]=gruppen.hinzufuegen(BENUTZER["value"][0],BENUTZER["value"][1:len(BENUTZER["value"])])
                print("gruppenerg",BENUTZER["value"])
                await notify_gruppeneu()
            elif data["action"] == "termin":
                BENUTZER["value"]=data["inhalt"]
                print("pyterminm:",BENUTZER["value"][0],BENUTZER["value"][1])
                BENUTZER["value"]=benutzer.termin(BENUTZER["value"][0],BENUTZER["value"][1])
                print("gruppenerg",BENUTZER["value"])
                termine=[]
                termine[0]=gruppen.ptermin(BENUTZER["value"][2])
                termine[1]=gruppen.fptermin(BENUTZER["value"][2])
                BENUTZER["value"]=termine
                await notify_termine()
            else:
                logging.error("unsupported event: {}", data)
    except:
        print("Fehlgeschlagen")
    finally:
        await unregister(websocket)
        print("unregistered")


start_server = websockets.serve(watch, "localhost", 6789)

try:
    print("Versuch")
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()
except:
    print("kaputt")
    pass
