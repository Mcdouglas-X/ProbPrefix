
import os
import bisect
from threading import Lock

class HashTable:
    def __init__(self, filename):
        self.filename = filename
        self.lock = Lock()
        self.ranges = []
        self.starts = []
        
        if os.path.exists(self.filename):
            self._load_file()

    def _load_file(self):
        with open(self.filename, 'r') as f:
            for line in f:
                start, end = map(int, line.strip().split(':'))
                self._add_mem(start, end)

    def _save_file(self, start, end):
        with open(self.filename, 'a') as f:
            f.write(f"{start}:{end}\n")

    def _add_mem(self, start, end):
        pos = bisect.bisect_left(self.starts, start)
        new_start, new_end = start, end
        
        if pos > 0 and self.ranges[pos-1][1] >= new_start - 1:
            new_start = min(new_start, self.ranges[pos-1][0])
            new_end = max(new_end, self.ranges[pos-1][1])
            pos -= 1
        
        while pos < len(self.ranges) and self.ranges[pos][0] <= new_end + 1:
            new_end = max(new_end, self.ranges[pos][1])
            del self.ranges[pos]
            del self.starts[pos]
        
        self.ranges.insert(pos, (new_start, new_end))
        self.starts.insert(pos, new_start)

    def add_range(self, r1, r2):
        with self.lock:
            self._add_mem(r1, r2)
            self._save_file(r1, r2)

    def is_range(self, num):
        with self.lock:
            pos = bisect.bisect_right(self.starts, num) - 1
            return pos >= 0 and self.ranges[pos][1] >= num

    def clear(self):
        with self.lock:
            self.ranges = []
            self.starts = []
            if os.path.exists(self.filename):
                os.remove(self.filename)
