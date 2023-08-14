#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Dark Angel

import os
import logging

class Config:
    
    API_ID = int(os.environ.get("API_ID", "10098309"))
    API_HASH = os.environ.get("API_HASH", "aaacac243dddc9f0433c89cab8efe323")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5567435254:AAEDn9yL-YYXyfI_O3glYrS3AC-SRU5XcN8") 
    BOT_SESSION = os.environ.get("BOT_SESSION", "bot") 
    CAPTION = os.environ.get("CAPTION", "")
    FROM_CHANNEL = os.environ.get("FROM_CHANNEL", "@OkFiles")
    FILTER_TYPE = os.environ.get("FILTER_TYPE", "video")
    OWNER_ID = os.environ.get("OWNER_ID", "2056407064")
    LIMIT = int(os.environ.get("LIMIT", "700000"))
    SKIP_NO = int(os.environ.get("SKIP_NO", "0"))
    SESSION = os.environ.get("SESSION", "BQE45_EAvHijDTUd41ruboYQ0kD9NnDvzSn07SaBQh8NLTwxS-5_TunGgwCgRX3R3Z9UpwGvLrc8EnsAL4ZV5GenhClUsWDzJ3VNUlhxaShRERdjmXYLXDhNlJw3Zbkjqnq45nv0OR7aTkjZs2Dix7EO8CaCkJW00bQMKeUvMVTi8tFoxcjqaHzsvhN0e4GJe_WjwD71fqmqWtpbAU45whE4eYqdbsgQZcAE7qc152LpJ5lBAIE2tJbPnuEnYOnSTk_-va_f5Vqjq9FvgxG03zfy6jSHfWQ0qWDJ0nhJiBh0QD-2ouiwlYJ_9jaK_n8F1Pg1hsjjdCnrh6-5BYZOiuGb0DO_BQAAAAFhVMVfAA")
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", "-1001872901173"))
def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
