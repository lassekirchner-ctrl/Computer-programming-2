
#testing debugging, code by cluade
def double(n):
    result = n * 2
    return result

def process_numbers(numbers):
    total = 0
    for num in numbers:
        doubled = double(num)
        total += doubled
    return total

numbers = [1, 2, 3, 4]
final_total = process_numbers(numbers)
print(f"Final total: {final_total}")
