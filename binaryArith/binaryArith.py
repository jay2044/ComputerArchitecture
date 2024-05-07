
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
def multAlg(multd, multr):

    # set up product string
    prod = ""
    prodLen = len(multd) + len(multr)
    # populate prod with zeros
    for i in range(prodLen):
        prod += "0"

    questionVals = [multd, multr, prod]

    # bool values to check if multd and multr are 2's comp
    dComp = False
    rComp = False

    #multiplicationPrompt(multd, multr)

    # check for leading bit 1, if 2's comp numbers
    if questionVals[0][0] == "1":
        dComp = True
        questionVals[0] = twosComp(questionVals[0], len(questionVals[0]))

    if questionVals[1][0] == "1":
        rComp = True
        questionVals[1] = twosComp(questionVals[1], len(questionVals[1]))

    
    size = len(multr)
    #need to update logic in this loop to get the intermediate values into the array to return the full process for question creation
    for i in range(len(multr)):

        # if ending bit is 1 add multiplicand to product
        if questionVals[1][len(multr) - 1] == "1":
            tempStr = binarySum(questionVals[2], questionVals[0])
            questionVals[2] = tempStr[2:]  # removes 0b

            curlen = len(questionVals[2])
            while curlen < prodLen:
                questionVals[2] = "0" + questionVals[2]
                curlen += 1

        # shift multd left
        questionVals[0] += "0"

        # shift multr right
        shiftString = ("0" + questionVals[1])
        questionVals[1] = shiftString[:-1]
        
        size = size - 1

    # check for need to 2's comp the prod
    if dComp and not rComp or not dComp and rComp:
        prod = twosComp(prod, prodLen)
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
