def generate_target_code(intermediate_code):
    target_code = []
    label_counter = 0
    for line in intermediate_code:
        if '=' in line:
            var, expr = line.split('=')
            target_code.append(f"MOV R1, {expr.strip()}")
            target_code.append(f"STORE {var.strip()}, R1")
        elif line.startswith('PRINT'):
            val = line.replace('PRINT ', '').strip()
            target_code.append(f"OUT {val}")
        elif line.startswith('IF'):
            condition = line.replace('IF ', '').strip()
            label_counter += 1
            target_code.append(f"CMP {condition}")
            target_code.append(f"JMP_FALSE ELSE_{label_counter}")
        elif line == 'ELSE':
            target_code.append(f"ELSE_{label_counter}:")
    return target_code
