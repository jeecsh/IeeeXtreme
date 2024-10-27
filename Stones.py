def probability_of_alice_winning(R1, B1, R2, B2):
    # Memoization dictionary to store states
    memo = {}

    # Recursive function with memoization
    def dp(R1, B1, R2, B2, alice_turn):
        # Base cases
        if R1 == 0 and B1 == 0:  # Alice loses
            return 0.0
        if R2 == 0 and B2 == 0:  # Bob loses
            return 1.0
        if (R1, B1, R2, B2, alice_turn) in memo:
            return memo[(R1, B1, R2, B2, alice_turn)]

        if alice_turn:
            # Alice's turn, maximize her probability of winning
            result = 0.0
            total_choices = 0
            
            if R1 > 0:  # If Alice can choose Red
                total_choices += 1
                # Bob guesses Red (Alice loses a Red stone)
                result += 0.5 * dp(R1 - 1, B1, R2, B2, False)
                # Bob guesses Blue (Bob loses a Blue stone)
                result += 0.5 * dp(R1, B1, R2, B2 - 1, False)

            if B1 > 0:  # If Alice can choose Blue
                total_choices += 1
                # Bob guesses Red (Alice loses a Blue stone)
                result += 0.5 * dp(R1, B1 - 1, R2 - 1, B2, False)
                # Bob guesses Blue (Bob loses a Blue stone)
                result += 0.5 * dp(R1, B1 - 1, R2, B2 - 1, False)

            if total_choices > 0:
                result /= total_choices  # Normalize by the number of choices
        else:
            # Bob's turn, minimize Alice's probability of winning
            result = 1.0  # Start with the worst case for Alice (Bob wins)
            total_choices = 0
            
            if R2 > 0:  # If Bob can choose Red
                total_choices += 1
                # Alice guesses Red (Bob loses a Red stone)
                result = min(result, 0.5 * dp(R1 - 1, B1, R2 - 1, B2, True))
                # Alice guesses Blue (Alice loses a Blue stone)
                result = min(result, 0.5 * dp(R1, B1 - 1, R2 - 1, B2, True))

            if B2 > 0:  # If Bob can choose Blue
                total_choices += 1
                # Alice guesses Red (Bob loses a Red stone)
                result = min(result, 0.5 * dp(R1 - 1, B1, R2, B2 - 1, True))
                # Alice guesses Blue (Alice loses a Blue stone)
                result = min(result, 0.5 * dp(R1, B1 - 1, R2, B2 - 1, True))

            if total_choices > 0:
                result /= total_choices  # Normalize by the number of choices

        memo[(R1, B1, R2, B2, alice_turn)] = result
        return result

    # Start with Alice's turn
    return dp(R1, B1, R2, B2, True)

# Example usage
R1, B1, R2, B2 = map(int, input().strip().split())  # Read input
print(f"{probability_of_alice_winning(R1, B1, R2, B2):.6f}")
