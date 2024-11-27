from settings import *
import requests
from requests.exceptions import RequestException
import pandas as pd
from storage import DB_storage
from urllib.parse import quote_plus

def search_api(query, pages = int(RESULT_COUNT/10)):
    result = []
    for i in range (0, pages):
        start = i * 10 + i
        url = SEARCH_URL.format(
            key = SEARCH_KEY,
            cx = SEARCH_ID,
            query = quote_plus(query),
            start = start
        )
        response =  requests.get(url)
        data = response.json()

        result += data["items"]

    res_df = pd.DataFrame.from_dict(result)
    res_df["rank"] = list(range(1, res_df.shape[0] + 1))
    res_df = res_df[["link", "rank", "snippet", "title"]]
    return res_df