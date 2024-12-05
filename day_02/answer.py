def part_one(file):
    f = open(file,'r')
    lines = [[int(item) for item in line.strip().split(' ')] for line in f.readlines()]
    safe_lines = 0
    for line in lines:
        #all increasing or all decreasing
        #adjacent must differ by 1 at most 3
        if (sort_line:=sorted(line)) != line and sort_line != line[::-1]:
            continue
        diffs = []
        for i in range(len(line)-1):
            diffs.append(abs(line[i]-line[i+1]))

        if not all([item <= 3 and item > 0 for item in diffs]):
            continue 
        safe_lines += 1
    print(f"there were {safe_lines} safe lines!") 

def part_two(file):
    f = open(file,'r')
    lines = [[int(item) for item in line.strip().split(' ')] for line in f.readlines()]
    safe_lines = 0
    for line in lines:
        sub_lines = [line]
        for i in range(len(line)):
            sub_lines.append(line[:i] + line[i+1:])
       
        for sl in sub_lines:
            #all increasing or all decreasing
            #adjacent must differ by 1 at most 3
            if (sort_line:=sorted(sl)) != sl and sort_line != sl[::-1]:
                continue
            diffs = []
            for i in range(len(sl)-1):
                diffs.append(abs(sl[i]-sl[i+1]))

            if not all([item <= 3 and item > 0 for item in diffs]):
                continue

            safe_lines += 1
            break
    print(f"there were {safe_lines} safe lines!") 



#part_one('./test_input.txt')
#part_one('./input.txt')

part_two('./test_input.txt')
part_two('./input.txt')

