'''
timer - Class for measuring elapsed time (stopwatch)
'''

import time
import datetime


class Timer:
    "Timer - class for timing things"
    
    def __init__(self):
        # Note start time
        self.started = time.time()
        
    def reset(self):
        # reset() - Reset start
        self.__init__()
        
    def elapsed(self):
        # Return elapsed timedelta
        return datetime.timedelta(seconds=time.time() - self.started)

    def elapsed_s(self):
        # Return elapsed time in s
        return self.elapsed().total_seconds()

    def __str__(self):
        # print representation is current elapsed time
        return str(self.elapsed())
