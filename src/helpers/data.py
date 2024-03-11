price = {
    "STANDART LC4 145±5 гр": 10500,
    "ECONOM LC3 145±5 гр": 9400
}

count_price = {
    "small": {
        1000: {"default": 950, "laque": 800},
        2000: {"default": 550, "laque": 500},
        3000: {"default": 400, "laque": 350},
        4000: {"default": 350, "laque": 300},
        5000: {"default": 300, "laque": 255},
        6000: {"default": 275, "laque": 245},
        7000: {"default": 265, "laque": 235},
        8000: {"default": 250, "laque": 225},
        9000: {"default": 240, "laque": 210},
        10000: {"default": 225, "laque": 200}
    },
    "large": {
        1000: {"default": 1100, "laque": 900},
        2000: {"default": 650, "laque": 600},
        3000: {"default": 450, "laque": 400},
        4000: {"default": 400, "laque": 350},
        5000: {"default": 350, "laque": 300},
        6000: {"default": 300, "laque": 275},
        7000: {"default": 285, "laque": 255},
        8000: {"default": 275, "laque": 245},
        9000: {"default": 270, "laque": 235},
        10000: {"default": 250, "laque": 225}
    }
}


def get_price_key(count: int) -> int:
    if 1000 <= count < 2000:
        return 1000
    elif 2000 <= count < 3000:
        return 2000
    elif 3000 <= count < 4000:
        return 3000
    elif 4000 <= count < 5000:
        return 4000
    elif 5000 <= count < 6000:
        return 5000
    elif 6000 <= count < 7000:
        return 6000
    elif 7000 <= count < 8000:
        return 7000
    elif 8000 <= count < 9000:
        return 8000
    elif 9000 <= count < 10000:
        return 9000
    elif count >= 10000:
        return 10000
    else:
        return None


def get_sheet_price(count: int, width: int, height: int):
    size = "small" if width <= 105 and height <= 75 else "large"
    price_per_sheet = count_price[size].get(get_price_key(count), None).get("default")
    if price_per_sheet is not None:
        return price_per_sheet
    else:
        return "Price not available for the given print run and size"


def get_lacquer_price(count: int, width: int, height: int):
    size = "small" if width <= 105 and height <= 75 else "large"
    price_per_sheet = count_price[size].get(get_price_key(count), None).get("laque")
    if price_per_sheet is not None:
        return price_per_sheet
    else:
        return "Price not available for the given print run and size"


def format_number(number: float):
    # Convert number to string and reverse it for easier manipulation
    num_str = str(int(number))[::-1]
    formatted_str = ""

    # Iterate through the reversed string and add spaces every three digits
    for i in range(len(num_str)):
        if i > 0 and i % 3 == 0:
            formatted_str += " "
        formatted_str += num_str[i]

    # Reverse back the formatted string and return
    return formatted_str[::-1]
