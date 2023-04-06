import timeit
import numpy as np

# Define the function for the secant method
def secant(f, x0, x1, tol=1e-6, maxiter=100):
    for i in range(maxiter):
        fx0 = f(x0)
        fx1 = f(x1)
        if abs(fx1) < tol:
            return x1
        dx = fx1 * (x1 - x0) / (fx1 - fx0)
        x0 = x1
        x1 = x1 - dx
    raise ValueError("Failed to converge")

# Prompt the user to define a polynomial
poly = input("Enter a polynomial (in the form of a string): ")
f = lambda x: eval(poly)

# Prompt the user to enter the initial guesses
x0 = float(input("Enter the first initial guess: "))
x1 = float(input("Enter the second initial guess: "))

# Measure the execution time
t = timeit.timeit(lambda: secant(f, x0, x1), number=1)

# Print the result and execution time
root = secant(f, x0, x1)
print("Root:", root)
print("Execution time:", t, "seconds")
