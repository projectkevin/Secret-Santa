from random import *
import csv

def who_are_you(d):
	print(">>In who are you")
	human = raw_input("Who are you?")
	if human == d[]
	print d


def do_the_work(p):
	print(">>In do_the_work")
	pairs = open("pairings.csv", "w")
	shuffle(p)
	people.append(p[0])
	dict = {}
	for i in range(len(p) - 1):
		dict.update({p[i]:p[i+1]})
		#pairs.write(p[i] + "," + p[i + 1] + "\n")
	print(">>Check pairings.csv")
	who_are_you(dict)

text_file = open("humans.txt", "r")
people = text_file.read().split(',')
do_the_work(people)