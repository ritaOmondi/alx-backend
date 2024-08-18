#!/usr/bin/env python3
def index_range(page, page_size):
  """
  This function returns a tuple of size two containing the start and end indexes
  corresponding to the range of indexes to return in a list for those particular
  pagination parameters.

  Args:
    page: The current page number (1-indexed).
    page_size: The number of items per page.

  Returns:
    A tuple containing the start and end indexes.
  """
  start_index = (page - 1) * page_size
  end_index = start_index + page_size
  return (start_index, end_index)
