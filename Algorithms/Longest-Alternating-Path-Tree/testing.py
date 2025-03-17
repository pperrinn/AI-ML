import random

def test_tree_path():
    print("===== Running Test Cases for Task 1: Tree Path =====")

    test_cases_tree = [
        ("ab", [-1, 0], 2),
        ("abbab", [-1, 0, 0, 0, 2], 3),
        ("abab", [-1, 2, 0, 1], 2),
        ("a", [-1], 1),  # Single-node tree
        ("aa", [-1, 0], 1),  # Same letter tree
        ("abbbba", [-1, 0, 1, 2, 3, 4], 2),  # Only one alternating transition
        ("ab"*5000, [-1] + [i//2 for i in range(1, 10000)], 5001),  # Large alternating tree
    ]

    passed_tree = 0
    total_tree = len(test_cases_tree)

    for i, (S, A, expected) in enumerate(test_cases_tree):
        result = solution_tree(S, A)
        if result == expected:
            passed_tree += 1
        print(f"Test {i+1}: {result} (Expected: {expected}) - {'PASS' if result == expected else 'FAIL'}")

    tree_score = (passed_tree / total_tree) * 100
    print(f"\n✅ Task 1 Score: {tree_score:.2f}% ({passed_tree}/{total_tree} tests passed)")
