import json
import logging

logging.basicConfig(level=logging.INFO)


def read_json(file: str):
    """The function of reading data from a json file
    Args:
      file: path to the file
    Returns:
      parameters from json file
    """
    try:
        with open(file, "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        print("File with settings not found")
        return
    except Exception as e:
        logging.error(f'[reading_from_json]: {e}')
        return

    return data


def write_json(path: str, data):
    try:
        with open(path, "w", encoding="utf-8") as file:
            json.dump({"card_number": data}, file)
    except FileNotFoundError:
        print("File with settings not found")
        return
    except Exception as e:
        logging.error(f'[writing_to_json]: {e}')
        return
