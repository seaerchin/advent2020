from collections import defaultdict
from itertools import takewhile

def parse_rule(rule):
    rule = list(map(lambda x: list(map(lambda y: y.strip(), x.split("-"))), rule.split("or")))
    return lambda x: any(map(lambda y: y(x), list(map(lambda x: within(int(x[0]), int(x[1])), rule))))

def collate_rules(input): 
    rules = dict()
    for i in input:
        name, rule = i[0], parse_rule(i[1])
        rules[name] = rule
    return rules

# this is bad style but ok
within = lambda lower, higher: lambda x: lower <= x <= higher 
create_or = lambda x, y: lambda z: x(z) or y(z)

if __name__ == "__main__":
    with open("data.txt", "r") as f:
        input = list(map(lambda x: list(map(lambda y: y.strip(), x.split(":"))), f.read().splitlines()))
        collated_rules = takewhile(lambda x: bool(x[0]), input)
        rules = collate_rules(collated_rules)
        nearby = input.index(['nearby tickets', ''])
        rest = list(map(lambda x: list(map(int, x.split(','))), [i[0] for i in input[nearby + 1:]]))
        adheres = lambda x: any([i(x) for i in rules.values()])
        res = 0 
        for i in rest: 
            for j in i:
                if not adheres(j):
                    res += j
        print(res)
        