

if __name__ == "__main__":
    with open("data.txt", "r") as f:
        input = f.read().splitlines()
        start, bus = input
        bus = list(filter(lambda x: x != 'x', bus.split(',')))
        start, bus = int(start), list(map(int, bus))
        times = map(lambda x: x - start % x, bus)
        bus_table = sorted(zip(times, bus), key = lambda x: x[0])
        wait, bus_num = bus_table.pop(0)
        print(wait * bus_num)