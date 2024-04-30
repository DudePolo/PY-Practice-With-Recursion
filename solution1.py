# Write code for algorithm 1 below
def count_down(n):

  #  Base case
  if n==0:
      return

  #  Recursive case
  else:
      print(n)
      count_down(n-1)


print('now for recursive')
# test case
n=8
count_down(n)

def count_down2(n):
  #inherent base case
  #(will stop if n <= 0)
  if n>0:
      #recursive case
      print(n)
      count_down2(n-1)
   
#test case
n=8
count_down2(n)
