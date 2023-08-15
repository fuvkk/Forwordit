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
    LIMIT = int(os.environ.get("LIMIT", "700000"))
    SKIP_NO = int(os.environ.get("SKIP_NO", "0"))
    SESSION = os.environ.get("SESSION", "BQE45_EAePhCWCBMpE9I9NJ6jIysRC4od9tf1_xIGzSvXjAPThrqK42SyrxEEoS7kPzIM4zlTVuQzNh2xe_lc0sPHQ14f_Z-gtmc1iG1sWNsdtct3Rqy5dRR2pA191dNLsD10ddeFcrni4vwt4aGFydlCSta_So9ZXCVPVunORNibC3eoMxV4WgYNNYQpKzmh0uzMKu1PdaALXueO_b7OfVTHbkfLwMmdfagURfDPoAUaqQ25BVw5gL8dvaOLQPW9hMDG6wfky4yC-afUKAQaIIN-zWagpxLC7PEB8RQalqzYXe3rrHbQQKK6MsODDAVOEdw31NvPc0o-zj3kRwvaGgIpirwAAAAFhVMVfAA")
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", "-1001837099658"))
def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
