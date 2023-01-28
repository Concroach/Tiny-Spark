import shelve


class save():
    def __init__(self):
        self.file = shelve.open('data')

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
            if name == 'flag_game_defoult':
                return True
            if name == 'flag_game':
                return False
            if name == 'flag_game_is':
                return False
            if name == 'flag_game_buy':
                return True
            if name == 'flag_music_defoult':
                return True
            if name == 'flag_music':
                return False
            if name == 'flag_music_is':
                return False
            if name == 'flag_music_buy':
                return True
            if name == 'flag_music_hotline_1':
                return False
            if name == 'flag_music_is_hotline_1':
                return False
            if name == 'flag_music_buy_hotline_1':
                return True
            if name == 'volume':
                return 1.0000000000000002
            else:
                return 0

    def __del__(self):
        self.file.close()