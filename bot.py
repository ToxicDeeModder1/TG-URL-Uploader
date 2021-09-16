#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K

# the logging things
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os

# the secret configuration specific things
if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config

import pyrogram
logging.getLogger("pyrogram").setLevel(logging.WARNING)


if __name__ == "__main__" :
    # create download directory, if not exist
    if not os.path.isdir(Config.DOWNLOAD_LOCATION):
        os.makedirs(Config.DOWNLOAD_LOCATION)
    plugins = dict(
        root="plugins"
    )
    app = pyrogram.Client(
        "NarutoXAnyLinkBot",
        bot_token=Config.1901621438:AAHk3dzDle82O-C1pB42SsR8GW8rdnwl9cY,
        api_id=Config.8522555,
        api_hash=Config.9e0b9e90b854c23fe89ee57b0a75ff32,
        plugins=plugins
    )
    Config.AUTH_USERS.add(683538773)
    app.run()
