pupils_scores = [
  {'school_class':'4a', 'scores':[5,3,4,3,4]},
  {'school_class':'4b', 'scores':[4,3,5,5,5]},
  {'school_class':'4c', 'scores':[5,5,5,5,5]},
  {'school_class':'4d', 'scores':[4,5,5,5,5]}
]

sum_all, count_all, tmp_sum, sum_class = 0, 0, 0, 0


for my_class in pupils_scores:
	for scores in my_class['scores']:
		sum_all += scores
		count_all += 1
	sum_class = sum_all - tmp_sum
	print('Средняя оценка в классе({0}): {1}'.format(my_class['school_class'], sum_class / len(my_class['scores'])))
	tmp_sum += sum_class

print('Средняя оценка по школе: {0}'.format(sum_all / count_all))