import csv
player_number = 24190286
file = r"C:\Users\shree\OneDrive - Southern Cross University\Desktop\Dhruv_Patel_A1\Part_1\playerCustomisation.csv"
with open(file, "r") as input_file:
   reader = csv.reader(input_file)
   for row in reader:
       file_player_number = row[0]
       print(file_player_number)
       if file_player_number == player_number:
           width = row[1]
           height = row[2]
           monster_count = row[3]
           wall_count = row[4]
           energy_count = row[5]
           animal = row[6]
           sound = row[7]            