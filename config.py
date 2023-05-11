#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Dark Angel

import os
import logging

class Config:
    
    API_ID = int(os.environ.get("API_ID", "10098309"))
    API_HASH = os.environ.get("API_HASH", "aaacac243dddc9f0433c89cab8efe323")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5457862323:AAEqZqChDW0MckF0vZQ_ck_DGNM1tE-efVs") 
    BOT_SESSION = os.environ.get("BOT_SESSION", "bot") 
    CAPTION = os.environ.get("CAPTION", "")
    FROM_CHANNEL = os.environ.get("FROM_CHANNEL", "@cigutg")
    FILTER_TYPE = os.environ.get("FILTER_TYPE", "video")
    OWNER_ID = os.environ.get("OWNER_ID", "2056407064")
    LIMIT = int(os.environ.get("LIMIT", "25000"))
    SKIP_NO = int(os.environ.get("SKIP_NO", "0"))
    SESSION = os.environ.get("SESSION", "BQAZbveeYDQDkJJkOH6rffMbAsFy3dJ7OhZoML3i4hqmrSTgw6iBszRNQXwitoeKgtjXx6z47EZV3Rn_c2xXta9Lrx7M1zT5mzXjeyuOLXTDqZ8cves8ScZHPIc1VILDsFiYqecLX1f1rmnVA9uesnwduz3NoElhvnaszuxMSWgbK6lJvTrZ_h50_vXGauGjxrH1ri5uGrNWhOvnVsW7HgfuG7gmkoQ95w8ssNFfP7AxKNq-bQgp943hQY09ZmO4SCr5X-ZlvvF2Ek6f2dXUnzV472WwBKNLOrRkHmX0yRTSQpMP7uD-BVCNb0Kuls1tAuqfGGS0ob3cAoaqWe-IOs07AAAAAWFUxV8A")
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", "-1001976377129"))
def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
