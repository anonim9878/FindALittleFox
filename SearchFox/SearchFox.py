from Objects import objects_in_game
from datetime import date
from datetime import datetime
import random
class World():
    def __init__(self):
        self.__size_board_x, self.__size_board_y = None, None
        self.__board = None
        self.__lis_safe_place = []
        self.__lis_obj = []
        self.__lis_animals = []
        self.__lis_foods = []
        self.__lis_terrains = []
        self.__fox = None
    def getFox(self):
        return self.__fox
    def getSizeBoardX(self):
        return self.__size_board_x
    def generate_world(self):
        self.__size_board_x, self.__size_board_y = 58, 58
        self.__board = objects_in_game.Board(self.__size_board_x, self.__size_board_y)
        for i in range(0, 50, 1):
            #Создаём случайный спавн безопасных мест для лисёнка(и других объектов подобным образом)
            coordinats = 0
            coordinats_x = 0
            coordinats_y = 0
            check = False
            while check == False: 
                check = True
                coordinats_x = random.randint(0, self.__size_board_x - 1) 
                coordinats_y = random.randint(0, self.__size_board_y - 1) * self.__size_board_x
                coordinats = coordinats_x + coordinats_y
                if len(self.__lis_obj) == 0:
                    break
                for i in self.__lis_obj:
                    if i.getCoordinats() == coordinats:
                        check = False
                        break
            choice_sim = random.randint(0, 2)
            if choice_sim == 0:
                choice_sim = "T"
            elif choice_sim == 1:
                choice_sim = "*"
            else:
                choice_sim = "Q"
            n_obj = objects_in_game.Object(coordinats_x, coordinats_y, choice_sim)
            self.__lis_safe_place.append(n_obj)
            self.__lis_obj.append(n_obj)
        for i in range(0, 30, 1):
            #Создаём случайный спавн еды(и других объектов подобным образом)
            coordinats = 0
            coordinats_x = 0
            coordinats_y = 0
            check = False
            while check == False: 
                check = True
                coordinats_x = random.randint(0, self.__size_board_x - 1) 
                coordinats_y = random.randint(0, self.__size_board_y - 1) * self.__size_board_x
                coordinats = coordinats_x + coordinats_y
                if len(self.__lis_obj) == 0:
                    break
                for i in self.__lis_obj:
                    if i.getCoordinats() == coordinats:
                        check = False
                        break
            choice_sim = random.randint(0, 1)
            if choice_sim == 0:
                choice_sim = "P"
            else:
                choice_sim = "A"
            n_obj = objects_in_game.Object(coordinats_x, coordinats_y, choice_sim)
            self.__lis_foods.append(n_obj)
            self.__lis_obj.append(n_obj)
        for i in range(0, 15, 1):
            #Создаём случайный спавн местностей(и других объектов подобным образом)
            coordinats = 0
            coordinats_x = 0
            coordinats_y = 0
            check = False
            while check == False: 
                check = True
                coordinats_x = random.randint(0, self.__size_board_x - 1) 
                coordinats_y = random.randint(0, self.__size_board_y - 1) * self.__size_board_x
                coordinats = coordinats_x + coordinats_y
                if len(self.__lis_obj) == 0:
                    break
                for i in self.__lis_obj:
                    if i.getCoordinats() == coordinats:
                        check = False
                        break
            n_obj = objects_in_game.TerrainAnimals(coordinats_x, coordinats_y, "O", 20)
            self.__lis_terrains.append(n_obj)
            self.__lis_obj.append(n_obj)
        for i in range(0, 2, 1):
            #Создаём случайный спавн животных(и других объектов подобным образом)
            coordinats = 0
            coordinats_x = 0
            coordinats_y = 0
            check = False
            while check == False: 
                check = True
                coordinats_x = random.randint(0, self.__size_board_x - 1) 
                coordinats_y = random.randint(0, self.__size_board_y - 1) * self.__size_board_x
                coordinats = coordinats_x + coordinats_y
                if len(self.__lis_obj) == 0:
                    break
                for i in self.__lis_obj:
                    if i.getCoordinats() == coordinats:
                        check = False
                        break
            n_obj = objects_in_game.Animal(coordinats_x, coordinats_y, self.__size_board_x, "V", 30, 20, 5)
            self.__lis_animals.append(n_obj)
            self.__lis_obj.append(n_obj)
        #Генерируем лису
        coordinats = 0
        coordinats_x = 0
        coordinats_y = 0
        check = False
        while check == False: 
            check = True
            coordinats_x = random.randint(0, self.__size_board_x - 1) 
            coordinats_y = random.randint(0, self.__size_board_y - 1) * self.__size_board_x
            coordinats = coordinats_x + coordinats_y
            if len(self.__lis_obj) == 0:
                break
            for i in self.__lis_obj:
                if i.getCoordinats() == coordinats:
                    check = False
                    break
        self.__fox = objects_in_game.Fox(coordinats_x, coordinats_y, self.__size_board_x, "F", 1, 1, 2, 200)
        self.__lis_animals.append(self.__fox)
        self.__lis_obj.append(self.__fox)
    def current_world(self):
        for i in self.__lis_animals:
            if i == self.__fox:
                i.behavior(self.__lis_animals, self.__lis_foods, self.__lis_terrains, self.__lis_safe_place, self.__lis_obj)
            else:
                i.behavior(self.__lis_animals, self.__lis_foods, self.__lis_terrains, self.__lis_obj)
        for i in self.__lis_terrains:
            i.behavior()
        self.__board.print_board1(self.__lis_obj)
        if len(self.__lis_foods) < 30:
            spawn = 15 - len(self.__lis_foods)
            for i in range(0, spawn, 1):
                #Создаём случайный спавн еды(и других объектов подобным образом)
                coordinats = 0
                coordinats_x = 0
                coordinats_y = 0
                check = False
                while check == False: 
                    check = True
                    coordinats_x = random.randint(0, self.__size_board_x - 1) 
                    coordinats_y = random.randint(0, self.__size_board_y - 1) * self.__size_board_x
                    coordinats = coordinats_x + coordinats_y
                    if len(self.__lis_obj) == 0:
                        break
                    for i in self.__lis_obj:
                        if i.getCoordinats() == coordinats:
                            check = False
                            break
                choice_sim = random.randint(0, 1)
                if choice_sim == 0:
                    choice_sim = "P"
                else:
                    choice_sim = "A"
                n_obj = objects_in_game.Object(coordinats_x, coordinats_y, choice_sim)
                self.__lis_foods.append(n_obj)
                self.__lis_obj.append(n_obj)
