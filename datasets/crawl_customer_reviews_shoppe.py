import re
import json
import requests
import pandas as pd


url = "https://shopee.vn/Qu%E1%BA%A7n-short-%C4%91%C3%B9i-n%E1%BB%AF-c%E1%BA%A1p-cao-ch%E1%BA%A5t-tuy%E1%BA%BFt-m%C6%B0a-i.290065942.6244070348?sp_atk=f3ad5a0f-3ee2-431a-9529-3b00499a0445"

r = re.search(r"i\.(\d+)\.(\d+)", url)
shop_id, item_id = r[1], r[2]
ratings_url = "https://shopee.vn/api/v2/item/get_ratings?filter=0&flag=1&itemid={item_id}&limit=20&offset={offset}&shopid={shop_id}&type=0"

offset = 0
d = {"username": [], "rating": [], "comment": []}
while True:
    data = requests.get(
        ratings_url.format(shop_id=shop_id, item_id=item_id, offset=offset)
    ).json()

    # uncomment this to print all data:
    # print(json.dumps(data, indent=4))
    # leng enumerate tra ket qua duoi dang liet ke
    i = 1
    for i, rating in enumerate(data["data"]["ratings"], 1):
        d["username"].append(rating["author_username"])
        d["rating"].append(rating["rating_star"])
        d["comment"].append(rating["comment"])

        print(rating["author_username"])
        print(rating["rating_star"])
        print(rating["comment"])
        print("-" * 100)

    if i % 20:
        break

    offset += 20

    df = pd.DataFrame(d)
    print(df)
    df.to_csv("data.csv", index=False)
