import random
#Класс доски. 
class Board:
    def __init__(self, xsize, ysize):
        self.__xsize = xsize
        self.__ysize = ysize
    def print_board1(self, lis_obj):
        #Заполняем список для отоброжения объектов. Сначала заполняем его пустотой, чтобы потом её заменить на символы объектов без помех.
        lis_ter = []
        for i in range(0, self.__xsize * self.__ysize, 1):
            lis_ter.append("   ") #Заполняем 3 пробелами, т.к. в некоторых случаях в игре потребуется именно столько места.
        #Добавляем объекты в соответствующие ячейки.
        for n_obj in lis_obj:
            lis_ter[n_obj.getCoordinats()] = n_obj.getSimbol()
        #Печатаем доску
        index = -1
        board = "   ="
        for i in range(0, self.__xsize * 4, 1):
            board += "="
        board += "\n   |"
        for i in range(0, self.__xsize, 1):
            if i <= 9:
                board += " " + str(i) + " |"
            else:
                board += " " + str(i) + "|"
        board += "\n===="
        for i in range(0, self.__xsize * 4, 1):
            board += "="
        for i in range(0, self.__ysize, 1):
            #board += "\n----"
            #for x in range(0, self.__xsize * 4, 1):
                #board += "-"
            board += "\n"
            if i <= 9:
                board += " " + str(i) + " |"
            elif i*self.__xsize > 9 and i <= 99:
                board += " " + str(i) + "|"
            elif i*self.__xsize > 99:
                board += str(i) + "|"
            for x in range(0, self.__xsize, 1):
                index += 1
                board += lis_ter[index] + "|"
        board += "\n===="
        for i in range(0, self.__xsize * 4, 1):
            board += "="
        print(board)
class Object:
    def __init__(self, coordinats_x, coordinats_y, simbol):
        self.__coordinats_x = coordinats_x
        self.__coordinats_y = coordinats_y
        self.__coordinats = coordinats_x + coordinats_y
        self.__simbol = " " + simbol + " "
    def getCoordinats(self):
        return self.__coordinats
    def getCoordinatsX(self):
        return self.__coordinats_x
    def getCoordinatsY(self):
        return self.__coordinats_y
    def getSimbol(self):
        return self.__simbol
