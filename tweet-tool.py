#!/usr/bin/env python
#-*- coding:utf-8 -*-

try:
    import twitter
except:
    raise ImportError('python-twitter is required!')

import os, sys, tempfile, logging
from ConfigParser import RawConfigParser

logfile = os.path.join(tempfile.gettempdir(), 'tweet-tool.log')
logging.basicConfig(level=logging.INFO, filename=logfile)
log = logging.getLogger(__name__)

class TweetToolError(Exception):
    pass

COUNT_PATH = os.path.join(tempfile.gettempdir(), '.PyTT-count')

def get_params(argv):
    '''
    Gets parameters from line command
    '''
    params = dict([arg[2:].split('=') for arg in argv[1:] if arg.startswith('--')])
    if len(argv) > 1 and not argv[1].startswith('--'):
        params.update({'message':argv[1]})
    return params

def config(params):
    '''
    Setting up dictionary parameters
    '''
    config_file = params.get('config-file', os.path.join( os.path.dirname(__file__), 'tweet-tool.cfg' ))
    if(config_file and os.path.exists(config_file)):
        config = RawConfigParser(); config.readfp(open(config_file))
        params.update( {'oauth_settings':dict(config.items('oauth_settings'))} )
    else:
        raise TweetToolError('Config file not found!')

    if not params.has_key('oauth_settings'):
        raise TweetToolError('OAuth settings not found!')

    if not params.has_key('message'):
        raise TweetToolError('Message is required!')

    return params

def get_interval_count():
    '''
    Gets the current interval count
    '''
    if os.path.exists(COUNT_PATH):
        count = open(COUNT_PATH).read() or '1'
        return int(count)
    return 1

def update_interval_count(number):
    '''
    Updates the interval count
    '''
    open(COUNT_PATH, 'w').write(str(number))

def tweet(oauth_settings, message):
    '''
    Sends message to twitter status
    '''
    api = twitter.Api(**oauth_settings)
    try:
        status = api.PostUpdate(message)
    except TweetToolError, e:
        raise e
    else:
        return status.id, status.text

if __name__ == '__main__':
    log.info('starting...')
    log.info('getting parameters...')
    params = get_params(sys.argv)
    log.info('setting up...')
    config(params)
    interval = int(params.get('interval', 1))
    log.info('interval: %s, current_interval: %s' %  (interval, get_interval_count()) ) 

    if get_interval_count() == interval:
        update_interval_count(1)
        post = tweet(params['oauth_settings'], params['message'])
        log.info(post)
    elif get_interval_count() > interval:
        update_interval_count(1)
    else:
        update_interval_count(get_interval_count()+1)
