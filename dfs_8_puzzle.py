# !/usr/bin/env python
# -*- coding: utf-8 -*-


'''
@Author Amit Joshi
'''


# time taken => 16:32,25
import Queue
import copy

class puzzle:
	def __init__(self, initial, final):
		self.initial = initial
		self.final = final

	def main(self):
		# initial = [[8, 1, 3], [4, 0, 2], [7, 6, 5]] # [[0, 1, 3], [4, 2, 5], [7, 8, 6]]
		# final = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
		self.Q = Queue.LifoQueue()
		level = 0
		states = []
		# state = copy.deepcopy(self.initial)
		current_state = copy.deepcopy(self.initial)

		self.Q.put((current_state, level))
		
		print current_state

		# if current_state == self.final:
		# 	print "success"
		# 	return
		# else:
		# 	self.state_space(self.Q.get())
		

		while(not self.Q.empty()):
			pop_value = self.Q.get()
			current_state = copy.deepcopy(pop_value[0])
			level = pop_value[1]

			if current_state == self.final:
				print current_state, '=>', level
				print "success"
				return
			else:
				try:
					states.index(current_state)
					print current_state, '=>', level, "Already Visited"
					continue
				except:
					print current_state, '=>', level
					self.state_space(pop_value)
					states.append(current_state)

	def state_space(self, pop_value):
		for side in ['L', 'R', 'U', 'D']:
			state1 = self.move(pop_value, side)


	def move(self, pop_value, side):# side => movement direction of 0
		end = 0
		state = copy.deepcopy(pop_value[0])
		level = pop_value[1]
		for i in range(3):
			if end == 1: break
			for j in range(3):
				if state[i][j] == 0:
					if side == "L":
						if j == 0:
							pass
							# print state, side, "LIMIT ABOVE"
						else:
							try:
								state[i][j] = state[i][j-1]
								state[i][j-1] = 0
								end = 1
								self.Q.put((state, level+1))
								break
							except:
								pass
								# print state, side, "Invalid move"
					if side == "R":
						try:
							state[i][j] = state[i][j+1]
							state[i][j+1] = 0
							end = 1
							self.Q.put((state, level+1))
							break
						except:
							pass
							# print state, side, "Invalid move"					
					if side == "U":
						if i == 0:
							# print state, side, "LIMIT ABOVE"
							pass
						else:
							try:
								state[i][j] = state[i-1][j]
								state[i-1][j] = 0					
								end = 1
								self.Q.put((state, level+1))
								break
							except:
								pass
								# print state, side, "Invalid move"
					if side == "D":
						try:
							state[i][j] = state[i+1][j]
							state[i+1][j] = 0					
							end = 1
							self.Q.put((state, level+1))
							break
						except:
							pass
							# print state, side, "Invalid move"


		# return state

if __name__ == '__main__':
	puzzle_main = puzzle([[2, 8, 3], [1, 6, 4], [7, 0, 5]], [[1, 2, 4], [8, 0, 3], [7, 5, 6]]) #([[8, 3, 5], [4, 1, 6], [2, 7, 0]], [[1, 2, 3], [8, 0, 4], [7, 6, 5]])
	puzzle_main.main()
