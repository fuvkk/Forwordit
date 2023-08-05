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
    SESSION = os.environ.get("SESSION", "BQAyaBSLPzKH89dXKeQvibaUgrzqIZo-todwUGajANstUsQO6YZX4n5bDPOhoEmd-SZDrTUG2oJPTdi04NYx8w5USQaioQVsWyGGqAChAmujS8gPDJPj93HWzr4e83y87TMAdgKFORuOxV6ulFz0oipdGZ15niIL57_Pzef2YLwM4xMDoKh18E3wfngPBYUf-lrYkH-odvXeQaXp06ATFGvZbsFz-aEuB410CTeUkGBgfCjcXZ3sLGzOee_KRjKjzvCkQDWeiDlpiN8HOX_KbHBbdnCgeUzjRQCBzgEIqnKiVT9iloHs8Hx2tXrQXclVRZitziPm44uRRJYg_5_FVvVkAAAAAWFUxV8A")
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", "-1001780263517"))
def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
