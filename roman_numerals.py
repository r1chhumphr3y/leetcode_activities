class Solution:
    def romanToInt(self, s: str) -> int:
        # create constants:
        roman = { "I": 1,
                "V": 5,
                "X": 10,
                "L": 50,
                "C": 100,
                "D": 500,
                "M": 1000
                }

        int_value = 0

        # for loop to iterate over words array
        previous = 1001
        for char in s:
            # deubg: print(char)
            if char in roman:
                char_value = roman[char]
                if (char_value <= previous):
                    int_value += char_value
                else:
                    int_value = (int_value - previous) + (char_value - previous)

                previous = char_value
            else:
                print("Error, invalid character")

        return(int_value)

if __name__ == '__main__':
    str = 'MCMLXXI'
    print("Converting: ", str)
    solution = Solution;
    print(solution.romanToInt(solution, str))


