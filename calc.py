import logging


# def add(a, b):
#   return a + b

def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    try:
        a / b
        logging.info(f"Succesful divide {a} / {b}")
        return a / b
    except ZeroDivisionError as err:
        logging.error("Na nol ne deli!!!", exc_info=True)
        return 0


def add(a, b):
    return a ** 2 + b ** 2


def sqrt(a):
    try:
        if a > 0:
            a ** 0.5
            logging.info(f"Succesful sqrt {a}**0.5")
            return a ** 0.5
        else:
            raise Exception(f"{a} не может быть отрицательным числом!!!")
    except Exception:
        logging.error(f"Квадрат любого числа - всегда неотрицательное число!!!", exc_info=True)
        return 0


def pow(a, b):
    return a ** b


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, filemode='w', encoding='utf-8', filename='py.log',
                        format="%(asctime)s | %(levelname)s | %(message)s")
    print(div(3, 4))
    print(div(3, 0))

    print(sqrt(4))
    print(sqrt(-4))
    print(4 ** 0.5)
