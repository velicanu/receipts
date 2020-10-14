import pandas as pd


def df_from_textract(response):
    """
    returns a df from a textract repsonse

    The relevant part of the repsonse looks like:
    {
        "DocumentMetadata": {"Pages": 1},
        "Blocks": [
            {
                {
                    "BlockType": "LINE",
                    "Text": "HERB BASIL 2.5 OZ",
                },
                {
                    "BlockType": "LINE",
                    "Text": "2.69",
                },
            }
        ],
    }
    """
    lines = [b for b in response["Blocks"] if b["BlockType"] == "LINE"]
    items = []
    for idx, line in enumerate(lines):
        if line["Text"].lower() == "subtotal":
            break
        next_line = lines[idx + 1]
        try:
            price = float(next_line["Text"])
            items.append({"item": line["Text"], "price": price})
        except ValueError:
            pass

    return pd.DataFrame.from_records(items)
