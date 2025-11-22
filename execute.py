import random
import time

def generate_random_numbers(count=10, lower=1, upper=100):
    return [random.randint(lower, upper) for _ in range(count)]

def calculate_average(numbers):
    return sum(numbers) / len(numbers)

def draw_bar_chart(numbers):
    print("\nBAR CHART:")
    for i, num in enumerate(numbers, start=1):
        print(f"{i:02d} | " + "#" * (num // 2) + f" ({num})")

# Execution
print("Generating random numbers...")
time.sleep(1)

nums.
print("Numbers:", nums)

avg = calculate_average(nums)
print(f"\nAverage: {avg:.2f}")

draw_bar_chart(nums)
