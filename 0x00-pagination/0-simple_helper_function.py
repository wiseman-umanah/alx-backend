#!/usr/bin/env python3
"""Module that calculates the page
size and offset"""
from typing import Tuple


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
