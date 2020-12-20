#Stew work on procedural geneartion of tile map

from stew_work import *



dungeon = Dungeon(14)
room_size = 19 #this is the number of lines that make up a room, also num of character across a room



def gen_line(line_num, level):
    """Given a line_number of the current dungeon level returns the tile_map notation line
    at that line num as a string"""
    out_str = ''
    for room in level:
        if room:
            if line_num != 0 and line_num != room_size - 1 and line_num != room_size // 2 and line_num != (room_size // 2) + 1:
                out_str += '1' + ('.' * (room_size -2)) + '1'
            if line_num == 0:
                if room[4]:
                    out_str += '1' * (room_size // 2) + '..' + ('1' * (room_size - (room_size//2)-2))
                else:
                    out_str += '1' * room_size
            if line_num == (room_size -1):
                if room[6]:
                    out_str += '1' * (room_size // 2) + '..' + ('1' * (room_size - (room_size//2)-2))
                else:
                    out_str += '1' * room_size
            if line_num == (room_size // 2) or line_num == ((room_size // 2)+1):
                if room[7] == 'Room 1': #special case, put a bar in middle of room 1 so we can find it
                    if room[3]:
                        if room[5]:
                            out_str += '.' * (room_size - 10) + '111.......'
                        else:
                            out_str += '.' * (room_size -10) + '111......1'
                    elif room[5]:
                        out_str += '1........111.......'
                    else:
                        out_str += '1' + ('.' * (room_size-11)) + '111......1'
                else:
                    if room[3]:
                        if room[5]:
                            out_str += '.' * room_size
                        else:
                            out_str += '.' * (room_size-1) + '1'
                    elif room[5]:
                        out_str += '1' + ('.' * (room_size-1))
                    else:
                        out_str += '1' + ('.' * (room_size-2)) + '1'
        else:
            out_str += ' ' * room_size
    return out_str

file = open('dungeon.txt', 'w')
dung = dungeon.map[::-1]
for level in dung:
    write_line = False
    for check in level:
        if check:
            write_line = True
    if write_line:
        for line_num in range(room_size):
            file.write(gen_line(line_num, level))
            file.write("\n")

    #file.write()