#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Dark Angel

import os
import logging

class Config:
    
    API_ID = int(os.environ.get("API_ID", 10098309))
    API_HASH = os.environ.get("API_HASH", "aaacac243dddc9f0433c89cab8efe323")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5341317942:AAFIPvtSBjf9eYEBK-GzDiuUejr9pwEViOc") 
    BOT_SESSION = os.environ.get("BOT_SESSION", "bot") 
    CAPTION = os.environ.get("CAPTION", "")
    FROM_CHANNEL = os.environ.get("FROM_CHANNEL", "@HEGGHEGE")
    FILTER_TYPE = os.environ.get("FILTER_TYPE", "video")
    OWNER_ID = os.environ.get("OWNER_ID", "2056407064")
    LIMIT = int(os.environ.get("LIMIT", "25000"))
    SKIP_NO = int(os.environ.get("SKIP_NO", "0"))
    SESSION = os.environ.get("SESSION", "BQCAZ_bkUn8s_8VcE9jQ-g-a2PsstkcuLyWyYeo8JDixVgyJ5Y5jopggmPT830nvGCofh2iQaRrD2KN410gqIEUN9UdD_7LVm0gfSdw_nLs92I7l7r58L1Claao-JGnqtr0U9UfRQ0c5SWm_5DkDozryo_5jMjU1ZPDBxTOa9SjEYYahR6BKapcfN7rKghSjKO8vi7VyTU8wrPx9vRS8mQ51rx3hnqCkLkh6MD171sqhtmLOQ0qyoO7NT-YpxDzTNBMZNsoamsRgnws84Q3Ve4tAHfbvOPgRtXt22SZgoQS1tUieBBCa_1g772uscfPcnLwnJtotZbXR-6G9DBq_7q1pAAAAAHqSSBgA")
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", "-1001541366034"))
def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
