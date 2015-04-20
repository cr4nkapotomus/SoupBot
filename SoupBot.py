# This Bot was made with the help of Fox (Tyler Mikesell) and 3xpl0itz (Rob Weiss)
# big greetz and all that jazz. Please use this bot for it's intended purposes if
# it ever gets propagated out. Cheers! - Cr4_nk

import re, sys, unicodedata, time, math, subprocess
from twisted.internet import reactor
from twisted.internet import protocol
from twisted.python import log
from twisted.words.protocols import irc
from selenium import webdriver

################################################################################
########                        S e t t i n g s                         ########
################################################################################
identity = {
    'CrankBot': {
        'nickname': 'SoupBot',
        'realname': 'IRCBot',
        'username': 'Soup',
        'nickserv_pw': ''
    },
}
networks = {
    'SomethingIRC': {
        'host': '192.168.2.131',
        'port': 6667,
        'ssl': False,
        'identity': identity['SoupBot'],
        'autojoin': (
            'soup',
        )
    },
}
################################################################################
log.startLogging(sys.stdout)

class TwistedBot(irc.IRCClient):

    start = 0

    def connectionMade(self):

        irc.IRCClient.connectionMade(self)
        print "Connection Established."

    def connectionLost(self, reason):

        irc.IRCClient.connectionLost(self, reason)
        print "Connection Lost."

    def signedOn(self):

        network = self.factory.network

        if network['identity']['nickserv_pw']:
            self.msg('NickServ', 'IDENTIFY %s' % network['identity']['nickserv_pw'])

        for channel in network['autojoin']:
            self.join(channel)

    def joined(self, channel):

        print("[I have joined %s]" %channel)

    def left(self, channel):

        print("[I have left %s]" %channel)

    def privmsg(self, user, channel, msg):

        timer = (time.time() - self.start)

        host = user.split('!', 1)[1]
        usernick = user.split('!', 1)[0]
        msgParts = msg.split(' ')

        if channel == self.nickname:
            print('<%s> %s' % (usernick, msg))
            msg = "Do not private message me."
            self.msg(usernick, msg) 

        if (timer > 3):

            if msgParts[0].startswith("!join") and usernick=="souperirc":
			
			
                channel = msgParts[1]
                self.join(channel)

            elif msgParts[0].startswith("!leave"):

                if msg == "!leave":

                    msg = "Ok fine :("
                    self.msg(channel, msg)
                    self.part(channel)

                else:

                    channel1 = msgParts[1]
                    msg = "Leaving #" + msgParts[1]
                    self.msg(channel, msg)
                    self.part(channel1)

            else:

                self.commands(user, channel, msg)

        self.start = time.time()

    def commands(self, user, channel, msg):

        host = user.split('!', 1)[1]
        usernick = user.split('!', 1)[0]
        msgParts = msg.split(' ')

        if msg == "!ping":

            msg = "\0038,1pong!"
            self.msg(channel, msg)
            print('<%s> %s' %(usernick, msg))

		elif msg == "!seltest":
		
			driver = webdriver.Chrome('/home/soupersalad/Botnwt/chromedriver')
			driver.get('http://www.google.com/xhtml');
			time.sleep(2) #This allows user to see something
			search_box = driver.find_element_by_name('q')
			search_box.send_keys('The Arreat Summit')
			search_box.submit()
			time.sleep(2) #This also allows user to see something
			
			link = driver.find_element_by_link_test('The Arreat Summit - A Strategy Guide for Diablo II')
			link.click()
			
			time.sleep(2) #Wait
			
			link = driver.find_element_by_link_test('Diablo II: Lord of Destruction')
			link.click()
			
			time.sleep(2) #Wait
			
			driver.quit() #Clears out webdriver, closes chrome, etc..)
			
		elif msg == "!randomize":
		
			subprocess.call("./doop.py", shell=True)
				

    def userJoined(self, user, channel):

        usernick = user.split('!', 1)[0]

    def alterCollidedNick(self, nickname):

        return nickname + '^'

    def kickedFrom(self, channel, kicker, message):

        print "I was kicked. \nChannel: " + channel + "\nKicker: " + kicker + "\nReason: " + message
        self.join(channel)
        print "Attempting to rejoin " + channel

    def userRenamed(self, oldname, newname):
        """
        Called when a user changes there nick
        """
        print "%s is now %s" %(oldname, newname)

    def _get_nickname(self):
        return self.factory.network['identity']['nickname']

    def _get_realname(self):
        return self.factory.network['identity']['realname']

    def _get_username(self):
        return self.factory.network['identity']['username']

    nickname = property(_get_nickname)
    realname = property(_get_realname)
    username = property(_get_username)

class TwistedBotFactory(protocol.ClientFactory):

    protocol = TwistedBot

    def __init__(self, network_name, network):

        self.network_name = network_name
        self.network = network

    def clientConnectionLost(self, connector, reason):

        print('client connection lost')
        connector.connect()

    def clientConnectionFailed(self, connector, reason):

        print('client connection failed')
        reactor.stop()

if __name__ == '__main__':

    for name in networks.keys():

        factory = TwistedBotFactory(name, networks[name])

        host = networks[name]['host']
        port = networks[name]['port']

        if networks[name]['ssl']:
            reactor.connectSSL(host, port, factory, ssl.ClientContextFactory())
        else:
            reactor.connectTCP(host, port, factory)

    reactor.run()