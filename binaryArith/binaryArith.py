import copy
import random

binarySum = lambda a, b: bin(int(a, 2) + int(b, 2))
binaryDiff = lambda a, b: bin(int(a, 2) - int(b, 2))

def generateRandomBinary(n):
    key1 = ""

    for i in range(n):
        temp = str(random.randint(0, 1))
        key1 += temp

    return key1

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

    if twoscomp:
        # bool values to check if multd and multr are 2's comp
        dComp = False
        rComp = False

        # check for leading bit 1, if 2's comp numbers
        if multd[0] == "1":
            dComp = True

        if multr[0] == "1":
            rComp = True

    # set up product string
    resulting_product_length = len(multd) + len(multr)
    # populate prod with zeros
    prod = "0" * resulting_product_length

    while len(multd) < resulting_product_length:
        multd = "0" + multd

    questionVals = [[multd, multr, prod]]

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
            questionVals[len(questionVals)-1][2] = twosComp(questionVals[len(questionVals)-1][2], len(questionVals[len(questionVals)-1][2]))

    return questionVals


# binary division algorithm
def divAlg(dividend, divisor, twoscomp):

    # this is here because if the result of division is 0 then the remainder is the divisor, which wasn't kept
    # this needs to be cleaned up somehow, maybe when each value of the question is stored in an array
    original = divisor

    # padSize = len(dividend)
    # j = 0

    # if len(divisor) == 0:
    #     return

    if twoscomp:
        # bool values to check if multd and multr are 2's comp
        ddComp = False
        drComp = False

        # check for leading bit 1, if 2's comp numbers
        if dividend[0] == "1":
            ddComp = True
            dividend = twosComp(dividend, len(dividend))

        if divisor[0] == "1":
            drComp = True
            divisor = twosComp(divisor, len(divisor))

    # left justify divisor
    original_divisor_length = len(divisor)
    divisor = divisor + "0" * len(divisor)

    dividend = ("0" * len(original)) + dividend

    # quotient = max bit size with all bits unset
    quotient = "0" * original_divisor_length

    problem_values = [[dividend, divisor, quotient]]

    problem_values.append(copy.copy(problem_values[0])) # Initialization step

    for i in range(original_divisor_length + 1):
        original_remainder = copy.copy(problem_values[i+1][0])

        # remainder = remainder - divisor
        problem_values[i+1][0] = binaryDiff(problem_values[i+1][0], problem_values[i+1][1])

        if problem_values[i+1][0][0] == "-": # if remainder < 0 => change remainder back to original, sll quotient
            # rem += divisor
            problem_values[i+1][0] = original_remainder
            # dividend = binarySum(dividend, divisor)
            problem_values[i+1][2] = problem_values[i][2][1:]
            problem_values[i+1][2] += "0"
            # quotient += "0"
        else: # if remainder > 0 => keep remainder the same, pad out to proper size, sll quotient and make quotient[0] = 1
            problem_values[i+1][0] = problem_values[i+1][0][2:]
            problem_values[i+1][0] = "0" * ((original_divisor_length * 2) - len(problem_values[i+1][0])) + problem_values[i+1][0]

            problem_values[i+1][2] = problem_values[i][2][1:]
            problem_values[i+1][2] += "1"

        # shift divisor right
        shift_string = problem_values[i+1][1][:-1]
        problem_values[i+1][1] = "0" + shift_string
        # append next step
        problem_values.append(copy.copy(problem_values[i+1]))

    # quotient padding, pads up or down to length
    # problem_values[2] = quotient
    # if padSize - len(problem_values[0][2]) > 0:
    #     problem_values[2] = "0" * (padSize - len(problem_values[2])) + problem_values[2]
    # elif padSize - len(problem_values[2]) < 0:
    #     problem_values[2] = problem_values[2][abs(padSize - len(problem_values[2])):]


    # # dividend padding
    # if problem_values[2] == "0" * padSize:
    #     problem_values[0] = original
    # else:
    #     problem_values[0] = dividend[2:]

    #     if padSize - len(problem_values[0]) > 0:
    #         problem_values[0] = "0" * (padSize - len(problem_values[0])) + problem_values[0]

    # # divisor padding, idk what this value should be or mean
    # problem_values[1] = divisor[-1:]

    # add something here for 2's comp??
    if twoscomp:
        # match remainder to sign of dividend
        if ddComp:
            problem_values[0] = twosComp(problem_values[0], len(problem_values[0]))

            # handle if dividend and divisor have different signs
            if not drComp:
                problem_values[2] = twosComp(problem_values[2], len(problem_values[2]))

    return problem_values


# print(divAlg("0111", "0010", False))
