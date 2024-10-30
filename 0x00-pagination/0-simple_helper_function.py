#!/usr/bin/env python3
"""module that create pagination index"""


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
