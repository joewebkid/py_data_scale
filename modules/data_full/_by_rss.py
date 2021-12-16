import pandas as pd
from modules.api_func.mongo_api import apiMongoConnect
import pandas_read_xml as pdx


df = pdx.read_xml("https://towardsdatascience.com/feed")

orderedDictList = df.rss[0]["channel"]["item"]
dataf = pd.DataFrame(orderedDictList)

json_date = dataf.T.to_json()

# apiMongoConnect.req("")