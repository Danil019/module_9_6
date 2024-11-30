def all_variants(text):
    for length in range(1, len(text) + 1):  # Длина подпоследовательности от 1 до len(text)
        for i in range(len(text) - length + 1):  # Индекс начала для каждой длины
            yield text[i:i + length]


result = all_variants('abc')
for k in result:
    print(k)