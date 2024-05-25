import json
import pickle


def read_text(path: str):
    """The function of reading text from file
    Args:
      path: path to the file
    Returns:
      text from the file
    """
    try:
        with open(path, 'r', encoding='UTF-8') as f:
            text = f.read().lower()
        return text
    except FileNotFoundError:
        return "File with data not found"
    except Exception as e:
        return f"Error reading file: {str(e)}"


def write_text(path: str, text: str):
    """The function of writing information to file
    Args:
      path: path to the file
      text: written text
    """
    try:
        with open(path, 'w', encoding='UTF-8') as f:
            f.write(text)
    except FileNotFoundError:
        print("Incorrect path to the directory")
    except Exception as e:
        print(f"Error writing to file: {str(e)}.")


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
        print(f"Error reading file {str(e)}")
        return

    return data


def write_binary(path: str, data):
    """The function of writing information to file
    Args:
      path: path to the file
      data: written data
    """
    try:
        with open(path, 'wb') as f:
            f.write(data)
    except FileNotFoundError:
        print("Incorrect path to the directory")
    except Exception as e:
        print(f"Error writing to file: {str(e)}.")


def read_binary(path: str):
    """The function of reading data from file
    Args:
      path: path to the file
    Returns:
      data from the file
    """
    try:
        with open(path, 'rb') as f:
            data = f.read()
        return data
    except FileNotFoundError:
        return "File with data not found"
    except Exception as e:
        return f"Error reading file: {str(e)}"


def write_encrypt(path: str, data):
    """The function of writing encrypt information to file
    Args:
      path: path to the file
      data: written encrypt data
    """
    try:
        with open(path, 'wb') as f:
            pickle.dump(data, f)
    except FileNotFoundError:
        print("Incorrect path to the directory")
    except Exception as e:
        print(f"Error writing to file: {str(e)}.")


def read_encrypt(path: str):
    """The function of reading data from file
    Args:
      path: path to the file
    Returns:
      data from the file
    """
    try:
        with open(path, 'rb') as f:
            data = pickle.load(f)
        return data
    except FileNotFoundError:
        return "File with data not found"
    except Exception as e:
        return f"Error reading file: {str(e)}"


def write_decrypt(path: str, data):
    """The function of writing information to file
    Args:
      path: path to the file
      data: written data
    """
    try:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(data.decode('utf-8'))
    except FileNotFoundError:
        print("Incorrect path to the directory")
    except Exception as e:
        print(f"Error writing to file: {str(e)}.")
