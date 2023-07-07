import multiprocessing
import time

def factorize(numbers):
    results = []
    for number in numbers:
        factors = []
        for i in range(1, number + 1):
            if number % i == 0:
                factors.append(i)
        results.append(factors)
    return results


numbers = [128, 255, 99999, 10651060]

start_time = time.time()
factors = factorize(numbers)
end_time = time.time()

execution_time = end_time - start_time

print("Factors (synchronous):", factors)
print("Execution time (synchronous):", execution_time, "seconds")

exit()

