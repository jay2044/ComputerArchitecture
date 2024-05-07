import copy
binarySum = lambda a, b: bin(int(a, 2) + int(b, 2))
binaryDiff = lambda a, b: bin(int(a, 2) - int(b, 2))

# computes the 2's complement of binary numbers
def twosComp(n, size):

    # where to store converted binary
    binResult = ""

    i = size - 1
    # finding first 1
    while n[i] != "1" and i >= 0:
        binResult = n[i] + binResult
        i -= 1

    if i == -1:
        return binResult

    binResult = n[i] + binResult
    i -= 1

    # flipping the rest of the bits
    while i > -1:
        if n[i] == "1":
            binResult = "0" + binResult
        else:
            binResult = "1" + binResult
        i -= 1

    return binResult


# binary multiplication algorithm, should return an array of computational values
def multAlg(multd, multr, twoscomp):

    # set up product string
    resulting_product_length = len(multd) + len(multr)
    # populate prod with zeros
    prod = "0" * resulting_product_length

    while len(multd) < resulting_product_length:
        multd = "0" + multd

    questionVals = [[multd, multr, prod]]

    if twoscomp:
        # bool values to check if multd and multr are 2's comp
        dComp = False
        rComp = False

        # check for leading bit 1, if 2's comp numbers
        if questionVals[0][0][0] == "1":
            dComp = True

        if questionVals[0][1][0] == "1":
            rComp = True

    questionVals.append(copy.copy(questionVals[0]))  # Initialization step
    multiplier_length = len(multr)

    # iterate multiplier length times and calculate the product step-by-step
    for i in range(multiplier_length):
        # if ending bit is 1 add multiplicand to product
        if questionVals[i+1][1][len(multr) - 1] == "1":
            tempStr = binarySum(questionVals[i+1][2], questionVals[i+1][0])
            questionVals[i+1][2] = tempStr[2:]  # removes 0b

            current_product_length = len(questionVals[i+1][2])
            while current_product_length < resulting_product_length:
                questionVals[i+1][2] = "0" + questionVals[i+1][2]
                current_product_length += 1

        # shift multd left
        questionVals[i+1][0] += "0"
        questionVals[i+1][0] = questionVals[i+1][0][1:]

        # shift multr right
        shiftString = ("0" + questionVals[i+1][1])
        questionVals[i+1][1] = shiftString[:-1]
        questionVals.append(copy.copy(questionVals[i+1]))
    questionVals[len(questionVals)-1][0] = "final"
    questionVals[len(questionVals)-1][1] = "product"

    if twoscomp:
        # check for need to twoscomp product
        if dComp and not rComp or not dComp and rComp:
            questionVals[len(questionVals)-1][2] = twoscomp(questionVals[2], len(questionVals[2]))

    return questionVals


# binary division algorithm
def divAlg(n, m):
    
    dividend = n
    divisor = m
    quotient = ""

    j = 0
    while j != m and divisor[j] != "1":
        j += 1

    if j == m:
        return

    j += 1
    # bool values to check if multd and multr are 2's comp
    ddComp = False
    drComp = False

    # check for leading bit 1, if 2's comp numbers
    if dividend[0] == "1":
        ddComp = True
        dividend = twosComp(dividend, n)

    if divisor[0] == "1":
        drComp = True
        divisor = twosComp(divisor, m)

    # right justify divisor
    for i in range(m):
        divisor = divisor + "0"

    # setting the new size of divisor
    m *= 2

    size = m
    j = m - j

    # algo loop
    for i in range(j):

        # remainder = remainder - divisor
        dividend = binaryDiff(dividend, divisor)

        # cond dividend[0] == '1'
        if dividend[0] == "-":
            # rem += divisor
            dividend = binarySum(dividend, divisor)
            quotient += "0"
        else:
            quotient += "1"

        # shift divisor right
        divisor = list(divisor)
        divisor.pop()
        divisor = "".join(divisor)
        size = size - 1

    #add something here for 2's comp??

    #this should return an array of all the values needed to give the question
    return


print(multAlg("0010", "0011", False))
