def fibo(n)
 sequence=[]
 a,b=0,1
 for i in range(n):
    sequence.append(a)
    a,b=b,a+b
    return sequence
    terms=int(input("enter the number of terms : "))
    print("fibonacci sequence ", terms)
