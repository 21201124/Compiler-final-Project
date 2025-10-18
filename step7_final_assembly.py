def generate_assembly(target_code):
    assembly = []
    assembly.append("section .text")
    assembly.append("global _start")
    assembly.append("_start:")
    for line in target_code:
        assembly.append(line)
    assembly.append("mov eax, 1")
    assembly.append("mov ebx, 0")
    assembly.append("int 0x80")
    return assembly
