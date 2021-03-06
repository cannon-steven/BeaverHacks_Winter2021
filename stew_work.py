# Author:Stew
# Date: 12/16/2020
# Description: This is where I am writing stuff so I don't mess up main

import random as rand

rand.seed()


class Character():
    """This is the class that defines player characters"""

    def __init__(self, hp=10, atk=1, lvl=1, exp=0):
        """this initializes the player character"""
        self.hp = hp
        self.atk = atk
        self.max_hp = hp
        self.lvl = lvl
        self.exp = exp

    def take_dmg(self, dmg):
        """takes an int amount of damage dealt to character, can take negative number for
        gaining health
        """
        self.hp -= dmg

    def gain_exp(self, amt):
        """gains the amount of experience inputted, if it goes over 10 times the level then levels up
        and resets exp appropriately"""
        self.exp += amt
        if self.exp >= (self.lvl * 10):
            self.lvl_up()

    def lvl_up(self):
        """levels up, assumes that experience is greater than or equal to 10 times level"""
        if self.exp < 10 * self.lvl:
            return
        self.exp -= 10*(self.lvl)
        self.lvl += 1

    def get_hp(self):
        """returns the current amount of health"""
        return self.hp

    def get_max_hp(self):
        """returns the max health of character"""
        return self.max_hp

    def get_atk_dmg(self):
        """returns the amount of damage character does when it gets correct answer"""
        return self.atk

class Dungeon():
    """class that stores the dungeon"""
    #contains list of 'rooms' which are themselves a list containing the encounter in that room
    #as well as a list of where there are doors in the room and the name of the room
    #Dungeon map is imagined to be marked in rows and collumns, with row 0 being the bottom row
    #and collum 0 being the left collum

    def __init__(self, num_rooms, depth=8):
        """initializes empty dungeon"""
        self.depth = depth #distance to boss room
        self.map = self._make_board()
        # print(self.map)
        self.start_room = (0,0)
        self.make_rooms(num_rooms)
        # for num in range(1, self.depth+1):
        #     print(self.map[-num])

    def _make_board(self):
        """returns an A by A size list where A is the size of the game board
         and every value is the input value given
         """
        return [[False for num_col in range(self.depth)] for num_row in range(self.depth)]

    def get_start_room(self):
        """Returns location of starting room"""
        return self.start_room

    #Notation for rooms in grid [bool-is-encounter-active,row,col,left,up,right,down0/1, room-name
    def make_rooms(self, num_rooms):
        """Generates a dungeon full of rooms, takes the number of rooms to generate"""
        pick_num = rand.randint(0,self.depth-1)
        self.start_room = (0,pick_num)
        row = 0
        col = 0
        counter = 0
        previous_room_dir = False
        while counter < self.depth:
            if counter < self.depth - 1:
                self.map[row][col] = [True, row, col,0,0,0,0,("Room " + str(counter+1))]
                if previous_room_dir:
                    self.map[row][col][((previous_room_dir +1)%4)+3] = 1
                else:
                    self.start_room = (row,col)
            else:
                self.map[row][col] = [True, row, col,0,0,0,0,"Boss Room"]
                self.map[row][col][((previous_room_dir +1)%4)+3] = 1
                break
            way = rand.randint(1,3)
            if way == 1:
                if previous_room_dir and (previous_room_dir + way) != 4 and col-1 >= 0:
                    self.map[row][col][way + 2] = 1
                    counter += 1
                    previous_room_dir = way
                    col -= 1
                else:
                    way = rand.randint(2,3)
            if way == 3:
                if previous_room_dir and (previous_room_dir + way) != 4 and col + 1 < self.depth:
                    self.map[row][col][way + 2] = 1
                    counter +=1
                    previous_room_dir = way
                    col += 1
                else:
                    way = 2
            if way == 2:
                self.map[row][col][way + 2] = 1
                counter +=1
                previous_room_dir=way
                row +=1
        self.add_rooms((num_rooms-self.depth))

    def add_rooms(self, num_rooms):
        """randomly adds rooms adjacent to existing rooms until it has added enough"""
        counter = 0
        while counter < num_rooms:
            pick_level = rand.randint(0,self.depth-1)
            for room in self.map[pick_level]:
                if room and rand.randint(0,1):
                    if self.add_adj_room(room, counter):
                        counter += 1
                        break

    def add_adj_room(self, room, counter):
        """adds a room adjacent to the room passed if it can, returns True if it can
        returns False if it can't"""
        if room[7] == 'Boss Room': #Stops the building of rooms adjacent to boss room
            return False
        row = room[1]
        col = room[2]
        list_poss_rooms = []
        if col-1 >= 0 and not self.map[row][col-1]:
            list_poss_rooms.append(1)
        if row+1 < self.depth and not self.map[row+1][col]:
            list_poss_rooms.append(2)
        if col+1 < self.depth and not self.map[row][col+1]:
            list_poss_rooms.append(3)
        if row-1 >= 0 and not self.map[row-1][col]:
            list_poss_rooms.append(4)
        if len(list_poss_rooms) == 0:
            # print("cant build from here", row, col)
            return False
        else:
            pick_dir = rand.randint(0,(len(list_poss_rooms)-1))
            direction = list_poss_rooms[pick_dir]
            room[direction+2] = 1
            if direction % 2 == 0:
                row = row - (direction-3)
                # print("building",row,col)
                self.map[row][col] = [True, row, col,0,0,0,0,("Room " + str(self.depth + counter))]
                self.map[row][col][((direction+1)%4)+3] = 1
                return True
            else:
                col = col + (direction - 2)
                # print('buildin',row,col)
                self.map[row][col] = [True, row, col,0,0,0,0,("Room " + str(self.depth + counter))]
                self.map[row][col][((direction+1)%4)+3] = 1
                return True
        print("this shouldnt print")
        return False