class Animal(Object):
    def __init__(self, coordinats_x, coordinats_y, size_board_x, simbol, strong, ter_damage, speed):
        super().__init__(coordinats_x, coordinats_y, simbol)
        self.__size_board_x = size_board_x
        self.__standart_simbol = simbol
        self.__strong = strong
        self.__coordinats_terrain_animal_x = -1
        self.__coordinats_terrain_animal_y = -1 
        self.__speed = speed
        self.__terrain_index = -1
        self.__terrain_damage = ter_damage
        self.__occupation = self.__coordinats_terrain_animal_y == self._Object__coordinats_y and self.__coordinats_terrain_animal_x == self._Object__coordinats_x
        self.__terrain = None
        self.__animal_for_attack = None
        self.__index_animal_for_attack = None
        self.__index_food = None
    def __setCoordinats_terrain_animals(self, terrains_animals):
        iteration = 0
        while True:
            iteration += 1
            index = random.randint(0, len(terrains_animals) - 1)
            terrain_index = index
            terrain = terrains_animals[terrain_index]
            if (terrain.getRepairStatus() or self.__terrain_index == terrain_index) and iteration != 1000:    
                continue
            else:
                if iteration == 1000:
                    print("|ВЫБРАНА АБСОЛЮТНО СЛУЧАЙНАЯ МЕСТНОСТЬ|")
                    break
                #Если мы пережили нападение, то выбираем ту местность, дорога к которой не будет пересекаться с дорогой нападавшего
                if self.__animal_for_attack != None:
                    x_check_right = self.__animal_for_attack.getCoordinatsX() >= self._Object__coordinats_x and terrain.getCoordinatsX() < self._Object__coordinats_x
                    x_check_left = self.__animal_for_attack.getCoordinatsX() <= self._Object__coordinats_x and terrain.getCoordinatsX() > self._Object__coordinats_x
                    y_check_down = self.__animal_for_attack.getCoordinatsY() >= self._Object__coordinats_y and terrain.getCoordinatsY() < self._Object__coordinats_y
                    y_check_up = self.__animal_for_attack.getCoordinatsY() <= self._Object__coordinats_y and terrain.getCoordinatsY() > self._Object__coordinats_y
                    if x_check_left or x_check_right or y_check_down or y_check_up:
                        break
                else:
                    break
        self.__terrain_index = terrain_index
        self.__coordinats_terrain_animal_x = terrain.getCoordinatsX()
        self.__coordinats_terrain_animal_y = terrain.getCoordinatsY()
    def __move_to_ter(self):
        #Передвижение животного. Если скорость не больше разницы расстояний между координатами места и животного, то используем её, иначе используем разницу
        if self.__coordinats_terrain_animal_x < self._Object__coordinats_x:
            if self._Object__coordinats_x - self.__speed >= self.__coordinats_terrain_animal_x:
                self._Object__coordinats_x -= self.__speed
            else:
                self._Object__coordinats_x -= -(self.__coordinats_terrain_animal_x - self._Object__coordinats_x)
        elif self.__coordinats_terrain_animal_x > self._Object__coordinats_x:
            if self._Object__coordinats_x + self.__speed <= self.__coordinats_terrain_animal_x:
                self._Object__coordinats_x += self.__speed
            else:
                self._Object__coordinats_x += -(self._Object__coordinats_x - self.__coordinats_terrain_animal_x)
        if self.__coordinats_terrain_animal_y < self._Object__coordinats_y:
            if self._Object__coordinats_y - self.__speed * self.__size_board_x >= self.__coordinats_terrain_animal_y:
                self._Object__coordinats_y -= self.__speed * self.__size_board_x
            else:
                self._Object__coordinats_y -= -(self.__coordinats_terrain_animal_y - self._Object__coordinats_y) 
        elif self.__coordinats_terrain_animal_y > self._Object__coordinats_y:
            if self._Object__coordinats_y + self.__speed * self.__size_board_x <= self.__coordinats_terrain_animal_y:
                self._Object__coordinats_y += self.__speed * self.__size_board_x
            else:
                self._Object__coordinats_y +=  -(self._Object__coordinats_y - self.__coordinats_terrain_animal_y) 
    def __occupation_area(self, ter):
        self._Object__simbol = self.__standart_simbol + "O "
        if ter.getHP() != 0:
            ter.setHP(ter.getHP() - self.__terrain_damage)
            ter.setOccupationStatus(True)
        else:
            self._Object__simbol = " " + self.__standart_simbol + " "
            self.__terrain_index = -1
            ter.setOccupationStatus(False)
    def get_Strong(self):
        return self.__strong
    def __attack(self, animal):
        #В случаи с лисёнком пишем отдельный код из-за её особенностей и последующей логики(подыхать и прятаться)
        #print("Attack!!!")
        win_rate = (self.__strong / (self.__strong + animal.get_Strong())) * 100
        dice = random.randint(0, 100)
        if win_rate >= dice:
            animal.defeat()
        else:
            self.defeat()
        self.__animal_for_attack = animal
    def __check_out_from_area_attack(self, animal):
        left_area = animal.getCoordinatsX() > (self._Object__coordinats_x - self.__speed)
        right_area = animal.getCoordinatsX() < (self._Object__coordinats_x + self.__speed)
        up_area = animal.getCoordinatsY() > (self._Object__coordinats_y - (self.__speed * self.__size_board_x))
        down_area = animal.getCoordinatsY() < (self._Object__coordinats_y + (self.__speed * self.__size_board_x))
        if self.__animal_for_attack != None:
            if self.__animal_for_attack == animal:
                if left_area and right_area and up_area and down_area and animal != self:
                    pass
                else:
                    self.__animal_for_attack = None
                    self.__index_animal_for_attack = None
    def defeat(self):
        self.__terrain_index = -1
        if self.__occupation:
            self.__terrain.setOccupationStatus(False)
            self._Object__simbol = " " + self.__standart_simbol + " "
    def __check_other_animals(self, animals):
        for i in animals:
            left_area = i.getCoordinatsX() > (self._Object__coordinats_x - self.__speed)
            right_area = i.getCoordinatsX() < (self._Object__coordinats_x + self.__speed)
            up_area = i.getCoordinatsY() > (self._Object__coordinats_y - (self.__speed * self.__size_board_x))
            down_area = i.getCoordinatsY() < (self._Object__coordinats_y + (self.__speed * self.__size_board_x))
            #Если у нас была проведена атака, то проверяем, вышли ли мы из поля боя
            if self.__animal_for_attack != None:
                self.__check_out_from_area_attack(i)
            #Проверяем, нет ли в нашем радиусе животных
            if left_area and right_area and up_area and down_area and i != self and i != self.__animal_for_attack:
                self.__attack(i)
                break
    def __eat(self, food, lis_foods, lis_obj):
        self._Object__coordinats_x = food.getCoordinatsX()
        self._Object__coordinats_y = food.getCoordinatsY()
        #Удаляем еду, будто мы её съели. Удаляем с двух списков, тк указатели на объект существуют в обоих списках
        index = -1
        for i in lis_foods:
            index += 1
            if i == food:
                del lis_foods[index]
                break
        index = -1
        for i in lis_obj:
            index += 1
            if i == food:
                del lis_obj[index]
                break
    def __check_foods(self, foods, lis_obj):
        rezult_check = False
        for i in foods:
            left_area = i.getCoordinatsX() >= (self._Object__coordinats_x - self.__speed)
            right_area = i.getCoordinatsX() <= (self._Object__coordinats_x + self.__speed)
            up_area = i.getCoordinatsY() >= (self._Object__coordinats_y - (self.__speed * self.__size_board_x))
            down_area = i.getCoordinatsY() <= (self._Object__coordinats_y + (self.__speed * self.__size_board_x))
            #Проверяем, нет ли в нашем радиусе животных
            if left_area and right_area and up_area and down_area and i != self and i != self.__animal_for_attack:
                self.__eat(i, foods, lis_obj)
                rezult_check = True
                break
        return rezult_check
    def behavior(self, animals, foods, terrain_animals, lis_obj):
        if self.__terrain_index == -1:
            self.__setCoordinats_terrain_animals(terrain_animals)
        self.__occupation = self.__coordinats_terrain_animal_y == self._Object__coordinats_y and self.__coordinats_terrain_animal_x == self._Object__coordinats_x
        self.__terrain = terrain_animals[self.__terrain_index]
        if self.__occupation:
            self.__occupation_area(self.__terrain)
        else:
            if self.__index_animal_for_attack != None:
                self.__animal_for_attack = animals[self.__index_animal_for_attack]
            self.__check_other_animals(animals)
            if self.__animal_for_attack != None and self.__index_animal_for_attack == None:
                x = 0
                for i in animals:
                    if i == self.__animal_for_attack:
                        self.__index_animal_for_attack = x
                    x += 1
            else:
                if self.__check_foods(foods, lis_obj):
                    pass
                else:
                    self.__move_to_ter()
        self._Object__coordinats = self._Object__coordinats_y + self._Object__coordinats_x
