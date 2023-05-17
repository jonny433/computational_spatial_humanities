import time
import logging
import pandas as pd

from db.db import DB

logger = logging.getLogger(__name__)


data = {
    "lon": [52.4, 52.4],
    "lat": [91.5, 93.4]
}
df = pd.DataFrame(data)

db = DB()


def get_time(name):
    logger.info("TEST Loger")
    db = DB()

    return name


#  INSERT INTO vendors(vendor_name) VALUES("Jonny")