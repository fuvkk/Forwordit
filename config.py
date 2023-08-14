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
    SESSION = os.environ.get("SESSION", "1BVtsOIEBu2HFl_C4Gb0H3maGKWCBcH1S9ICGy3GwplK4QdySO9ptLBgeLWg0UZtw-hOCj9VnkXuSZ2PiVeKRn8RvJ8Ic8DfcaYyj-nyYaIbcqW-o2KrH5ziU7Lfp9tngbe-DRCifTLFvDlPPTgbuu8Yckx3MQ2TCezk-TcqbPDBWtL6xFfnlX62GRkR_SUMa16utzG4g1hA_N9SrriAIX4lh8LxqfcuqUgywKMTEZ-eymzurl8jKFLytknRwJjtNB-iSX1VLVwHZpCEPl8h27-i_j-OGSkSYMgXHFPkHx6fykT2rwKOILzrJrnOsUTF9_0GZfrRjpxHz8Jgxmmf9bHOBLTAZ6bY=")
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", "-1001837099658"))
def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
