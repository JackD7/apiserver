from datetime import datetime

class ApiLogger:
    
    def __init__(self, level):
        self.level = level

    def log(self, data, level):
        print("[{}] - {} - {}".format(datetime.now().time(), level, data), flush=True)

    def error(self, data):
        if self.level in ['error']:
            self.log(data, 'ERROR')

    def info(self, data):
        if self.level in ['debug', 'info']:
            self.log(data, 'INFO')

    def debug(self, data):
        if self.level in ['debug', 'info', 'error']:
            self.log(data, 'DEBUG')
