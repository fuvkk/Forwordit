#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Dark Angel

import os
import logging

class Config:
    
    API_ID = int(os.environ.get("API_ID", "10098309"))
    API_HASH = os.environ.get("API_HASH", "aaacac243dddc9f0433c89cab8efe323")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5473067352:AAHMEGb37UGorEcmgi_43YW5AQ9VjEQXuR4") 
    BOT_SESSION = os.environ.get("BOT_SESSION", "bot") 
    CAPTION = os.environ.get("CAPTION", "")
    FROM_CHANNEL = os.environ.get("FROM_CHANNEL", "@OkFiles")
    FILTER_TYPE = os.environ.get("FILTER_TYPE", "video")
    OWNER_ID = os.environ.get("OWNER_ID", "2056407064")
    LIMIT = int(os.environ.get("LIMIT", "700000"))
    SKIP_NO = int(os.environ.get("SKIP_NO", "0"))
    SESSION = os.environ.get("SESSION", "BQE45_EAA5JNTw2uFcGlV-h3VQ4IefkebZf4d4arKR_yZeAp5236ggMsTAZQIzzzllq9DaRjl6ME04zIxwqLGzI4ebR7OPpMiecjBxxNIHXylH8sa52AsdeokeKBF1HvhepTTiKquu8hmQp6AIXUqs9QUgMNheQsyj1LCWVokf254cmwtkoWfFFMuWscSnztgvjc02e4Mp4hOkcxY49Oj-m3LCmWXuY6w8RLxEeCoGiah_brLVPk8fEKaWZklqN_WOSV4HRwZiXKMXJOlT_yRE48cf92GLQ1c7_1XVM9r6fESIUyiOtp_I_v7PU1CYq4fV-J9zW8KomocLqfJOhYqlICMcsKZgAAAAFhVMVfAA")
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", "-1001837099658"))
def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