class TerrainAnimals(Object):
    def __init__(self, coordinats_x, coordinats_y, simbol, hp):
        super().__init__(coordinats_x, coordinats_y, simbol)
        self.__MAX_HP = hp
        self.__hp = hp
        self.__occupation_status = False
        self.__repair_status = False
    def getOccupationStatus(self):
        return self.__occupation_status
    def getRepairStatus(self):
        return self.__repair_status
    def getHP(self):
        return self.__hp
    def setHP(self, val):
        try:
            if val < 0:
                self.__hp = 0
            else:
                self.__hp = val
        except TypeError:
            print(val, " не int")
    def setOccupationStatus(self, val):
        if val != True and val != False:
            print("Я не могу присвоить значение ", val, ", т.к. оно не булевое")
            return
        self.__occupation_status = val
    def __repair(self):
        self.__hp += 1
        self._Object__simbol = " X "
        self.__repair_status = True
    def behavior(self):
        if self.__hp < self.__MAX_HP and self.__occupation_status == False:
            self.__repair()
        else:
            self._Object__simbol = " O "
            self.__repair_status = False
    def getCoordinatsX(self):
        return self._Object__coordinats_x
    def getCoordinatsY(self):
        return self._Object__coordinats_y
#И, наконец, лисёнок
class Fox(Animal):
    def __init__(self, coordinats_x, coordinats_y, size_board_x, simbol, strong, ter_damage, speed, time_growing):
        super().__init__(coordinats_x, coordinats_y, size_board_x, simbol, strong, ter_damage, speed)
        self.__die_status = False
        self.__TIME_GROWING = time_growing
        self.__time_growing_now = 0
        self.__safe_terrain = None
        self.__action_retreat = False
    def __growing(self):
        self.__time_growing_now += 1
        if self.__time_growing_now >= self.__TIME_GROWING:
            self._Animal__speed += 1
            self._Animal__strong += 1
            self.__time_growing_now = 0
    def getDieStatus(self):
        return self.__die_status
    def __retreat(self):
        print("Retreat")
        rezult_check = False
        for i in self.__safe_terrain:
            left_area = i.getCoordinatsX() >= (self._Object__coordinats_x - self._Animal__speed)
            right_area = i.getCoordinatsX() <= (self._Object__coordinats_x + self._Animal__speed)
            up_area = i.getCoordinatsY() >= (self._Object__coordinats_y - (self._Animal__speed * self._Animal__size_board_x))
            down_area = i.getCoordinatsY() <= (self._Object__coordinats_y + (self._Animal__speed * self._Animal__size_board_x))
            #Проверяем, нет ли в нашем радиусе безопасных мест
            if left_area and right_area and up_area and down_area:
                #Если есть, то тп туда(по идее под его знаком, но у меня будет совмещёнка)
                self._Object__simbol = self._Animal__standart_simbol + "Sa"
                self._Object__coordinats_x = i.getCoordinatsX()
                self._Object__coordinats_y = i.getCoordinatsY()
                self.__action_retreat = True
                rezult_check = True
                break
        return rezult_check
    def __die(self):
        self.__die_status = True
        self._Object__simbol = self._Animal__standart_simbol + "Di"
    def defeat(self):
        if self.__retreat():
            return
        else:
            print("Die")
            self.__die()
            return super().defeat()
    def behavior(self, animals, foods, terrain_animals, safe_terrain, lis_obj):
        if self.__die_status:
            if self._Object__simbol != self._Animal__standart_simbol + "Di":
                self._Object__simbol = self._Animal__standart_simbol + "Di"
            return
        else:
            self.__growing()
            self.__safe_terrain = safe_terrain
            if self.__action_retreat == False and self._Animal__occupation == False and self.__die_status == False:
                self._Object__simbol = " " + self._Animal__standart_simbol + " "
            if self.__action_retreat:
                self._Object__coordinats = self._Object__coordinats_y + self._Object__coordinats_x
                self.__action_retreat = False
                return
            return super().behavior(animals, foods, terrain_animals, lis_obj)




