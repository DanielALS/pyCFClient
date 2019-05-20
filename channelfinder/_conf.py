# -*- coding: utf-8 -*-

"""
Internal module

Used to read the channelfinderapi.conf file

example file
cat ~/channelfinderapi.conf
[DEFAULT]
BaseURL=http://localhost:8080/ChannelFinder
username=MyUserName
password=MyPassword
"""

def __loadConfig():
    import logging
    import os.path
    import ConfigParser

    log = logging.getLogger(__name__)

    dflt = {'BaseURL':'http://localhost:8080/ChannelFinder'}

    cf = ConfigParser.SafeConfigParser(defaults=dflt)
    cf.read(['/etc/channelfinderapi.conf',
             os.path.expanduser('~/channelfinderapi.conf'),
             'channelfinderapi.conf'
             ])

    logging.info("URL:%s" % cf.get('DEFAULT', 'BaseURL'))
    return cf

_conf = __loadConfig()
