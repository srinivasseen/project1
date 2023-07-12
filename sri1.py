import csv
from collections import defaultdict

word_counts = defaultdict(int)

with open('test.txt', 'r') as in_file:
    for line in in_file:
        words = line.split()
        for word in words:
            word_counts[word] += 1

with open('demo copy.csv', 'w', newline='') as out_file:
    writer = csv.writer(out_file)
    writer.writerow(['Word', 'Count'])
    for word, count in word_counts.items():
        writer.writerow([word, count])
        print(word, count)
