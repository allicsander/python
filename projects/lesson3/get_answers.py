answers = {"привет": "И тебе привет!" ,"как дела": "Лучше всех" ,"пока": "Увидимся"}

def get_answer(question, answers):
  return answers.get(question).lower()


print(get_answer("привет", answers))  