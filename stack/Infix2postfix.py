from ArrayStack import ArrayStack
from EvalPostfix import evalPostfix

# 연산자의 우선순위 계싼 함수
def precedence (op):
  if (op == '(' or op == ')') : return 0
  elif (op == '+' or op == '-') : return 1
  elif (op == '*' or op == '/') : return 2
  else : return -1

# 중위 표기 수식의 후위식 변환
def Infix2Postfix(expr):
  s = ArrayStack(100)
  output = []

  for term in expr: 
    if term == '(':
      s.push(term)

    elif term == ')':
      while not s.isEmpty():
        op = s.pop()
        if op == '(':
          break
        else:
          output.append(op)

    elif term in "+-*/":
      while not s.isEmpty():
        op=s.peek()
        if (precedence(term)) <= precedence(op):
          output.append(op)
          s.pop()
        else:break
      s.push(term)
    else:
      output.append(term)
  while not s.isEmpty():
    output.append(s.pop())
  return output



# 테스트
if __name__ == "__main__":
    print('중위 표기식 후위 표기 변환₩n')

    infix1 = ['(', '6', '-', '3', ')', '*', '2', '+', '20', '/', '(', '10', '+', '5', ')']
    infix2 = ['1','/','2','*','4','*','(','1','/','4',')']

    postfix1 = Infix2Postfix(infix1)
    postfix2 = Infix2Postfix(infix2)

    result1 = evalPostfix(postfix1)
    result2 = evalPostfix(postfix2)

    print(' 중위표기:', infix1)
    print(' 후위표기', postfix1)
    print(' 게산결과:', result1)

    print(' 중위표기:', infix2)
    print(' 후위표기', postfix2)
    print(' 게산결과:', result2)