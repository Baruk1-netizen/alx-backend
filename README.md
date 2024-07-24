# ALX Backend Project

Welcome to the ALX Backend Project repository! This repository contains a collection of projects designed to help you develop and demonstrate your backend skills using Python. The focus is on creating efficient and scalable backend solutions with practical applications.

## Projects

### 0. Simple Helper Function

- **File:** `0-simple_helper_function.py`
- **Description:** Provides a helper function `index_range` to compute the start and end indices for pagination based on a given page number and page size.

### 1. Simple Pagination

- **File:** `1-simple_pagination.py`
- **Description:** Implements a `Server` class that paginates a dataset of popular baby names. The `get_page` method retrieves a specific page of data, allowing for basic pagination functionality.

### 2. Hypermedia Pagination

- **File:** `2-hypermedia_pagination.py`
- **Description:** Extends the `Server` class from the previous project to include hypermedia pagination. The `get_hyper` method returns additional metadata alongside the paginated data, such as the next and previous page numbers.

### 3. Deletion-Resilient Hypermedia Pagination

- **File:** `3-hypermedia_del_pagination.py`
- **Description:** Further extends pagination to handle scenarios where data may be deleted between requests. The `get_hyper_index` method ensures that pagination remains accurate even if rows are removed from the dataset.

## Usage

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/your-username/alx-backend.git
   ```

2. **Navigate to the Project Directory:**

   ```bash
   cd alx-backend
   ```

3. **Run the Main Files:**

   Each project contains a `main` file that demonstrates its functionality. For example, to run the `get_page` method from the Simple Pagination project:

   ```bash
   python3 1-main.py
   ```

## Requirements

- Python 3.x
- Modules: `csv`, `math` (for specific projects)

## Author

Baruk1-netizen

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
