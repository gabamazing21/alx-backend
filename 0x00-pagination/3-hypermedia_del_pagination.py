#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """ Deletion-resilient hypermedia pagination

            Args:
                index: the starting index
                page_size(int): number of item in a page
            Return:
                Dict: index, data, page_size, next_index
           """
        dataset = self.indexed_dataset()
        max_index = max(dataset.keys())
        if (index >= max_index or not isinstance(index, int)):
            raise AssertionError
        if (index < 0):
            raise AssertionError
        hyper_index_dict = {}
        dataset = self.indexed_dataset()
        data = []
        current_index = index
        while len(data) < page_size and current_index <= max_index:
            if current_index in dataset:
                data.append(dataset[current_index])
            current_index += 1

        hyper_index_dict["index"] = index
        hyper_index_dict["data"] = data
        hyper_index_dict["page_size"] = len(data)
        hyper_index_dict["next_index"] = current_index

        return hyper_index_dict
