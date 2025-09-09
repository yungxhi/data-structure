class Node:
    def __init__(self, elem, next=None):   # 노드 생성자
        self.data = elem                   # 노드가 저장할 데이터 필드
        self.link = next                   # 다음 노드를 가리키는 링크 필드


class LinkedList:
    # 리스트의 데이터: 생성자에서 정의 및 초기화
    def __init__(self):
        self.head = None   # head: 시작 노드를 가리킴

    def isEmpty(self): 
        return self.head == None   # head가 None이면 공백 상태

    def isFull(self):
        return False   # 포화 상태가 될 수는 없음

    # pos 위치의 노드를 참조(반환): getNode(pos)
    # 시간 복잡도: O(n)
    def getNode(self, pos):
        if pos < 0: return None
        node = self.head
        # 시작 노드에서 pos번 링크를 따라 움직이면 pos 위치의 노드에 도착
        while pos > 0 and node != None:
            node = node.link
            pos -= 1
        return node

    # pos 위치의 요소(내용)를 참조: getEntry(pos)
    # 시간 복잡도: O(n)   ※ 배열 리스트의 경우: O(1)
    def getEntry(self, pos):
        node = self.getNode(pos)   # pos 위치의 노드를 먼저 구한 후
        if node == None: return None
        else: return node.data     # 그 노드의 데이터 필드를 반환

    # 삽입 연산: insert(pos, elem)
    # 시간 복잡도: O(n)
    def insert(self, pos, elem):
        before = self.getNode(pos-1)
        if before == None:   # 맨 앞에 삽입함
            self.head = Node(elem, self.head)
        else:
            node = Node(elem, before.link)
            before.link = node

    # 삭제 연산: delete(pos, elem)
    # 시간 복잡도: O(n)   / 만약 before를 알고 있다면? O(1)
    def delete(self, pos):
        before = self.getNode(pos-1)
        if before == None:   # 맨 앞 노드를 삭제
            if self.head != None:
                self.head = self.head.link
        elif before.link != None:
            before.link = before.link.link

    # 문자열 변환 연산자 중복 함수: __str__()
    def __str__(self):
        arr = []
        node = self.head
        while node is not None:
            arr.append(node.data)
            node = node.link
        return str(arr)


# 테스트 프로그램
if __name__ == "__main__":
    L = LinkedList()

    print("최초", L)
    L.insert(0, 10)
    L.insert(0, 20)
    L.insert(1, 30)
    L.insert(3, 40)
    L.insert(2, 50)

    print("삽입x5 ", L)
    print("연결리스트 3번째 값: ", L.getEntry(3-1))

    L.delete(2)
    print("삭제(2)", L)

    L.delete(3)
    print("삭제(3)", L)

    L.delete(0)
    print("삭제(0)", L)