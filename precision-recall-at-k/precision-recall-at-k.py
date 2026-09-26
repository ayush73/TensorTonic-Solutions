def precision_recall_at_k(recommended: list, relevant: list, k: int) -> list[float]:
    """
    Returns [precision, recall] as a list of two floats.
    """
    # Write code here
    relevant_set = set(relevant)

    top_k = recommended[:k]

    numerator = 0

    for item in top_k:
        if item in relevant_set:
            numerator = numerator + 1

    precision = numerator/k
    recall = numerator/len(relevant_set)

    return [precision, recall]