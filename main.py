from step1_lexer import lexer
from step2_syntax_analyzer import SyntaxAnalyzer
from step3_semantic_analyzer import SemanticAnalyzer
from step4_intermediate_code import IntermediateCodeGenerator
from step5_optimizer import optimize_code
from step6_target_codegen import generate_target_code
from step7_final_assembly import generate_assembly

source_code = """
int a = 5;
int b = 10;
int c;
c = a + b * 2;
print(c);
if (c > 10) {
    print(c);
} else {
    print(a);
}
"""

print("=================================================")
print("           MINI COMPILER (7 COMPLETE PHASES)     ")
print("=================================================")

print("\n🔹 PHASE 1: LEXICAL ANALYZER")
tokens = lexer(source_code)
for t in tokens:
    print(t)

print("\n🔹 PHASE 2: SYNTAX ANALYZER")
syntax = SyntaxAnalyzer(tokens)
syntax.parse()
print("✅ Syntax Analysis Successful.")

print("\n🔹 PHASE 3: SEMANTIC ANALYZER")
semantic = SemanticAnalyzer(tokens)
table = semantic.analyze()
print("✅ Symbol Table:", table)

print("\n🔹 PHASE 4: INTERMEDIATE CODE GENERATOR")
ir = IntermediateCodeGenerator(tokens)
icode = ir.generate()
for line in icode:
    print(line)

print("\n🔹 PHASE 5: OPTIMIZER")
optimized = optimize_code(icode)
for line in optimized:
    print(line)

print("\n🔹 PHASE 6: TARGET CODE GENERATOR")
target = generate_target_code(optimized)
for line in target:
    print(line)

print("\n🔹 PHASE 7: FINAL ASSEMBLY CODE")
assembly = generate_assembly(target)
for line in assembly:
    print(line)

print("\n✅ Compilation Successful!")
