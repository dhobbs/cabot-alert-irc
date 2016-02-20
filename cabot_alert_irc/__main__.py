import itertools

import irc.client
import sys
import Queue


def on_connect(connection, event, channel):
    print "on_connect: ", channel
    connection.join(channel)


def on_join(connection, event, channel, reactor, messages):
    print "on_join: ", channel, "msg: ", messages
    message_loop(connection, channel, messages)


def on_disconnect(connection, event):
    raise SystemExit()


def irc_connect(server, port, nickname, channel, msgs):
    reactor = irc.client.Reactor()
    try:
        c = reactor.server().connect(server, port, nickname)
    except irc.client.ServerConnectionError:
        print(sys.exc_info()[1])
        raise SystemExit(1)

    c.add_global_handler("welcome", lambda connection, event: on_connect(connection, event, channel))
    c.add_global_handler("join", lambda connection, event: on_join(connection, event, channel, reactor, msgs))
    c.add_global_handler("disconnect", on_disconnect)

    return reactor


def message_stream(messages):
    while True:
        yield messages.get()


def message_loop(connection, channel, messages):
    for msg in itertools.takewhile(bool, message_stream(messages)):
        print (msg)
        connection.privmsg(channel, msg)


def main():
    print "Hello world"
    channel = '#_test777'
    messages = Queue.Queue()
    reactor = irc_connect('chat.freenode.net', 6667, 'cabotirc123', channel, messages)

    print 'Connected'

    messages.put('Yo')
    messages.put('Dude')

    reactor.process_forever()

if __name__ == "__main__":
    main()
