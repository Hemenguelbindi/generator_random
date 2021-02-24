import random


class Random_Key:
    """ Generator symbol, str_en, number, key """
    def __init__(self, number = 5):
        self.number = number

    def random_symbol(self):
        item = '!@#$%^&*()/*-,.\';:><'
        items = [i for i in item]
        symbol = ''.join(random.sample(items, self.number))
        return symbol

    def random_str_en(self):
        litter = 'QWERTYUIOPASDFGHJKLZXCVBNM'
        litters = [i for i in litter]
        en_str = ''.join(random.sample(litters, self.number))
        return litter

    def random_number(self):
        numb = '1234567890'
        numbs = [n for n in numb]
        r_numb = ''.join(random.sample(numbs, self.number))
        return r_numb

    def random_key(self):
        sym_lit = '1234567890QWERTYUIOPASDFGHJKLZXCVBNM'
        sym_litters = [i for i in sym_lit]
        key1= ''.join(random.sample(sym_litters, self.number))
        key2 = ''.join(random.sample(sym_litters, self.number))
        key3 = ''.join(random.sample(sym_litters, self.number))
        key4 = ''.join(random.sample(sym_litters, self.number))
        key5 = ''.join(random.sample(sym_litters, self.number))
        simple_key = key1+'-'+key2+'-'+key3+'-'+key4+'-'+key5
        return simple_key



