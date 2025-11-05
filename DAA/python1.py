def fib_recursive(n):
      if n <=1:
          return n
      else:
          return fib_recursive(n-1) + fib_recursive(n-2)
   
          
def fib_nonrecursive(n):
    a,b=0,1
  
    series=[]
    for _ in range(n):
        series.append(a)
        a,b=b, a+b
    return series
    
    
# Main program
n = int(input("Enter number of terms: "))
if n<=0:
   print("Please enter a postivie number")
   exit()
# Non-recursive output
non_rec_series = fib_nonrecursive(n)
print("\nFibonacci Series (Non-Recursive):")
print(non_rec_series)

# Recursive output
rec_series = [fib_recursive(i) for i in range(n)]
print("\nFibonacci Series (Recursive):")
print(rec_series)

# Time & Space Complexity
print("\n--- Time and Space Complexity ---")
print("Recursive:  Time = O(2^n),  Space = O(n)")
print("Non-Recursive:  Time = O(n),  Space = O(1)")
