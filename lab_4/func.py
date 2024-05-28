import hashlib
import multiprocessing as mp
import time

from tqdm import tqdm
from matplotlib import pyplot as plt
from work_files import *

logging.basicConfig(level=logging.INFO)


def check_number_card(tested_part: int, hash: str, last_digits: str, bins: list) -> str | None:
    """
    Function compares the card number with a specified number for match
    args:
        tested_part: generated part for testing
        hash: hash that must be checked
        last_digits: last 4 digits of the card number
        bins: list of BINs
    return:
        card_number: matched with hash number of card OR
        None: if not matched
    """
    for bin in bins:
        card_number = f'{bin}{tested_part:06d}{last_digits}'
        if hashlib.sha1(card_number.encode()).hexdigest() == hash:
            logging.info(f"Match found: {card_number}")
            return card_number
    return None


def number_search(save_path: str, hash: str, last_digits: str, bins: list) -> str:
    """
    Function uses parallel processing with the help of a process pool to search
    for the card number according to the given hash
    args:
        save_path: path to save the search results
        hash: hash that must be checked
        last_digits: last 4 digits of the card number
        bins: list of BINs
    return:
        card_numbers: found card number
    """
    card_numbers = None
    with mp.Pool(mp.cpu_count()) as p:
        for result in p.starmap(check_number_card, [(i, hash, last_digits, bins) for i in range(0, 1000000)]):
            if result is not None:
                card_numbers = result
                break
    try:
        write_json(save_path, card_numbers)
    except Exception as ex:
        logging.error(ex)
    return card_numbers


def luna_algorithm(card_number: str) -> bool:
    """
    The function verify the correctness of the credit card number with the Luna algorithm
    args:
        card_number: matched with hash number of card
    return:
        result of the check
    """
    try:
        card_number_list = [int(char) for char in card_number]
        for i in range(len(card_number_list) - 2, -1, -2):
            card_number_list[i] *= 2
            if card_number_list[i] > 9:
                card_number_list[i] -= 9
        return sum(card_number_list) % 10 == 0
    except Exception as ex:
        logging.error(ex)
        return False
    

def analysis_time_search_hash_collision(hash: str, last_digits: str, bins: list) -> None:
    """
    The function analyzes the time to search for hash collisions
    depending on the number of processes
    args:
        hash: hash of number
        last_digits: last 4 digits of card's number
        bins: list of BINs
    """
    try:
        times = []
        num_cores = int(mp.cpu_count() * 1.5)
        
        for i in tqdm(range(1, num_cores + 1), desc='Search of collisions'):
            start_time = time.time()
            with mp.Pool(i) as pool:
                results = pool.starmap(check_number_card, [(j, hash, last_digits, bins) for j in range(1000000)])
                for result in results:
                    if result is not None:
                        break
            elapsed_time = time.time() - start_time
            times.append(elapsed_time)
        
        plt.plot(range(1, num_cores + 1), times, color="blue", marker=".", markersize=5)
        plt.xlabel("Number of processes")
        plt.ylabel("Time, sec")
        plt.title("Graph of dependence between time and number of processes")
        plt.show()
    except Exception as ex:
        logging.error(ex)
