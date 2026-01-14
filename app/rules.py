

def apply_rules(values,
                high_threshold = 90,
                low_threshold = 5,
                delta_threshold = 30
                ):
    """
    Docstring for apply_rules
    
    Apply simple rule based anomaly checks.

    returns: list[int] -> 1(normal) or -1(anomaly)
    """

    rule_flag = []

    for i, val in enumerate(values):
        is_anomaly = False

        # Rule 1: Absolute high value
        if val > high_threshold:
            is_anomaly=True
        
        # Rule 2: Absolute low value
        if val < low_threshold:
            is_anomaly=True

        # Rule 3: Sudden Jump
        if i > 0  and abs(val-values[i-1] > delta_threshold):
            is_anomaly = True

        rule_flag.append(-1 if is_anomaly else 1)
    
    return rule_flag