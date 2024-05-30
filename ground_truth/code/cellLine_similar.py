import csv

'''
    If two cell lines share 10 of the key genes mutated, the relationship between the cell lines is considered similar
'''

with open('../data/Number_of_co-mutated_genes.csv', 'r') as csv_file, open('../data/cellLine_similarity.csv', 'w', newline='') as new_csv_file:
    csv_reader = csv.reader(csv_file)
    csv_writer = csv.writer(new_csv_file)

    for row in csv_reader:
        first_column_data = row[0].split('_')

        first_column_part1 = first_column_data[0]
        first_column_part2 = first_column_data[1]

        second_column_data = int(row[1])

        if second_column_data >= 10:
            third_column_data = 1
        else:
            third_column_data = 0

        csv_writer.writerow([first_column_part1, first_column_part2, third_column_data])
