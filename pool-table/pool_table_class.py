#Create class object called PoolTable to be used in the pool table app

from datetime import datetime


class PoolTable:
    def __init__(self, number):
        self.number = number
        self.is_occupied = False
        self.start_time = None
        self.end_time = None
        self.total_time = None
        self.elapsed_time = None

    def check_out(self):
        now = datetime.now()
        time = now.strftime("%H:%M:%S")
        self.is_occupied = True
        self.start_time = time

    def return_table(self):
        now = datetime.now()
        time = now.strftime("%H:%M:%S")
        self.is_occupied = False
        self.end_time = time
        

