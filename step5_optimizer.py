def optimize_code(intermediate_code):
    optimized = []
    for line in intermediate_code:
        if line not in optimized:
            optimized.append(line)
    return optimized
