Tweet-Command-Line-Tool
=======================
Is a simple python script to send tweets. It can be ease integrated to another app, such as media player, to send Now Playing status.

**Needed oauth consumer and access tokens with write permission.**

##Usage
```bash
python the-path-where-you-placed-the-file/tweet-tool.py 'My tweet message'
```

##Options

**--config-file**: Absolute path to config file that holds the OAuth tokens like shown below.

```bash
[oauth_settings]
consumer_key = your cosumer key
consumer_secret = your cosumer secret
access_token_key = your access token key
access_token_secret = your access token secret
```
        
If omitted, the config file will be searched by weet-tool.cfg in the same location where the tweet-tool.py was placed.

**--interval**: A number that indicates how often the tweets will be sent.
        Example:
```bash
python the-path-where-you-placed-the-file/tweet-tool.py 'My automatic tweet message' --interval=3
```
In above example, the automatic message will be sent for each 3 (three) scripts's call.
This is a very useful feature for automatic calls from apps. Avoid nagging his followers flooding their timelines.


##If you are using GmusicBrowser

- Go to settings > plugins
- Enable Now Playing plugin
- Fill the field "Command when playing song changed" like shown bellow.

```bash
python the-path-where-you-placed-the-file/tweet-tool.py '%t by %a #NowPlaying' --interval=3
```

##Installation

```bash
$ pip install tweet-command-line-tool
```

or download/clone the package and

```bash
$ python setup install
```

That's it.
