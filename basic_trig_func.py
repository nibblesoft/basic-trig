import math

# Get the period of sinusoidal function.
def get_sinusoidal_period(B):
    x = (2 * math.pi) 
    B = abs(b)
    return x / B

# Given an A return if function is stretched or compressed.
def get_function_state(A):
    # TODO: ensure A is a number.
    A = abs(A)
    if abs(A) > 1:
        print('Function is stretched')
    else:
        print('Function is compressed')
