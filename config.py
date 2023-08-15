#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Dark Angel

import os
import logging

class Config:
    
    API_ID = int(os.environ.get("API_ID", "20506609"))
    API_HASH = os.environ.get("API_HASH", "94f95fc96d4d914d8a807ecb3ca6ba92")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5473067352:AAHMEGb37UGorEcmgi_43YW5AQ9VjEQXuR4") 
    BOT_SESSION = os.environ.get("BOT_SESSION", "bot") 
    CAPTION = os.environ.get("CAPTION", "")
    FROM_CHANNEL = os.environ.get("FROM_CHANNEL", "@OkFiles")
    FILTER_TYPE = os.environ.get("FILTER_TYPE", "video")
    OWNER_ID = os.environ.get("OWNER_ID", "2056407064")
    LIMIT = int(os.environ.get("LIMIT","10000"))
    SKIP_NO = int(os.environ.get("SKIP_NO", "0"))
    SESSION = os.environ.get("SESSION", "BQByPmwASpFCKnoXcYJM5MTb8RL8BZUnTvTDvnrOXpegkAZud1M0-2c7P_p1ypncFSDZ2OOuxEbQfYfTfbxJb85SMICbuxKbZ4vD6ZXS1Vr2A6ncED3LsY_sMRKeDmZXC33nVp7CNZMNxMJrrrk7HchMOM5FicxdrIYG_a3vY5oouDvEXj8gNVuQbmIYnbq1Vvn2rFiwKmMhyJVeKPyNeiX6ZnSCefxayecFr051rchgVUHbmG2UzPYk1m3vAOI5eMjz0vXgfQoNvQxc4gPOhtwRfpt-AMcNfysxr_CzYpg-setLROr4RfgqEPDh1SJxMUwBUjz9eOZCrjiOXBtYiBAfUC9zTAAAAAB0nNOMAA")
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", "-1001837099658"))
def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
