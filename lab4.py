import matplotlib.pyplot as plt
import timeit

nums = list(range(10, 300, 10))

def fact_recursive(n: int) -> int:
    """Рекурсивный факториал"""
    if n == 0:
        return 1
    else:
        return n * fact_recursive(n-1)
        

def fact_iterative(n: int) -> int:
    """Нерекурсивный факториал"""
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact

def benchmark(f, n, number, repeat):
    """Возвращает среднее время выполнения func(n)"""
    times = timeit.repeat(lambda: f(n), number=number, repeat=repeat)
    return min(times)

res_recursive = []
res_iterative = []

for n in nums:
      res_recursive.append(benchmark(fact_recursive, n, repeat=5, number=1000))
      res_iterative.append(benchmark(fact_iterative, n, repeat=5, number=1000))

# Визуализация
plt.plot(nums, res_recursive, label="Рекурсивный")
plt.plot(nums, res_iterative, label="Итеративный")
plt.xlabel("n")
plt.ylabel("Время (сек)")
plt.title("Сравнение рекурсивного и итеративного факториала")
plt.grid(True)
plt.legend()
plt.show()
