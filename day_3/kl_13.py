# błedy, wyjątki
try:
    print(2 / 0)
# Traceback (most recent call last):
#   File "C:\Users\CSComarch\PycharmProjects\PythonSrednio_21_05_2025\day_3\kl_13.py", line 2, in <module>
#     print(2 / 0)
#           ~~^~~
# ZeroDivisionError: division by zero
#
# Process finished with exit code 1 - oznacza błąd
except ZeroDivisionError:
    print("Nie dziel przez zero")
else:
    print("Gdy nie błedu")
finally:
    print("Wykona się zawsze")
print("program nadal działa")


# Nie dziel przez zero
# Wykona się zawsze
# program nadal działa

class MyException(Exception):
    def __init__(self, message):
        super().__init__(message)


try:
    x = int(input("Podaj liczbę całkowitą większą od zera"))
    if x <= 0:
        raise MyException("Liczba musi być większa od zera")  # raise - rzucenie wyjątku
except MyException:
    print("Wartość musi być większa od zera")
except Exception as e:
    print("Bład", e)
else:
    print("Podana wartośc", x)
finally:
    print("Koniec")
