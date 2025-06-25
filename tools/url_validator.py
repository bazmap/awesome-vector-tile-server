import json
import requests
import time



def validate_urls(data):
    if isinstance(data, dict):
        for key, value in data.items():
            # URL only in objets stored in a key finishing with "-url"
            if key.endswith("-url") and isinstance(value, dict):

                url = value.get("url")

                if url:
                    
                    # For URL with https://abc.xyz/{z}/{x}/{y}.yxz format : need to strip the end part
                    url = url.split("{z}/")[0]

                    try:
                        # Using the HEAD method to avoid downloading large files
                        response = requests.head(url, timeout=5)
                        value["active"] = True

                    except requests.RequestException:
                        try:
                            # Some URL needs to be requested with the GET method
                            response = requests.get(url, stream=True, timeout=5)
                            value["active"] = True

                            # Stopping the downloading after 5 second to avoid downloading large files
                            start = time.time()
                            for chunk in response.iter_content(chunk_size=1024):
                                if time.time() - start > 5:
                                    break

                        except requests.RequestException:
                            value["active"] = False

            else:
                validate_urls(value)

    elif isinstance(data, list):
        for item in data:
            validate_urls(item)

    return data



if __name__ == "__main__":

    list_file = ".\\vector-tile-server-list.json"

    with open(list_file, "r", encoding='utf-8') as f:
        data = json.load(f)

    updated_data = validate_urls(data)

    with open(list_file, "w", encoding='utf-8') as f:
        json.dump(updated_data, f, ensure_ascii=False, indent=2)