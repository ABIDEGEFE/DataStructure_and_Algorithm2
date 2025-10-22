def canConstruct(ransomNote, magazine):
    """
    :type ransomNote: str
    :type magazine: str
    :rtype: bool
    """

    freq = {}

    for i in ransomNote:
        freq[i] = freq.get(i, 0) + 1
    print(freq)
    for i in magazine:
        if i in freq:
            freq[i] = freq[i] - 1
            if freq[i] == 0:
                del freq[i]

    return len(freq) == 0


print(canConstruct("", "b"))