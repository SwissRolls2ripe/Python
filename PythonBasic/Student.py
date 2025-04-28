# -*- coding: utf-8 -*-
class student:
	def __init__(self, name, student_id, yuwen_score, math_score, english_score):
		self.name = name
		self.student_id = student_id
		self.yuwen_score = yuwen_score
		self.math_score = math_score
		self.english_score = english_score

	def get_allscore(self):
		print(f"{self.name}的成绩如下： 语文成绩：{self.yuwen_score}，数学成绩：{self.math_score}，英语成绩：{self.english_score}。")
		return None

Philip = student("Philip", 1001, 90, 95, 85)
Philip.get_allscore()