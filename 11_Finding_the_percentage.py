if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

sum=0
if(query_name ==x for x in student_marks):
    test = student_marks[query_name]
    for itr in test:
        sum+=itr
    avg=sum/len(test)

    print(f"{avg:0.2f}")

