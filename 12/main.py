def navigate(inst): 
    DIR = [(0, 1), (-1, 0), (0, -1), (1, 0)]
    x, y = 0, 0
    facing = 0 # eswn; indexed using pos in dir array

    CMD = {
        "N": lambda x, y, units: (x + units, y),
        "S": lambda x, y, units: (x - units, y),
        "E": lambda x, y, units: (x, y + units),
        "W": lambda x, y, units: (x, y - units),
        "L": lambda units, dir: (dir - units // 90) % 4,
        "R": lambda units, dir: (dir + units // 90) % 4,
        "F": lambda x, y, units, dir: (x + DIR[dir][0] * units, y + DIR[dir][1] * units) 
    }

    for i in inst:
        cmd, num = i[0], int(i[1:])
        if cmd in "NSEW":
            x, y = CMD[cmd](x, y, num)
        elif cmd in "LR":
            facing = CMD[cmd](num, facing)
        else:
            x, y = CMD[cmd](x, y, num, facing)
        print(x, y, facing)
    return abs(x) + abs(y)

if __name__ == "__main__":
    with open("data.txt", "r") as f:
        input = f.read().splitlines()
        print(navigate(input))
