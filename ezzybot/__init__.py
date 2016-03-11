#EzzyBot 2016
#Created by zz & Bowserinator (freenode)

import socket
import ssl as securesl
from time import sleep
import thingdb

def send(data):
    print("[SEND) {}".format(data))
    irc.send("{}\r\n".format(data).encode("UTF-8"))

def recv():
    part = ""
    data = ""
    while not part.endswith("\r\n"):
        part = irc.recv(2048)
        part = part.decode()
        data += part
    data = data.splitlines()
    return data

def printrecv():
    ircmsg = recv()
    for line in ircmsg:
        print("[RECV) {}".format(line))
    return ircmsg
    

    

def run(config={}):
    global irc, db
    host = config.get("host") or "irc.freenode.net"
    port = config.get("port") or 6667
    ssl = config.get("ssl") or False
    nick = config.get("nick") or "EzzyBot"
    ident = config.get("indent") or "EzzyBot"
    realname = config.get("realname") or "EzzyBot: a simple python framework for IRC bots."
    channels = config.get("channels") or ["#EzzyBot"]
    analytics = config.get("analytics") or True

    if Analytics == True:
        channels.append("#EzzyBot")
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    if ssl == True:
        irc = securesl.wrap_socket(sock)
    else:
        irc = sock
    irc.connect((host, port))
    send("NICK {}".format(nick))
    send("USER {} * * :{}".format(ident, realname))
    send("JOIN {}".format(",".join(channels)))
    while True:
        msg = printrecv()
        for irc_msg in msg:
            irc_msg = ircmsg.strip(":")
            t = irc_msg.split()
            
            if t[0] == "PING":
                send("PONG {}".format(" ".join(t[1:])))

#Testing just for now
run({"channels":["##bwbellairs-bots"]})
