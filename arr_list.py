# 리스트의 데이터: 전역 변수
capacity = 100
# 리스트 용량: 예) 용량을 100으로 지정
array =[None]*capacity #요소 배열: [None, .., None] (길이가 capacity)
size = 0 # 리스트 항목들의 개수: 공백상태(0)로 초기화 함


# ------------- 공백 상태 검사 isEmpty() --------------
def isEmpty( ) : 
  if size == 0 : return True  # 공백이면 True 반환 # 아니면 False 반환
  else : return False # 아니면 False 반환


# ------------- 포화 상태 검사 isFull() --------------
def isFull( ) : # size가 capacity이면 포화상태 비교연산 size == capacity 결과를 바로 반환
  return size == capacity


# ------------- 삽입 연산 insert() --------------
def insert( pos, e ) :
  global size # size는 전역변수
  if not isFull() and 0 <= pos <= size : # 포화 상태가 아니고 pos가 유효한 위치이면
    for i in range(size, pos,-1): # pos부터 size-1까지의 모든 항목을 한 칸씩 뒤로 옮김
      array[I] = array[i-1]
    array[pos] = e # pos위치에 새로운 요소 추가
    size += 1 # 요소의 수 size가 하나 증가
  else : 
    print("리스트 overflow 또는 유효하지 않은 삽입 위치")
    exit()


# ------------- 삭제 연산 delete() --------------
def delete( pos ) :
  global size # size는 전역변수
  if not isEmpty() and 0 <= pos < size : # 공백 상태가 아니고 pos가 유효한 위치이면
    e = array[pos] # array[pos]의 복사본 e를 저장해 두고
    for i in range(pos, size-1) : # pos+1부터 size-1까지의 모든 항목을 한 칸씩 앞으로 옮김
      array[i] = array[i+1]
    size -= 1 # 요소의 수 size를 하나 감소
    return e # e 반환
  else :
    print("리스트 underflow 또는 유효하지 않은 삭제 위치")
    exit()


# ------------- pos 위치의 항목을 참조 getEntry(pos) --------------
def getEntry(pos) :
  if O<=pos< size: # pos가 유효한 위치(0~size-1)이면 arraylpos] 반환
    return array(pos)
  else : return None
# 그렇지 않으면 None 반환


# ------------- 더 해야됨 --------------