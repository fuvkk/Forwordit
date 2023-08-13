#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Dark Angel

import os
import logging

class Config:
    
    API_ID = int(os.environ.get("API_ID", "10098309"))
    API_HASH = os.environ.get("API_HASH", "aaacac243dddc9f0433c89cab8efe323")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5473067352:AAGWQhamLe-9LT-jMtxhY5PID0FJ03x8wvg") 
    BOT_SESSION = os.environ.get("BOT_SESSION", "bot") 
    CAPTION = os.environ.get("CAPTION", "")
    FROM_CHANNEL = os.environ.get("FROM_CHANNEL", "@OkFiles")
    FILTER_TYPE = os.environ.get("FILTER_TYPE", "video")
    OWNER_ID = os.environ.get("OWNER_ID", "2056407064")
    LIMIT = int(os.environ.get("LIMIT", "1000000"))
    SKIP_NO = int(os.environ.get("SKIP_NO", "0"))
    SESSION = os.environ.get("SESSION", "BQE45_EAMODUWefKh2pAjdotR6sSHf-lsJs2zqQmQZh-ALg1QdSFndoWAr9h3xtCW3Tiy9QIqTzFy1t9owQn-q6FHBRiz3nuBsfprVGxp5zqpWRFnrL3Ui06PZX3ONHZu-v4LH9f_LnakWGhauIWCAL-JjQl0aG_IEDm2P9wDC-fIVZbZG6AFx2cTLXZ9YHfA04LoD0EvfiSmm2tTPNmu1oSMKoXBob8MEMnITCh4HK2wzRJLnBAW3dNgauHidAOLPT5LWycntjScr55fnSeJTmbd74395KFTwbVr6iEVbXm9mjawvdB7VjTnAxIu4TZJgWakQrqSBUD4ovolbhnNgIMJfz08wAAAAFhVMVfAA")
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", "-1001837099658"))
def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
