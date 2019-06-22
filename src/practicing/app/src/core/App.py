#!/usr/bin/python3
#-*- coding: utf-8 -*-

class App():

	app = {}

	def load(self, alia, library):

		self.app[alia] = library

	def run(self):

		print("Inicialice")

	def show(self):

		print(self.app["menu"].items())
		