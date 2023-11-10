import pandas as pd
import requests

import requests

# from .models import Car
from googletrans import Translator, LANGUAGES

# Global dictionary for color translations
color_translation = {}


def translate_text(text, target_lang="en"):
    translator = Translator()
    try:
        translation = translator.translate(text, dest=target_lang)
        return translation.text
    except Exception as e:
        print(f"Error during translation: {e}")
        return text


def fetch_car_data_as_dataframe(brand, model):
    base_url = "https://bama.ir/cad/api/search"
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
    }
    page_index = 0
    all_cars = []

    while True:
        print(f"Analyzing page: {page_index}")
        params = {"vehicle": f"{brand},{model}", "pageIndex": page_index}
        response = requests.get(base_url, headers=headers, params=params)

        if response.status_code != 200 or not response.json()["data"]["ads"]:
            break

        data = response.json()
        for ad in data["data"]["ads"]:
            try:
                # if ad['type'] == 'ad':
                car_detail = ad["detail"]
                price_text = ad.get("price", {}).get("price", "0").replace(",", "")
                price = float(price_text) if price_text.isdigit() else 0
                mileage_text = car_detail["mileage"]
                mileage = (
                    0
                    if "صفر" in mileage_text
                    else int("".join(filter(str.isdigit, mileage_text)))
                )
                color_body = car_detail["body_color"]
                if color_body not in color_translation:
                    translated_color = translate_text(color_body)
                    color_translation[color_body] = translated_color
                all_cars.append(
                    {
                        "brand": brand,
                        "model": model,
                        "color_body": color_translation[color_body],
                        "mileage": mileage,
                        "year": car_detail["year"],
                        "price": price,
                    }
                )
            except Exception as e:
                print(f"An error occurred on page {page_index}: {e}")
                continue

        if not data["metadata"]["has_next"]:
            break
        page_index += 1
    return pd.DataFrame(all_cars)
