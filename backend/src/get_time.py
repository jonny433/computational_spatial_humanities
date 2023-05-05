import time
import logging
import pandas as pd

from db.db import DB

logger = logging.getLogger(__name__)

def get_time(name):
    logger.info("TEST Loger")
    db = DB()
    test = db.execute_query("""
                           SELECT * FROM vendors
                            """)
    return test

#  INSERT INTO vendors(vendor_name) VALUES("Jonny")