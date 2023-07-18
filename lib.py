import requests

def count_word_at_url(url):
    """
    это функция для примера как вызывает async
    :param url:
    :return:
    """
    response = requests.get(url)

    print(len(response.text.split()))
    return len(response.text.split())