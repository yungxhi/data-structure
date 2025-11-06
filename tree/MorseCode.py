# 이진트리를 위한 노드 클래스
class TNode:
    def __init__ (self, elem, left=None, right=None):
        self.data = elem 
        self.left = left
        self.right = right

# 모스 코드 표
table = [
    ('A', '.-'), ('B', '-...'), ('C', '-.-.'), ('D', '-..'),
    ('E', '.'), ('F', '..-.'), ('G', '--.'), ('H', '....'),
    ('I', '..'), ('J', '.---'), ('K', '-.-'), ('L', '.-..'),
    ('M', '--'), ('N', '-.'), ('O', '---'), ('P', '.--.'),
    ('Q', '--.-'), ('R', '.-.'), ('S', '...'), ('T', '-'),
    ('U', '..-'), ('V', '...-'), ('W', '.--'), ('X', '-..-'),
    ('Y', '-.--'), ('Z', '--..')
]

# 인코딩 알고리즘
def encode(ch):
    idx = ord(ch) - ord('A')
    return table[idx][1]

# 디코딩 알고리즘
def decode(root, code):
    node = root 
    for c in code:
        if c == '.':
            node = node.left
        elif c == '-':
            node = node.right
    return node.data

# 모스 코드 결정 트리 만들기
def make_morse_tree():
    root = TNode(None)
    for tp in table:
        code = tp[1]
        node = root
        for c in code:
            if c == '.':
                if node.left is None:
                    node.left = TNode(None)
                node = node.left
            elif c == '-':
                if node.right is None:
                    node.right = TNode(None)
                node = node.right
        node.data = tp[0]
    return root

# 테스트 프로그램
if __name__ == "__main__":
    morseCodeTree = make_morse_tree()
    s = input("입력 문장 (A~Z만): ").upper()
    mlist = []

    for ch in s:
        code = encode(ch)
        mlist.append(code)
    print("Morse Code:", mlist)

    print("Decoding  :", end=' ')
    for code in mlist:
        ch = decode(morseCodeTree, code)
        print(ch, end='')
    print()
