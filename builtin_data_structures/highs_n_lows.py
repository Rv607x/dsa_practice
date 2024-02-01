def count_low_high(num_list):
    lows = []
    highs = []
    for i in num_list:
        if i > 50 or i % 3 == 0:
            highs.append(i)
        else:
            lows.append(i)
    output = []
    output.append(len(highs))
    output.append(len(lows))
    return output

print(count_low_high([-10, 90, 15, 43]))