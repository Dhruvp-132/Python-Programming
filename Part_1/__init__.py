import csv

class PlayerCustomization:
    def __init__(self, width, height, num_monsters, num_walls, player_animal, player_sound):
        self.width = width
        self.height = height
        self.num_monsters = num_monsters
        self.num_walls = num_walls
        self.player_animal = player_animal
        self.player_sound = player_sound

    def __str__(self):
        return f"Player Customization:\nWidth: {self.width}\nHeight: {self.height}\nNumber of Monsters: {self.num_monsters}\nNumber of Walls: {self.num_walls}\nPlayer's Animal: {self.player_animal}\nPlayer's Sound: {self.player_sound}"


file_path = r"C:\Users\shree\OneDrive - Southern Cross University\Desktop\Dhruv_Patel_A1\Part_1\playerCustomisation.csv"

player_id = int(input("Enter the last digit of your student ID: "))
with open(file_path, "r") as input_file:
    reader = csv.reader(input_file)
    for i, row in enumerate(reader):
        if i == player_id + 1: 
            player_data = PlayerCustomization(*map(int, row[1:5]), row[6], row[7])
            print(player_data)
            break