import shelve


class save():
    def __init__(self):
        self.file = shelve.open('data')
        self

    def save(self, name, value):
        self.file[name] = value

    def get(self, name):
        try:
            return self.file[name]
        except:
            if name == 'flag_mario':
                return True
            if name == 'flag_mine':
                return False
            if name == 'flag_mine_is':
                return False
            if name == 'flag_mine_buy':
                return True
            if name == 'flag_rocket':
                return False
            if name == 'flag_rocket_is':
                return False
            if name == 'flag_rocket_buy':
                return True
            if name == 'volume':
                return 1
            else:
                return 0

    def __del__(self):
        self.file.close()