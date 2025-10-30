def addBinary(a, b):
    carry = 0
    result = []

    i, j = len(a)-1, len(b)-1

    while i > 0 or j > 0 or carry:
        val_a = a[i] if i > 0 else 0
        val_b = a[j] if j > 0 else 0
        total = val_a + val_b + carry
        carry = total // 2
        result.append(str(total % 2))
        i -= 1
        j -= 1  

    return ''.join(reversed(result))