def get_keyword(ciphertext, key_len):
    key = ''
    frequency = [0.079, 0.014, 0.027, 0.041, 0.122, 0.021, 0.019, 0.059, 0.068, 0.002, 0.008, 0.039, 0.023,
                 0.065, 0.072, 0.018, 0.001, 0.058, 0.061, 0.088, 0.027, 0.010, 0.023, 0.002, 0.019, 0.010]
    text = [[0] * 26 for _ in range(key_len)]
    for i in range(len(ciphertext)):
        text[i % key_len][ord(ciphertext[i]) - 65] += 1
    for i in range(key_len):
        n = sum(text[i])
        for j in range(26):
            text[i][j] = round(text[i][j] / n, 3)
    for t in text:
        m = float("inf")
        r = 0
        for i in range(26):
            diff = 0
            for j in range(26):
                diff += abs(frequency[j] - t[(j + i) % 26])
            if diff < m:
                m = diff
                r = i
        key += chr(r + 65)
    return key