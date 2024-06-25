#!/usr/bin/env python3
"""Module that calculates the page
size and offset"""
import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Function that returns the start and end
    index based on page and page size

    Args:
        page (int): the size of page
        page_size (int): The items per page

    Return:
        returns tuple of start and end index
    """
    assert type(page) is int and page > 0
    assert type(page_size) is int and page_size > 0
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    res = (start_index, end_index)
    return res


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
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
        """Function to get the data of a particular set"""
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0
        ran = index_range(page, page_size)
        return self.dataset()[ran[0]: ran[1]]
