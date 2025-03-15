with open("file.csv") as file:
    all_data=file.readlines()

for i in range(len(all_data)):
    all_data[i]=all_data[i].replace("\n","")

print(all_data)