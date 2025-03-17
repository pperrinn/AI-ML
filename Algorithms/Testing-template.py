import random

def run_tests(solution_function, test_cases, function_name):
    """
    Runs a set of test cases for a given function and calculates an overall score.

    Parameters:
    - solution_function: The function to be tested.
    - test_cases: A list of tuples in the format (input_data, expected_output).
    - function_name: The name of the function being tested (for display purposes).

    Output:
    - Prints test results and an overall success percentage.
    """
    print(f"\n===== Running Test Cases for {function_name} =====")

    passed_tests = 0
    total_tests = len([tc for tc in test_cases if tc[1] is not None])  # Exclude large cases

    for i, (input_data, expected) in enumerate(test_cases):
        result = solution_function(*input_data) if isinstance(input_data, tuple) else solution_function(input_data)

        if expected is None:
            print(f"Test {i+1}: Completed large test case (Manual verification required).")
        else:
            if result == expected:
                passed_tests += 1
            print(f"Test {i+1}: {result} (Expected: {expected}) - {'PASS' if result == expected else 'FAIL'}")

    # Calculate and display score
    score = (passed_tests / total_tests) * 100 if total_tests > 0 else 0
    print(f"\n✅ {function_name} Score: {score:.2f}% ({passed_tests}/{total_tests} tests passed)\n")
    return score
