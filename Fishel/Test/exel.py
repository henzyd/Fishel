import pandas as pd 

df = pd.read_csv('Fishel/Test/a_file.csv')
print(df)

# x = []
# for i in df:
#     print('lmlm')
#     x.append(i)
# print(x)



import csv

with open('Fishel/Test/physics_highers.csv') as file_obj:
    heading = next(file_obj)
    reader_obj = csv.reader(file_obj)
    print(type(reader_obj))
    for row in reader_obj:
        # row[-1]
        print(row)
        