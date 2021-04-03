import random
from string import punctuation, ascii_letters, ascii_uppercase, digits


class Passwords:
    """ Generator symbol, str_en, number, key """

    def __init__(self, number=5):
        self.number = number

    def random_symbol(self):
        return ''.join(random.sample(punctuation, self.number))

    def random_str_en_letter(self):
        return ''.join(random.sample(ascii_letters, self.number))

    def random_str_en_upper(self):
        return ''.join(random.sample(ascii_uppercase, self.number))

    def random_digit(self):
        return ''.join(random.sample(digits, self.number))



if __name__ == '__main__':
    r = Passwords()
    print(r.random_symbol())
    print(r.random_str_en_letter())
    print(r.random_str_en_upper())
    print(r.random_digit())