def core_game(red_code, blue_code, state=None):    
	# Imports & Init
	import random
	import json
	#from pygame import draw, display, Rect, event, QUIT, Color, time, Surface, font
	from node_vm2 import VM
	#pygame.init()
	#pygame.font.init()

	# URL Specific Setup
	turn_code = dict()
	turn_code["red"]= red_code 
	turn_code["blue"] = blue_code 

	# Globals
	#FONT = font.SysFont("Arial", 24)
	SQUARE_WID = 75
	BOARD_WID = 10
	#WHITE = Color(255, 255, 255)
	#BLACK = Color(0, 0, 0)
	#RED = Color(200, 0, 0)
	#BLUE = Color(0, 0, 200)
	player_dict = dict()
	#col_dict = {"blue": BLUE, "red": RED, "white": WHITE}
	dir_to_delta = { "U":(0, -1), "D":(0, 1), "L":(-1,0), "R": (1,0)}
	preload_code = open("preload.js").read()

	# Utils
	def valid_sq(x, y):
		return x > -1 and x < BOARD_WID and y > -1 and y < BOARD_WID

	def copy_2D(mat):
		return [[i for i in row] for row in mat]

	def copy_3D(mat):
		return[copy_2D(i) for i in mat]

	def r_ind():
		return random.randint(0,BOARD_WID-1)


	# Player Class
	class Player:
		def __init__(self, color):
			self.color = color
			player_dict[color] = self

		def turn(self, mat, strength, x, y):
			ref = {"mat":copy_2D(mat), "x":x, "y":y}
			try:
				with VM() as vm:
					turn_call = "turn({}, {}, {}, {}, {})".format(" '{}' ".format(self.color), json.dumps(mat), strength, x, y)
					call_str = "{} {} {}".format(preload_code, turn_code[self.color], turn_call)
					action = vm.run(call_str)
					if type(action) == list:
						return tuple(action)
			except:
				print("Error: {}".format(self.color))

	# Core Functions
	def execute(move, mat, x, y, col):
		move_id = move[0]
		move_info = move[1:]

		if move_id == "move":
			direction = move_info[0]
			dx, dy = dir_to_delta[direction]
			num = int(move_info[1])
			if valid_sq(x+dx, y+dy):
				sq, to_sq = mat[x][y], mat[x+dx][y+dy]
				to_col = to_sq[0]
				units = min(sq[1], num)
				if to_col in (col, "white"):
					sq[1] -= units
					to_sq[0] = col
					to_sq[1] += units

		elif move_id == "attack":
			direction = move_info[0]
			dx, dy = dir_to_delta[direction]
			num = int(move_info[1])
			if valid_sq(x+dx, y+dy):
				sq, to_sq = mat[x][y], mat[x+dx][y+dy]
				to_col = to_sq[0]
				units = min(sq[1], num)
				if to_col not in (col, "white"):
					if sq[1] - units < 2:
						return
					enemy_units = to_sq[1]
					del_units = units - enemy_units
					sq[1] -= units + 1
					if del_units == 0:
						to_sq[0], to_sq[1] = "white", 0
					elif del_units > 0:
						to_sq[0], to_sq[1] = col, del_units
					else:
						to_sq[1] -= units

		elif move_id == "heal":
			mat[x][y][1] += 1

	def setup():
		Player("blue")
		Player("red")
		col_mat = [[["white", 0] for i in range(BOARD_WID)] for j in range(BOARD_WID)]
		col_mat[r_ind()][r_ind()] = ["blue", 299]
		col_mat[r_ind()][r_ind()] = ["red", 299]
		return  col_mat

	def main():
		col_mat = setup()
		#screen = display.set_mode((750, 750))
		#clock = pygame.time.Clock()
		counter = 0
		while counter < 10:
			#for ev in event.get():
			#	if ev.type == QUIT:
			#		break
			#screen.fill((0, 0, 0))
			next_mat = copy_2D(col_mat)
			for i, row in enumerate(col_mat):
				for j, tup in enumerate(row):
					if "white" not in tup:
						col, strength = tup
						move = player_dict[col].turn(copy_2D(next_mat), strength, i, j)
						if move:
							execute(move, next_mat, i, j, col)

			col_mat = next_mat
			if state != None:
				state.append(copy_3D(col_mat))
			counter += 1
			print(counter)
			#clock.tick(500)

	main()
	print("finished")
	return state


def local_test():
	red_code = open("turn_red.js", "r").read()
	blue_code = open("turn_red.js", "r").read()
	core_game(red_code, blue_code)

#local_test()








