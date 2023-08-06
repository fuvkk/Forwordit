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
    FROM_CHANNEL = os.environ.get("FROM_CHANNEL", "@cigutg")
    FILTER_TYPE = os.environ.get("FILTER_TYPE", "video")
    OWNER_ID = os.environ.get("OWNER_ID", "2056407064")
    LIMIT = int(os.environ.get("LIMIT", "25000"))
    SKIP_NO = int(os.environ.get("SKIP_NO", "0"))
    SESSION = os.environ.get("SESSION", "BQBCa_j9IuaXuwWqmX6aCxAmLllIdj5Dus00gUDw3ekpZiSOIuSl4xY3mib0gjAIaG-GXI02IsHRJYFnZftfwElFU4R1DaZxIQjkhqvosMIL47ixaKaAtoZcHlmjbtgx8-16XBdwhGc2ECm8jmTdLxi76vj72ijo3bi_QndSdKM3mrZegULpDMVAb8egASKytZmH0CgQrpg3f3LllRquIG3vQ-Lxh51O4hIXut9X3f3a_aycHgGus7UEIadYVneoKV8DiDy51cI_Sv9FNSOsAfYe10YNbdIMNh1RyBoOgCjT6aQaAFvTMzjCbsSNeE1DcsdXgy2G5hfM6WWpayrlWXlmAAAAAWFUxV8A")
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", "-1001580057771"))
def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
