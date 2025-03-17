import random

def test_count_divisors():
    print("\n===== Running Test Cases for Task 2: Count Divisors =====")

    test_cases_divisors = [
        ([2, 4, 3, 6], [0, 1, 0, 2]),
        ([8, 4, 2], [0, 0, 0]),
        ([7, 8, 7, 8, 8], [0, 0, 1, 1, 2]),
        ([1], [0]),  # Single element
        ([3, 3, 3, 3, 3], [0, 1, 2, 3, 4]),  # All same numbers
        ([101, 103, 107, 109], [0, 0, 0, 0]),  # Large prime numbers (no divisors)
        ([1, 2, 4, 8, 16, 32], [0, 1, 2, 3, 4, 5]),  # Power of 2 sequence
        ([10, 5, 20, 40, 2, 4, 8], [0, 0, 1, 2, 0, 1, 3]),  # Mixed factors
        ([8, 1, 3, 7, 21, 2, 14], [0, 1, 1, 1, 3, 1, 3]),  # Edge case that previously failed
        (list(range(1, 10001)), [0] * 10000),  # Strictly increasing numbers (minimal divisors)
        ([1000] * 10000, list(range(10000))),  # Large list of repeated values
        ([random.randint(1, 50000) for _ in range(10000)], None)  # Random test (only for performance)
    ]

    passed_divisors = 0
    total_divisors = len([tc for tc in test_cases_divisors if tc[1] is not None])  # Exclude large random case

    for i, (A, expected) in enumerate(test_cases_divisors):
        result = solution_divisors(A)
        if expected is None:
            print(f"Test {i+1}: Completed large test case (Manual verification required).")
        else:
            if result == expected:
                passed_divisors += 1
            print(f"Test {i+1}: {result} (Expected: {expected}) - {'PASS' if result == expected else 'FAIL'}")

    divisors_score = (passed_divisors / total_divisors) * 100
    print(f"\n✅ Task 2 Score: {divisors_score:.2f}% ({passed_divisors}/{total_divisors} tests passed)")
