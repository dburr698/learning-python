#Create class object called PoolTable to be used in the pool table app

from datetime import datetime

fmt = "%H:%M:%S"
class PoolTable:
    def __init__(self, number):
        self.number = number
        self.is_occupied = False
        self.start_time = None
        self.end_time = None
        self.total_time = None
        self.elapsed_time = None
        self.cost = None

    def check_out(self):
        now = datetime.now()
        time = now.strftime(fmt)
        self.is_occupied = True
        self.start_time = time

    def return_table(self):
        now = datetime.now()
        time = now.strftime(fmt)
        self.is_occupied = False
        self.end_time = time

    def delta_total(self):
        delta = datetime.strptime(self.end_time, fmt) - datetime.strptime(self.start_time, fmt)
        self.total_time = delta

    def delta_elapsed(self):
        now = datetime.now()
        time = now.strftime(fmt)
        delta = datetime.strptime(time, fmt) - datetime.strptime(self.start_time, fmt)
        self.elapsed_time = delta

    def calculate_cost(self):
        sec = self.total_time.seconds
        total_hours = sec/3600
        cost = total_hours * 30
        cost = round(cost, 2)
        self.cost = cost

