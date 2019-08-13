def split_and_join(line):
    # write your code here
    test=line.split(" ")
    test ="-".join(test)
    return test

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
