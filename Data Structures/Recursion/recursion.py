print("hello recursion")

#simple recursion
def rec(n:int) -> int:
    if n >=0:
        print(n)
        rec(n-1)
    
rec(10)


