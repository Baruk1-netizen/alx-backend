# Pagination Project README

## Overview

This repository provides a set of Python utilities for paginating large datasets. It demonstrates various techniques to handle pagination including simple pagination, hypermedia pagination, and deletion-resilient hypermedia pagination.

## Files

1. **0-simple_helper_function.py**
   - Contains a helper function `index_range` which calculates the start and end indices for pagination.

2. **1-simple_pagination.py**
   - Implements the `Server` class to paginate a dataset of popular baby names. This class includes a `get_page` method that retrieves a specific page of the dataset.

3. **2-hypermedia_pagination.py**
   - Extends the `Server` class to include hypermedia pagination. The `get_hyper` method returns additional metadata along with the paginated data.

4. **3-hypermedia_del_pagination.py**
   - Further extends pagination to be deletion-resilient. The `get_hyper_index` method ensures that pagination remains accurate even if data is deleted between requests.

## Usage

### 0. Simple Helper Function

The `index_range` function takes two arguments:
- `page` (int): The page number (1-indexed).
- `page_size` (int): The number of items per page.

It returns a tuple `(start_index, end_index)`.

Example:
```python
index_range(1, 7)  # Returns (0, 7)
index_range(3, 15) # Returns (30, 45)
```

### 1. Simple Pagination

The `Server` class provides a `get_page` method:
- `page` (int): The page number (default is 1).
- `page_size` (int): The number of items per page (default is 10).

It returns a list of rows for the specified page.

### 2. Hypermedia Pagination

The `Server` class includes a `get_hyper` method:
- `page` (int): The page number (default is 1).
- `page_size` (int): The number of items per page (default is 10).

It returns a dictionary with the following keys:
- `page_size`: The length of the returned dataset page.
- `page`: The current page number.
- `data`: The dataset page.
- `next_page`: The number of the next page (or `None` if there is no next page).
- `prev_page`: The number of the previous page (or `None` if there is no previous page).
- `total_pages`: The total number of pages in the dataset.

### 3. Deletion-Resilient Hypermedia Pagination

The `Server` class now includes a `get_hyper_index` method:
- `index` (int): The starting index for the current page (default is `None`).
- `page_size` (int): The number of items per page (default is 10).

It returns a dictionary with the following keys:
- `index`: The current start index of the return page.
- `next_index`: The next index to query.
- `page_size`: The current page size.
- `data`: The actual page of the dataset.

The method ensures that even if rows are deleted, the pagination remains consistent.

## Requirements

- Python 3.x
- `csv` module
- `math` module

## Author

Baruk1-netizen

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
