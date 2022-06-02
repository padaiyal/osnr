def multiply_two_nums(num1: int, num2: int) -> int:
    """
    Multiply two numbers and return the result.
    :param num1: Number 1 used in the multiplication
    :type num1: int
    :param num2: Number 2 used in the multiplication
    :type num2: int
    :return: int: The result of the multiplication of num1 and num2
    :rtype: int
    """
    if num1 is None or num2 is None:
        raise AttributeError("Input number cannot be None!")

    if type(num1) != int or type(num2) != int:
        raise AttributeError("Both inputs have to be of type int.")

    return num1 * num2
