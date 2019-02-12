#!/usr/bin/python
# -*- coding: utf-8 -*-


class DisjointSet:
	
	disjoint_set = list()
	edges = [[]]

	def __init__(self, init_arr):
		self.disjoint_set = []
		if init_arr:
			for element in list(set(init_arr)):
				self.disjoint_set.append([element])

	def isConnected (self):
		rows = len(self.edges)
		for row in range (rows):
			self.union (self.edges[row][0], self.edges[row][1])
		if self.size() == 1:
			print ("connected")
		else:
			print ("not connected, number of connected components is:")
			print (self.size())

	def storeEdges (self, edgeArray):
		self.edges = edgeArray
		print (self.edges)

	def find (self, element):
		for item in self.disjoint_set:
			if element in item:
				return self.disjoint_set.index(item)
		return None

	def union (self, x, y):
		x_set = self.find (x)
		y_set = self.find (y)
		if x_set != y_set and x_set is not None and y_set is not None:
			self.disjoint_set[y_set] = self.disjoint_set[x_set] + self.disjoint_set[y_set]
			del self.disjoint_set[x_set]
		return self.disjoint_set
		
	def get(self):
		return self.disjoint_set

	def size (self):
		return len(self.disjoint_set)
