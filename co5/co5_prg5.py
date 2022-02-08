#dictionary to csv
import csv 
dict_value = [
{"name":"Manas","age":27,"course":"MBA"},
{"name":"Biju","age":23,"course":"MCA"},
{"name":"Ananghu","age":20,"course":"BSC"},
]

fields = ["name","age","course"]

with open('dictconverted.csv','w') as csvfile:
    writer = csv.DictWriter(csvfile,fieldnames=fields)
    writer.writeheader()
    writer.writerows(dict_value)
    csvfile.close()

with open('dictconverted.csv','r') as csvfiles:
    readerobj = csv.reader(csvfiles)
    for rows in readerobj:
        print(rows)


