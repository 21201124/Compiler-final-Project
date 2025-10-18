from step1_lexer import lexer
from step2_syntax_analyzer import SyntaxAnalyzer
from step3_semantic_analyzer import SemanticAnalyzer
from step4_intermediate_code import IntermediateCodeGenerator
from step5_optimizer import optimize_code
from step6_target_codegen import generate_target_code
from step7_final_assembly import generate_assembly

# ===========================================================
# 🧠 REALISTIC MINI PROGRAM INPUT (Syntax-Compatible)
# ===========================================================
source_code = """
int gpa = 5;
float cgpa = 4.50;
string university = "UAP";
string slogan = "UAP is Best!";
string dogAction = "Dog is Barking!";
char grade = 'A';
bool passed = true;

print(university);
print(slogan);
print(dogAction);

int marks = 90;
if (marks >= 80) {
    print("Excellent Result!");
} else {
    print("Need Improvement!");
}

float height = 5.9;
float weight = 65.5;
float bmi = weight / (height * height);

print("Your BMI is:");
print(bmi);

int day = 1;
while (day <= 3) {
    print("Day count:");
    print(day);
    day = day + 1;
}

print("My GPA is:");
print(gpa);
print("Compilation Finished Successfully!");
"""

# ===========================================================
#              MINI COMPILER EXECUTION PIPELINE
# ===========================================================
print("=================================================")
print("           MINI COMPILER (7 COMPLETE PHASES)     ")
print("=================================================")

try:
    
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

    print("✅ SYMBOL TABLE (Formatted):")
    print("--------------------------------------------")
    print(f"{'Name':<12} | {'Type':<10} | {'Value':<15} | {'Scope'}")
    print("--------------------------------------------")
    for name, info in table.items():
        print(f"{info['name']:<12} | {info['type']:<10} | {str(info['value']):<15} | {info['scope']}")
    print("--------------------------------------------")

   
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

except Exception as e:
    print(f"❌ Error during compilation: {e}")
