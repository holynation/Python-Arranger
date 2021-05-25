># **Arithmetic Arranger** (CSC 231 Project)

Scientific Programming (CSC 231) Course Project 1
## Description
Students in primary school often arrange arithmetic problems vertically to make them easier to solve. For example, "235 + 52" becomes:
```
  235
+  52
-----
```

A function that receives a list of strings that are arithmetic problems and returns the problems arranged vertically and side-by-side. The function optionally takes a second argument. When the second argument is set to `True`, the answers is displayed.

> ### For example

Function Call:
```py
arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])
```

Output:
```
   32      3801      45      123
+ 698    -    2    + 43    +  49
-----    ------    ----    -----
```

Function Call:
```py
arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)
```

Output:
```
  32         1      9999      523
+  8    - 3801    + 9999    -  49
----    ------    ------    -----
  40     -3800     19998      474
----	------	  ------    -----
```

> ## Rules

The function will return the correct conversion if the supplied problems are properly formatted, otherwise, it will **return** a **string** that describes an error that is meaningful to the user.  


* Situations that will return an error:
  1. If there are **too many problems** supplied to the function. The limit is **seven**, anything more will return:
    `Error: Too many problems.`
  2. The appropriate operators the function will accept are **addition** and **subtraction**. Multiplication and division will return an error. Other operators not mentioned in this bullet point will not need to be tested. The error returned will be:
    `Error: Operator must be '+' or '-'.`
  3. Each number (operand) should only contain digits (0 - 9). Otherwise, the function will return:
    `Error: Numbers must only contain digits.`
  4. Each operand (aka number on each side of the operator) has a max of six digits in width. Otherwise, the error string returned will be:
    `Error: Numbers cannot be more than six digits.`
*  If the user supplied the correct format of problems, the conversion returned follow these rules:
    * There's a single space between the operator and the longest of the two operands, the operator is on the same line as the second operand, both operands are in the same order as provided (the first at the top one and the second will at the bottom).
    * Numbers are right-aligned.
    * There are four spaces between each problem.
    * There are dashes at the bottom of each problem and at the bottom of each answer. The dashes run along the entire length of each problem individually. (The example above shows what this looks like.)


Code in `arithmetic_arranger.py`.

#

>## Acknowlegements
* ___Osanebi Emmanuel___: Emms wrote the primordal codes upon which the final codes was built on
* ___Ivuelekwa Stephen___: Stepen wrote the script for unit-testing the project to ensure it is working as expected.
* ___Alatise Oluwaseun___: For excellent management of the project's developement.
* ___Akinwusi Ifeoluwa___: The Course's Rep and his assistant ___Adisa Christiana___.
* Members of the Project's Dev group and the entire members of the department.

#
***c. 2021 Computer Science Department UI (200lv)***