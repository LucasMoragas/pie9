import random
import time

class MockDataSource:
    def __init__(self, min_value = 0, max_value = 100, delay = 0.1):
        self.min_value = min_value
        self.max_value = max_value
        self.delay = delay
        
    def read_line(self):
        """_summary_
            Simulate reading a line from a data source.
        Returns:
            _type_: random integer between min and max value
        """
        time.sleep(self.delay)
        return random.randint(self.min_value, self.max_value)
    
    