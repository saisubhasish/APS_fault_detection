import pymongo
import pandas as pd
import json
from dataclasses import dataclass
# 
import os



# Provide the mongodb localhost url to connect to mongodb
client = pymongo.MongoClient()