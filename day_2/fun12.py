from functools import reduce

transactions = [
    {"id": 1, "type": "income", "amount": 1000, "currency": "USD"},
    {"id": 2, "type": "expense", "amount": 200, "currency": "USD"},
    {"id": 3, "type": "income", "amount": 500, "currency": "USD"},
    {"id": 4, "type": "expense", "amount": 300, "currency": "USD"},
    {"id": 5, "type": "income", "amount": 700, "currency": "USD"},
    {"id": 6, "type": "expense", "amount": 400, "currency": "EUR"},
    {"id": 7, "type": "income", "amount": 100, "currency": "EUR"},
]


def filter_transactions(transactions, transaction_type):
    return list(filter(lambda x: x['type'] == transaction_type, transactions))


def map_transactions(transactions, currency):
    return list(map(lambda x: x['amount'] if x['currency'] == currency else 0, transactions))


def reduce_transactions(transactions):
    return reduce(lambda x, y: x + y, transactions, 0)


def process_transactions(transactions, transaction_type, currency):
    filtered = filter_transactions(transactions, transaction_type)
    mapped = map_transactions(filtered, currency)
    total = reduce_transactions(mapped)
    return total


print(process_transactions(transactions, "expense", "EUR"))  # 400
print(process_transactions(transactions, "income", "USD"))  # 2200


# def test_transaction_processing():
#     assert map_transactions(filter_transactions(transactions, "income"),"USD") == [1000, 500, 700, 0]

# pip install pytest
# C:\Users\CSComarch\PycharmProjects\PythonSrednio_21_05_2025\.venv\Scripts\python.exe "C:/Program Files/JetBrains/PyCharm Community Edition 2025.1/plugins/python-ce/helpers/pycharm/_jb_pytest_runner.py" --target fun12.py::test_transaction_processing
# Testing started at 12:34 ...
# Launching pytest with arguments fun12.py::test_transaction_processing --no-header --no-summary -q in C:\Users\CSComarch\PycharmProjects\PythonSrednio_21_05_2025\day_2
#
# ============================= test session starts =============================
# collecting ... collected 1 item
#
# fun12.py::test_transaction_processing PASSED                             [100%]
#
# ============================== 1 passed in 0.01s ==============================
#
# Process finished with exit code 0

