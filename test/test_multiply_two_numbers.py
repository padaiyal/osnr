import unittest
from multiply_two_numbers import multiply_two_nums


class MultiplyTwoNumsTest(unittest.TestCase):

    def test_multiplication(self) -> None:
        """
        Tests the multiply_two_numbers() method for the following
        input combinations.
        [-2,-2] : 4
        [2,-2] : -4
        [2,2] : 4
        [3, 0] : 0
        [2, "iha"] : AttributeError
        [2, 2.5] : AttributeError
        [None, 3] : AttributeError
        """

        test_inputs: dict = {
            20: [-4, -5],
            -4: [2, -2],
            7: [7, 1],
            0: [3, 0]
        }

        for expected_value, inputs in test_inputs.items():
            self.assertEqual(
                expected_value,
                multiply_two_nums(inputs[0], inputs[1])
            )

        self.assertRaises(AttributeError, multiply_two_nums, None, 3)
        self.assertRaises(AttributeError, multiply_two_nums, 2, 2.5)
        self.assertRaises(AttributeError, multiply_two_nums, 2, "iha")
