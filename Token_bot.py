import requests
import json
from config import cur


class ConvException(Exception):
    pass


class Converter:
    @staticmethod
    def convert(first: str, second: str, summ: str):

        if first == second:
            raise ConvException("Введены одинаковые валюты")

        try:
            first_ticker = cur[first]
        except KeyError:
            raise ConvException(f"Не удалось обработать - {cur[first]}")

        try:
            second_ticker = cur[second]
        except KeyError:
            raise ConvException(f"Не удалось обработать валюту - {cur[second]}")

        try:
            summ = int(summ)
        except ValueError:
            raise ConvException(f"Не удалось обработать количество - {summ}")
        response = requests.get(
            f"https://min-api.cryptocompare.com/data/price?fsym={first_ticker}&tsyms={second_ticker}")
        parsing = json.loads(response.content)[cur[second]]

        return parsing
