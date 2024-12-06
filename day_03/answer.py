import re
def part_one(file):
    f = open(file,'r')
    lines = [line.strip() for line in f.readlines()]
    
    total = 0
    regex = r"(mul\(\d+,\d+\))"
    for line in lines:
        muls = re.findall(regex,line)
        nums = re.findall(r"(\d+),(\d+)",''.join(muls))
        
        line_total = sum([int(pair[0])*int(pair[1]) for pair in nums])
        total += line_total
    print(f"total = {total}")

def part_two(file):
    f = open(file,'r')
    lines = [line.strip() for line in f.readlines()]
    big_line = ''.join(lines)
    total = 0
    regex = r"(mul\(\d+,\d+\))"
    
    enabled = True

    new_line = big_line.split("don't()")
    ok_lines = [new_line.pop(0)]
    for sub_line in new_line:
        # there is probably a better way to do this
        if "do()" not in sub_line:
            continue
        ok_lines.append(sub_line.split("do()",1)[1])
    good_line = ''.join(ok_lines)
    regex = r"(mul\(\d+,\d+\))"
    muls = re.findall(regex,good_line)
    nums = re.findall(r"(\d+),(\d+)",''.join(muls))
    
    line_total = sum([int(pair[0])*int(pair[1]) for pair in nums])
    print(f"total = {line_total}")


part_one('./test_input.txt')
part_one('./input.txt')

part_two('./test_input.txt')
part_two('./input.txt')
