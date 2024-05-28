import os
import argparse

from func import number_search, luna_algorithm, analysis_time_search_hash_collision
from work_files import *

logging.basicConfig(level=logging.INFO)


def main():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-s', '--settings', type=str,
                        default=os.path.join('settings.json'), help='Path to the settings file')
    args = parser.parse_args()

    try:
        settings = read_json(args.settings)

        bins = settings.get("bins")
        hash_value = settings.get("hash")
        last_digits = settings.get("last_digits")
        save_path = settings.get("save_path")

        print(settings)

        if not bins or not hash_value or not last_digits or not save_path:
            logging.error("Invalid settings file.")
            exit(1)

        result = number_search(save_path, hash_value, last_digits, bins)

        if result:
            if luna_algorithm(result):
                logging.info("The card number is valid according to the Luhn algorithm.")
            else:
                logging.info("The card number is invalid according to the Luhn algorithm.")

        analysis_time_search_hash_collision(hash_value, last_digits, bins)

    except Exception as ex:
        logging.error(f"An error occurred: {ex}")


if __name__ == "__main__":
    main()
