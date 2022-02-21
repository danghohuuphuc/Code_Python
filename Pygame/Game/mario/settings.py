from turtle import title

level_map = [
'                            ',
'                            ',
'                            ',
'XX     XXX            XX    ',
'XX                          ',
'XXXX         XX          XX ',
'XXXX        XX              ',
'XX     X  XXXX    XX  XX    ',
'       X  XXXX    XX  XXX   ',
'    XXXX  XXXXXX  XX  XXXX  ',
'XXXXXXXX  XXXXXX  XX  XXXX  ']

title_size = 64
screen_width = 1200
screen_height = len(level_map) * title_size
print(screen_height)