class Player():
    def __init__(self, count_move):
        self.__count_move = count_move
        self.__max_count_move = count_move
    def getCountMove(self):
        return self.__count_move
    def getMaxCountMove(self):
        return self.__max_count_move
    def to_go(self, move_x, move_y):
        print("Count move: ", self.__count_move , "/", self.__max_count_move)
        self.__count_move -= 1
        while True:
            try:
                move_x = input("Input X coordinat(input Enter for scipe move): ")
                if move_x == "":
                    break
                else:
                    move_x = int(move_x)
                break
            except ValueError:
                print("\nValue error\n")
        if move_x == "":
            move_x = -1
            move_y = -1
            return move_x, move_y
        while True:
            try:
                move_y = int(input("Input Y coordinat: "))
                break
            except ValueError:
                print("\nValue error")
        return move_x, move_y
class Game():
    def __init__(self):
        self.__world_obj = None
        self.__end_game = False
        self.__player = None
        self.__choice = ""
        self.__scene1 = """\n ____o
/ |  |    - You found the foxly!"""
        self.__scene2 = """\n ____X
/ /  /    - You found the DIE foxly!"""
        self.__scene3 = """\n\\____W
 |  |    - You was die by fox!"""
        self.__scene4 = """\n ________X
 /  /    - Foxly die."""
    def main(self):
        while self.__choice != "n":
            move_x = 0
            move_y = 0
            self.__world_obj = World()
            self.__end_game = False
            self.__player = Player(3000)
            self.__world_obj.generate_world()
            while self.__end_game == False:
                self.__world_obj.current_world()
                move_x, move_y = self.__player.to_go(move_x, move_y)
                move_y *= self.__world_obj.getSizeBoardX()
                self.__check_end_game(move_x, move_y)
            self.__restart()
        input("\n\t\t\t\t\t\t\t\t\t\t\t\t  ___\n\t\t\t\t\t\t\t\t\t\t\t\t</OIO\\>\n\t\t\t\t\t\t\t\t\t\t\t\t \\ I / \n\t\t\t\t\t\t\t\t\t\t\t\t  \\I/  Bye!")
    def __check_end_game(self, move_x, move_y):
        if move_x + move_y == (self.__world_obj.getFox()).getCoordinats() and (self.__world_obj.getFox()).getDieStatus() == False:
            self.__end_game_scenes(1)
            self.__end_game = True
        elif (move_x + move_y == (self.__world_obj.getFox()).getCoordinats()) and (self.__world_obj.getFox()).getDieStatus():
            self.__end_game_scenes(2)
            self.__end_game = True
        elif self.__player.getCountMove() <= 0 and (self.__world_obj.getFox()).getDieStatus() == False:
            self.__end_game_scenes(3)
            self.__end_game = True
        elif self.__player.getCountMove() <= 0 and (self.__world_obj.getFox()).getDieStatus():
            self.__end_game_scenes(4)
            self.__end_game = True
    def __end_game_scenes(self, number):
        end = [self.__scene1, self.__scene2, self.__scene3, self.__scene4]
        rezult_file = open("rezult_game.txt", "a", encoding='utf-8')
        today = date.today()
        time = datetime.now()
        current_time = time.strftime("%H:%M:%S")
        rezult_file.write("\n\n---------------------------------------------------------------------------------------------\n")
        print(end[number - 1])
        rezult_file.write(end[number - 1])
        rezult_file.write("\n---------------------------------------------------------------------------------------------\n\nSteps: " + str(self.__player.getCountMove()) + "/" + str(self.__player.getMaxCountMove()) + "\t\t\t\t\t\t Date and Time: " + str(today) + " " + str(current_time))
    def __restart(self):
        print("\n\nYou want restart the game?")
        self.__choice = ""
        while self.__choice != "y" and self.__choice != "n":
            self.__choice = input("\ny - restart, n - exit: ")
game = Game()
game.main()