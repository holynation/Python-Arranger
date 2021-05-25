# CSC 231 Course Project
# Name: Arithmetic Arranger
# Department: Computer Science
# Level: 200

def arithmetic_arranger(expression, result = False):
    """
    Arithmetic Arranger\n
    Accepts a list of arithmetic expressions and returns a string of the arithmetic expression arranged vertically.\n
    If more than one expressions are present in the list, each of the vertically arranged expressions are arranged horizontally,\n
    seperating each expresssion from each other.
    \te.g.
    >>> arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])
       32      3801      45      123
    + 698    -    2    + 43    +  49
    -----    ------    ----    -----
    
    \n\nCall the function with a second boolean argument set to True, returns a string of arranged expressions togther with their evaluations
    >>> arithmetic_arranger(["32 - 23", "1 - 3801", "9999 + 9999", "523 - 49"], True)
      32         1      9999      523
    - 23    - 3801    + 9999    -  49
    ----    ------    ------    -----
       9     -3800     19998      474
    ----    ------    ------    -----

    """    
    if len(expression) > 7:                         # Handling First Error: Function must only accept a maximum of six expressions
        return "Error: Too many problems."

    # Empty List objects to hold each line of each expression
    # There would be a maximum of 4 lines for each expression (i.e if result argument is True)
    li1 = []        # To hold the first line of each of the expressions (i.e the line containing the first operand)
    li2 = []        # To hold the second line of each of the expressions (i.e the line containing the operator and second operand)
    li3 = []        # The third line for underlining (i.e  bunch of horizontal dashes to separate the operands from their result)
    li4 = []        # Fourth line of  each expression (i.e the result of each of the individual expression)
    for exp in expression:
        exp = exp.replace(" ", "")                  # Removing all whitespace from expression

        # Checking for the supported Operators ('+' and '-' only)
        if "+" in exp:
            exp = exp.split("+")                    # Spliting characters in the expression using "+" as a delimiter (Yields a list containing the two operands of the expression)
            operator = "+"
        elif "-" in exp:
            exp = exp.split("-")                    # Spliting with "-" as a delimiter instead
            operator = "-"
        else:                                       # Second Error Handling: Only '+' and '-' operators are required
            return "Error: Operator must be '+' or '-'."

        # Checking for non-digit operands
        if (not exp[0].isdigit()) or (not exp[1].isdigit()):    # Third Error handling: Expressions must contain digit operands only
            return "Error: Numbers must only contain digits."
        
        # Checking for operand with digits greater than six
        if len(exp[0]) > 6 or len(exp[1])> 6:                   # Fourth Error handling: Each operands must not have digits greater than six
            return "Error: Numbers cannot be more than six digits."
        
        
        align = max([len(exp[0]), len(exp[1])]) + 2             # Getting number of digits contained in the operand with the longest digits (adding 2 to it). This determines the number characters that a line can have in each arranged expression
        
        # Evaluating the arithmetic expression (If the second argument 'result' is True)        
        if result:
            res = str(eval(exp[0] + operator + exp[1]))         # Evaluating the concatenation of the operands and the operator with the 'eval' function
            li4.append(res.rjust(align))                        # Appending into list the result of the expression with the contained digits rightly-just
        

        li1.append(exp[0].rjust(align))                                                     # Appending into list, first Operand, rightly-just
        li2.append((operator + (" " * (align - len(exp[1]) - 1)) + exp[1]).rjust(align))    # Appending into list, operator and the second operand, rightly-just
        li3.append("-" * (align))                                                           # Appending into list, the underlining (bunch of dashes)

    # End of loop    
    
    # Arranging the expression into a single string

    line1 = "    ".join(li1)
    line2 = "    ".join(li2)        # Joining each element in each line into a string, separated by four whitespaces
    line3 = "    ".join(li3)

    arranged_string = "\n".join([line1, line2, line3])  # Joining line 1 - 3 into a single string, separated by a newline character

    if result:                                          # Adding the fourth line if the result argument is True
        line4 = "    ".join(li4)
        arranged_string += "\n" + line4 + "\n" + line3

    
    return arranged_string          # Returning the arranged string!!!
