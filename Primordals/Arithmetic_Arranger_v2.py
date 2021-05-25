# CSC 231 Course Project
# Name: Arithmetic Arranger
# Date: April 29, 2021

def arithmetic_arranger(expression: list[str], result: bool = False) -> str:
    if len(expression) > 7:
        return "Error: Too Many Problems"

    li1 = []
    li2 = []
    li3 = []
    li4 = []
    for exp in expression:
        exp = exp.replace(" ", "")
        if "+" in exp:
            exp = exp.split("+")
            operator = "+"
        elif "-" in exp:
            exp = exp.split("-")
            operator = "-"
        else:
            return "Error: Operator must be '+' or '-'"

        if (not exp[0].isdigit()) or (not exp[1].isdigit()):
            return "Error: Numbers must only contain digits"
        if len(exp[0]) > 6 or len(exp[1])> 6:
            return "Error: Numbers cannot be more than six digits"
        
        if result:
            res = str(eval(exp[0] + operator + exp[1]))
        else:
            res  = ""
        
        align = max([len(exp[0]), len(exp[1]), len(res)])

        li1.append("  " + exp[0].rjust(align))
        li2.append(operator + " " + exp[1].rjust(align))
        li3.append("-" * (align + 2))
        li4.append("  " + res.rjust(align))
    
    line1 = "    ".join(li1)
    line2 = "    ".join(li2)
    line3 = "    ".join(li3)

    arranged_string = "\n".join([line1, line2, line3])

    if result:
        line4 = "    ".join(li4)
        arranged_string += "\n" + line4

    arranged_string += "\n" + line3
    
    return arranged_string
    
      

# Test
print(arithmetic_arranger(["32 - 23", "1 - 3801", "9999 + 9999", "523 - 49"], True))
