def sum(a, b):
    result = []
    for i in range(len(a)):
        row = []
        for j in range(len(a[0])):
            row.append(a[i][j] + b[i][j])
        result.append(row)

    return result


def minus(a, b):
    result = []
    for i in range(len(a)):
        row = []
        for j in range(len(a[0])):
            row.append(a[i][j] - b[i][j])
        result.append(row)

    return result


def mult(a, b):
    result = []
    for i in range(len(a)):
        row = []
        for j in range(len(b[0])):
            sum = 0
            for k in range(len(a[0])):
                sum += a[i][k] * b[k][j]
            row.append(sum)
        result.append(row)

    return result


operation = {
    "sum": sum,
    "minus": minus,
    "mult": mult,
}
