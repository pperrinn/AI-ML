# The function I've sumitted
def solution_divisors(A):
    N = len(A)
    result = [0] * N
    count_map = defaultdict(int)  # Tracks occurrences of each number seen so far

    logging.debug(f"Input Array: {A}")

    for i in range(N):
        num = A[i]
        divisor_count = 0

        logging.debug(f"\nProcessing A[{i}] = {num}")

        # Check all divisors up to sqrt(num)
        for d in range(1, int(num ** 0.5) + 1):
            if num % d == 0:
                if d in count_map:  # d is a divisor and has appeared before
                    divisor_count += count_map[d]
                    logging.debug(f"  Found divisor {d}, count so far: {divisor_count}")

                quotient = num // d
                if quotient != d and quotient in count_map:  # Check quotient as divisor
                    divisor_count += count_map[quotient]
                    logging.debug(f"  Found divisor {quotient}, count so far: {divisor_count}")

        result[i] = divisor_count
        count_map[num] += 1  # Track occurrences of num

        logging.debug(f"Updated count_map: {dict(count_map)}")
        logging.debug(f"Result so far: {result}")

    logging.debug(f"\nFinal Result: {result}")
    return result
