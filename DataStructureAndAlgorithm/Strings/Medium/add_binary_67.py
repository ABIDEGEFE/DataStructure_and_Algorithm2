def addBinary(a, b):
    """
    :type a: str
    :type b: str
    :rtype: str
    """
    binary_value = {
        0 : "0",
        1: "1",
        2 : "10",
        3 : "11",
        4: "100",
        5: "101",
        6: "110",
        7: "111",
        8: "1000",
        9: "1001"
    }

    min_bin = ""
    if len(a) > len(b):
        min_bin = b
    else:
        min_bin = a
    max_bin = max(len(a), len(b))

    for i in range(max_bin - len(min_bin)):
        min_bin = "0" + min_bin

    carry = 0
    result = ""
    
    if len(a) != len(b):
        if len(a) < len(b):
            a = min_bin
        else:
            b = min_bin

    print(a, b)

    for i in range(len(min_bin)-1, -1, -1):
        a_val = int(a[i])
        b_val = int(b[i])
        sm = carry + a_val + b_val

        bin_val = binary_value[sm]
        if len(bin_val) > 1:
            carry = int(bin_val[0])
            stored_val = bin_val[-1]
            result = stored_val + result
        else:
            carry = 0
            stored_val = bin_val[0]
            result = stored_val + result

    if carry == 1:
        result = "1" + result

    return result


print(addBinary("11", "1"))  # Output: "100"