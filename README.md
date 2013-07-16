*Needed library python-twitter, oauth consumer and access tokens with write permission.

Usage:
    python the-path-where-you-placed-the-file/tweet-tool.py 'My tweet message'


Options:
    --config-file=absolute-path-to-config-file : File with OAuth tokens like shown bellow.

            [oauth_settings]
            consumer_key = your cosumer key
            consumer_secret = your cosumer secret
            access_token_key = your access token key
            access_token_secret = your access token secret

        If omitted, will be searched by config-file tweet-tool.cfg in the same location where the tweet-tool.py was placed

    --interval=number : Indicates how often the tweets will be sent.
        Example:

            python the-path-where-you-placed-the-file/tweet-tool.py 'My automatic tweet message' --interval=3

        In above example, the automatic message will be sent for each 3 (three) scripts's call.
        This is a very useful feature for automatic calls from apps. Avoid nagging his followers flooding their timelines.


If you are using GmusicBrowser

    -Go to settings > plugins
    -Enable Now Playing plugin
    -Fill the field "Command when playing song changed" like shown bellow.

        python the-path-where-you-placed-the-file/tweet-tool.py 'My tweet message' --interval=3


That's it.
