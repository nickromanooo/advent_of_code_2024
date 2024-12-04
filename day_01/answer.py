def part_one(file):    
    f = open(file,'r')
    lines = [line.strip().replace('   ',' ').split(' ') for line in f.readlines()]
    left = sorted([int(l[0]) for l in lines])
    right = sorted([int(r[-1]) for r in lines])
    distances = [abs(p[0]-p[-1]) for p in zip(left,right)]
    print(sum(distances))

def part_two(file):
    f = open(file,'r')
    lines = [line.strip().replace('   ',' ').split(' ') for line in f.readlines()]
    left = sorted([int(l[0]) for l in lines])
    right = sorted([int(r[-1]) for r in lines])
    
    totals = 0

    for i in range(len(left)):
        num = left[i]
        count = right.count(num)
        totals += num * count
    print(totals)
    

part_one('./test_input.txt')
part_one('./input.txt')

part_two('./test_input.txt')
part_two('./input.txt')
