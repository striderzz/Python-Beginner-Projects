quiz ={
  "question1":{
    "question":"What is the capital of france?","answer":"paris"
  },
   "question2":{
    "question":"What is the capital of germany?","answer":"berlin"
  },
   "question3":{
    "question":"What is the capital of uk?","answer":"london"
  },
   "question4":{
    "question":"What is the capital of italy?","answer":"rome"
  }
}
score = 0
for key,value in quiz.items():
  print(key +" - "+ value['question'])
  answer = input()

  if answer.lower() == value['answer']:
    score = score + 1
  else:
    print("Wrong answer")
    print(f'The correct answer was {value["answer"]}\n')  

print(f'Your score is {score}/{len(quiz.items())} !!!')
print(f'You got {(score/len(quiz.items()))*100} % right')
  
