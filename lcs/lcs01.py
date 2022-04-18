A = input("Input first sentence and enter(default: ABCDEF): ") or 'ABCDEF'
B = input("Input second sentence and enter(default: GBCDFE): ") or 'GBCDFE'

LCS01 = [[0]*(len(A)+1) for i in range(len(B)+1)]
head_A = [0]*(len(A)+1)
head_B = [0]*(len(B)+1)

def print_LCS01():
    for i in range(len(LCS01[0])-1):
        head_A[i+1] = A[i]
        
    for i in range(len(LCS01)-1):
        head_B[i+1] = B[i]

    str = "     {0}".format(head_A[0])    
    for i in range(1,len(LCS01[0])):
        str += ", {0}".format(head_A[i])
    print(str)
    for i in range(len(LCS01)):
        print(head_B[i], ' ', LCS01[i])

# Longest Common Substring
if 1:
    print("---- Longest Common Substring ----")
    for i in range(0, len(LCS01)):
        for j in range(0, len(LCS01[0])):
            if i == 0 or j == 0:
                LCS01[i][j] = 0
            elif (head_A[i] == head_B[j]):
                LCS01[i][j] = LCS01[i-1][j-1] + 1
            else:
                LCS01[i][j] = 0
        print_LCS01()
        input("press enter..({0}, {1})".format(i,j))

# Find the length of Longest Common Subsequence
if 1:
    print("---- Find the length of Longest Common Subsequence ----")
    for i in range(0, len(LCS01)):
        for j in range(0, len(LCS01[0])):
            if i == 0 or j == 0:
                LCS01[i][j] = 0
            elif (head_A[i] == head_B[j]):
                LCS01[i][j] = LCS01[i-1][j-1] + 1
            else:
                LCS01[i][j] = max(LCS01[i-1][j],LCS01[i][j-1])
        print_LCS01()
        # input("press enter..({0}, {1})".format(i,j))

    print("---- Find the subsequence of Longest Common Subsequence #1 (left first) ----")
    
    i = len(LCS01)-1
    j = len(LCS01[0])-1
    current = LCS01[i][j]
    result = ''

    # print(current, result)

    while LCS01[i][j] != 0:
        if LCS01[i][j] == LCS01[i][j-1]:
            j = j - 1
        elif LCS01[i][j] == LCS01[i-1][j]:
            i = i - 1
        else:
            result = "{0}{1}".format(head_A[j], result)
            i = i - 1
            j = j - 1
        print_LCS01()
        input("press enter..({0}, {1}, {2})".format(i,j, result))

    print("---- Find the subsequence of Longest Common Subsequence #2 (right first) ----")
    
    i = len(LCS01)-1
    j = len(LCS01[0])-1
    current = LCS01[i][j]
    result = ''

    # print(current, result)

    while LCS01[i][j] != 0:
        if LCS01[i][j] == LCS01[i-1][j]:
            i = i - 1
        elif LCS01[i][j] == LCS01[i][j-1]:
            j = j - 1
        else:
            result = "{0}{1}".format(head_A[j], result)
            i = i - 1
            j = j - 1
        print_LCS01()
        input("press enter..({0}, {1}, {2})".format(i,j, result))
