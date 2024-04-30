# Write code for algorithm 2 below
def natural_numbers(x):
    if x < 1:
        return
    
    for i in range(1, x + 1):
        print(i)

natural_numbers(3)

#output: 1 2 3