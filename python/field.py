from tile import Tile
from palette import Palette
from json import dumps
from json import loads

class Field:
	def __init__(self, x, y, char=None):
		self.sequence = []
		self.x=x
		self.y=y
		self.default_char = char
		self.change_buffer = list()
	def build_layer(self, char=None):
		matrix=[]
		for i in range(0, self.x):
			matrix.append([])
			for j in range(0, self.y):
				matrix[len(matrix)-1].append(Tile(char=char, rgba=Palette[char]))
		return matrix
    def unite(self, layers:list):
        united_layers = self.__from_None_to_space(layers[0])
        for index_x, x in enumerate(self.sequence):
            # print("x: ", x, end=" ") #
            for index_y, y in enumerate(x):
                # print("y: ", y, end=" ") #
                for tile in enumerate(y):
                    match tile[1].char:
                        case "\n":
                            continue
                        case None:
                            continue
                        case _ :
                            united_layers[index_y][tile[0]].char = tile[1].char
        return united_layers
	def sequence_to_json(self, layer):
	    ...
	#  ____    _____   []
	# |  _ \  |    \   __
	# | |_| | | || /  | |
	# |  __/  |   \   | |
	# | |     | |\ \  | |
	# |_|     |_| \_\ |_|
	def print(self, separate=""):
	    sequence_to_print = self.unite(self.sequence)
		for y in range(self.y):
			for x in range(self.x):
				print(sequence_to_print[x][y].char + separate, end="")
			print()
	def __from_None_to_space(self, layer):
	    for y in enumerate(layer):
	        for tile in enumerate(y[1]):
	            if tile[1].char == None:
	                layer[y[0]][tile[0]].char = " "
	    return layer
	def rect(self, begin:list, end:list, char="#"):
		layer = self.build_layer(char=self.default_char)
		if end[0] < begin[0]:
			end[0], begin[0] = begin[0], end[0]
		if end[1] < begin[1]:
			end[1], begin[1] = begin[1], end[1]
		for x in range(begin[0], end[0]):
			for y in range(begin[1], end[1]):
				# print("x:", x, " y:", y) #
				layer[x][y].char = char
		return layer
	#	 _        _    _    _    ______
	#	| |      | |  | \_ | |  |  ____|
	#	| |      | |  | |\\| |  | |----,
	#	| |____  | |  | | \\ |  | |----'
	#	|_____|  |_|  |_|  \_|  |______|
	def line(self, begin, end, char="#"):
		layer = self.build_layer(char=self.default_char)
		def build_by_y():
			print("Build by y")
			points = []
			koef_x = 0
			cycle_begin = begin[1]
			cycle_end = end[1] + 1
			begin_x = begin[0]
			if end[0] < begin[0]:
				koef_x = -1
			else:
				koef_x = 1
			if begin[1] > end[1]:
				cycle_begin = end[1]
				cycle_end = begin[1] + 1
				begin_x = end[0]
				koef_x = -koef_x
			corner_koef = abs(end[0]-begin[0])/abs(end[1]-begin[1])
			error = 0
			x = begin_x
			for y in range(cycle_begin, cycle_end):
				if error >= 0.5:
					x += koef_x
					error -= 1
				points.append((x, y))
				print("x: ", x, " y: ", y, " e: ", error, " ck: ", corner_koef)
				error += corner_koef
			for coors in points:
				layer[coors[0]][coors[1]].char = char
		def build_by_x():
			print("Build by x")
			points = []
			koef_y = 0
			cycle_begin = begin[0]
			cycle_end = end[0] + 1
			begin_y = begin[1]
			if end[1] < begin[1]:
				koef_y = -1
			else:
				koef_y = 1
			if begin[0] > end[0]:
				cycle_begin = end[0]
				cycle_end = begin[0] + 1
				begin_y = end[1]
				koef_y = -koef_y
			corner_koef = abs((end[1]-begin[1])/(end[0]-begin[0]))
			error = 0
			y = begin_y
			for x in range(cycle_begin, cycle_end):
				if error >= 0.5:
					y += koef_y
					error -= 1
				points.append((x, y))
				print("x: ", x, " y: ", y, " e: ", error, " ck: ", corner_koef)
				error += corner_koef
			for coors in points:
				layer[coors[0]][coors[1]].char = char
		if abs(begin[0]-end[0]) >= abs(begin[1]-end[1]):
			build_by_x()
		else:
			build_by_y()
		return layer
