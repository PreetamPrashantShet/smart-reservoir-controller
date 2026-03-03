def calculate_release(predicted_storage, capacity, inflow):

    safe_upper = 0.9 * capacity
    safe_lower = 0.4 * capacity

    if predicted_storage > safe_upper:
        return (predicted_storage - safe_upper) + inflow * 0.5

    elif predicted_storage < safe_lower:
        return inflow * 0.1

    else:
        return inflow * 0.3