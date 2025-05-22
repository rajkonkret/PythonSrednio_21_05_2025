import fun12 as f12

transactions = [
    {"id": 1, "type": "income", "amount": 500, "currency": "USD"},
    {"id": 2, "type": "expense", "amount": 200, "currency": "USD"},
    {"id": 3, "type": "income", "amount": 500, "currency": "USD"},
    {"id": 4, "type": "expense", "amount": 300, "currency": "USD"},
    {"id": 5, "type": "income", "amount": 700, "currency": "USD"},
    {"id": 6, "type": "expense", "amount": 400, "currency": "EUR"},
    {"id": 7, "type": "income", "amount": 100, "currency": "EUR"},
]


def test_transaction_processing():
    assert f12.map_transactions(f12.filter_transactions(transactions, "income"), "USD") == [500, 500, 700, 0]
    assert f12.reduce_transactions([1000, 500, 700, 0]) == 2200

    print("All test passed")


def test_process():
    assert f12.process_transactions(transactions, "expense", "EUR") == 400

# (.venv) PS C:\Users\CSComarch\PycharmProjects\PythonSrednio_21_05_2025\day_2> pytest .\fun12_test.py
# ==================================================================================================== test session starts =====================================================================================================
# platform win32 -- Python 3.11.9, pytest-8.3.5, pluggy-1.6.0
# rootdir: C:\Users\CSComarch\PycharmProjects\PythonSrednio_21_05_2025\day_2
# collected 2 items
#
# fun12_test.py ..                                                                                                                                                                                                        [100%]
#
# ===================================================================================================== 2 passed in 0.01s ======================================================================================================
# (.venv) PS C:\Users\CSComarch\PycharmProjects\PythonSrednio_21_05_2025\day_2>
