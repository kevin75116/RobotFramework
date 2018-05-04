from robot.api import logger

class MyLibrary(object):
    
    def __init__(self):
        self.count = 0
        
    def get_count_value(self):
        self.count = self.count + 1
        return self.count
