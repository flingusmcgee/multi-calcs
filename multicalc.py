def save():
    saveList = []
    for i in range(len(calculatorID)):
        saveList.append(calculatorID[i] + "\n")
        saveList.append(calculatorFormula[i] + "\n")
    with open("multicalcs.txt","w") as file:
        file.writelines(saveList)

# whats inside?
with open("multicalcs.txt","r+") as file:
    readFile = file.read().splitlines()
calculatorID = []
calculatorFormula = []
for i in range(len(readFile)):
    if i % 2 == 0:
        calculatorID.append(readFile[i])
    else:
        calculatorFormula.append(readFile[i])

# user
mode = input("Do a (Q)uick calculation, (F)ind a calculator, or make a (N)ew one?").capitalize()
if mode == "F" or mode == "Q":

    # select a calculator
    if mode == "F":
        print("Which calculator? (Enter : after to edit or delete.)")
        for i in range(len(calculatorID)):
            print(f"    {i + 1}. {calculatorID[i]}: {calculatorFormula[i]}")
        request = input()
        if ":" in request:
            selectedCalc = int(request[:-1]) - 1
            calculatorFormula[selectedCalc] = input(f"Enter the new calculator for '{calculatorID[selectedCalc]}' or leave blank to delete.")
            if calculatorFormula[selectedCalc] == "":
                calculatorID.pop(selectedCalc)
                calculatorFormula.pop(selectedCalc)
            save()
            exit()
        else:
            selectedCalc = int(request) - 1
            print(f"Selected '{calculatorID[selectedCalc]}'")
    
    # perform a quick calculation
    else:
        print("Please enter your calculator in this format:")
        print("Variables must be single lettered. The same letter represents the same variable.\n"
          "Seperate operations and variables with a space. Join the negative sign with the variable.\n"
          "+ = addition, - = subtraction, * = multiplication, / = division\n"
          "% = modulus, ^ = exponentiation")
        calculatorFormula.append(input())
        selectedCalc = len(calculatorFormula) - 1

    print("-----------")

    # find variables
    print(calculatorFormula[selectedCalc])
    vars = []
    equation = []
    for i in range(len(calculatorFormula[selectedCalc])):
        equation.append(calculatorFormula[selectedCalc][i])
        if calculatorFormula[selectedCalc][i].isalpha() and not calculatorFormula[selectedCalc][i] in vars:
            vars.append(calculatorFormula[selectedCalc][i])
    
    # kill quick calculation
    if mode == "Q":
        calculatorFormula.pop(selectedCalc)
    
    # substitute variables
    for i in range(len(vars)):
        varValue = int(input(f"Substitute {vars[i]} for: "))
        for tims in range(len(equation)):
            if equation[tims] == vars[i]:
                equation[tims] = varValue

    print("-----------")

    # calculate result
    question = equation
    solution = [] # Calculations

    # implement brackets
    """
    chunker = ""
    bracker = 0
    for i in range(len(question)):
        if (question[i] != "(") and (bracker == 0):
            if (question[i] == " "):
                solution.append(chunker)
                chunker = ""
            else:
                chunker = chunker + str(question[i])
        else:
            if (question[i] == ")"):
                bracker = 0
                chunker = chunker + str(question[i])
            else:
                bracker = 1
                chunker = chunker + str(question[i])
    solution.append(chunker)
    """

    while ("^" in solution):
        for e in range(len(solution)):
            if (solution[e] == "^"):
                solution.insert(e - 1, float(solution[e - 1]) ** float(solution[e + 1]))
                solution.pop(e)
                solution.pop(e)
                solution.pop(e)
                # print(solution)
                break

    while (("*" in solution) or ("/" in solution)):
        for m in range(len(solution)):
            if (solution[m] == "*"):
                solution.insert(m - 1, float(solution[m - 1]) * float(solution[m + 1]))
                solution.pop(m)
                solution.pop(m)
                solution.pop(m)
                # print(solution)
                break
            if (solution[m] == "/"):
                solution.insert(m - 1, float(solution[m - 1]) / float(solution[m + 1]))
                solution.pop(m)
                solution.pop(m)
                solution.pop(m)
                # print(solution)
                break

    while (("+" in solution) or ("-" in solution)):
        for a in range(len(solution)):
            if (solution[a] == "+"):
                solution.insert(a - 1, float(solution[a - 1]) + float(solution[a + 1]))
                solution.pop(a)
                solution.pop(a)
                solution.pop(a)
                # print(solution)
                break
            if (solution[a] == "-"):
                solution.insert(a - 1, float(solution[a - 1]) - float(solution[a + 1]))
                solution.pop(a)
                solution.pop(a)
                solution.pop(a)
                # print(solution)
                break
    print(solution)

# create a calculator
elif mode == "N":
    print("Please enter your calculator in this format:")
    print("Variables must be single lettered. The same letter represents the same variable.\n"
          "Seperate operations and variables with a space. Join the negative sign with the variable.\n"
          "+ = addition, - = subtraction, * = multiplication, / = division\n"
          "% = modulus, ^ = exponentiation")
    calculatorFormula.append(input())
    calculatorID.append(input("Give this calculator an identifying name: "))

# put it all back
save()
