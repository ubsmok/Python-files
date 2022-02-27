def is_even(number):
    return True if number % 2 == 0 else False


def print_board(s):
    print("=" * len(s))
    print(s)
    print("=" * len(s))


if __name__ == "__main__":
    print("Starting from itself...")