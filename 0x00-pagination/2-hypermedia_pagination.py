#!/usr/bin/env python3
"""module that Hypermedia pagination"""


import csv
import math
from typing import List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """ initialize the private attribute"""
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ get the list in that particular page

            Args:
                page_numer(int): the current page numer (1 - indexed)
                page_size(int): number of item in a page
            Return:
                List: A list of the current page
           """
        if (not isinstance(page, int) or not isinstance(page_size, int)):
            raise AssertionError
        if (page <= 0 or page_size <= 0):
            raise AssertionError
        a, b = index_range(page, page_size)
        page_list = self.dataset()
        if a >= len(page_list) or b > len(page_list):
            return []
        return page_list[a:b]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        total_page = math.ceil(len(self.dataset()) / page_size)
        hyper_dict = {}
        hyper_dict["page_size"] = page_size
        hyper_dict["page"] = page
        hyper_dict["data"] = self.get_page(page, page_size)
        hyper_dict["next_page"] = page + 1 if page < total_page else None
        hyper_dict["prev_page"] = page - 1 if page > 1 else None
        hyper_dict["total_page"] = total_page
        return hyper_dict


def index_range(page, page_size):
    """
    calculate the start and end indice of a given page numer

    Args:
        page_numer(int): the current page numer (1 - indexed)
        page_size(int): number of item in a page
    Return:
        tuple: A tuple of start and end index
    """
    if (page < 1 or page_size < 1):
        return ValueError("Page number and page size must be greater than 0")
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)
