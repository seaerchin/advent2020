from collections import defaultdict

class MemoryBus:
    def __init__(self):
        self.mask = ""
        self.memory = defaultdict(int)
    
    def write(self, index, value): 
        value = self.with_mask(value)
        self.memory[index] = value

    # value is a str
    def with_mask(self, value): 
        value = bin(int(value))[2:]
        padded = self.pad(value)
        masked = ''
        for i in range(len(padded)): 
            if self.mask[i] == 'X':
                masked += padded[i]
            else:
                masked += self.mask[i]
        return masked
    
    def pad(self, value):
        return '0' * (len(self.mask) - len(value)) + value

if __name__ == "__main__":
    with open("data.txt", "r") as f:
        input = list(map(lambda x: x.split(' '), f.read().splitlines()))
        mem = MemoryBus()
        for line in input:
            inst = line[0]
            if inst == 'mask': 
                mem.mask = line[-1]
            else: 
                index, value = inst[4:-1], line[-1]
                mem.write(index, value)
        print(sum([int(x, 2) for x in mem.memory.values()]))
        