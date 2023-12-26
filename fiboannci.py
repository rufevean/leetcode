n = 10
## Fibonacci using recursion
def fib_rec(n:int)-> int:
    if n == 0 :
        return 0
    if n == 1 or n == 2 :
        return 1
    return fib_rec(n-1) + fib_rec(n-2)

result = fib_rec(n)
print(result)

# fibonacci using memoization 

new_hash = {0:0,1:1}
def fib_rec_memo(n:int,new_hash : dict)-> int:
    if n in new_hash:
        return new_hash[n]
    else:
        new_hash[n] = fib_rec_memo(n-1,new_hash )+ fib_rec_memo(n-2,new_hash)
        return new_hash[n]

result2 = fib_rec_memo(n,new_hash)
print(result2)

# fibonacci using iterative approach
def fib_iter(n:int)-> int:
    a,b = 0,1
    for i in range(0,n):
        a,b = b,a+b
    return a

result_iter = fib_iter(n)
print(result_iter)



