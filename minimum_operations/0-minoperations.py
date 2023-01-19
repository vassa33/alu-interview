#!usr/bin/python3

def minOperations(n):
    if n <= 0: 
        return 0
    else:
        copy_all = 0
        while n % 2 == 0:
            n = n // 2
            copy_all += 1
        return copy_all + (n - 1)
        
#new line
