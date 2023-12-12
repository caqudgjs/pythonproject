# 링크드 리스트 노드
class Node:
    def __init__(self, elem, next=None):
        self.data = elem
        self.link = next

# 연결 큐 클래스
class ConnectedQueue:
    def __init__(self):
        self.front = None  # 큐의 전단
        self.rear = None   # 큐의 후단

    def is_empty(self):
        return self.front is None

    def enqueue(self, elem):
        new_node = Node(elem)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            self.rear.link = new_node
            self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            print("큐가 비어 있습니다. 디큐할 수 없습니다.")
            return None

        data = self.front.data
        self.front = self.front.link

        # 디큐 후 front가 None이 되면 rear도 None으로 설정
        if self.front is None:
            self.rear = None

        return data

    def size(self):
        count = 0
        node = self.front
        while node is not None:
            count += 1
            node = node.link
        return count

    def __str__(self):
        arr = []
        node = self.front
        while node is not None:
            arr.append(node.data)
            node = node.link
        return str(arr)

# 큐 인스턴스 생성
queue = ConnectedQueue()

# 큐가 비어 있는지 확인
print(queue.is_empty())  # True

# 큐에 원소 추가
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

# 큐의 내용 출력
print(queue.__str__())  # [1, 2, 3]

# 큐에서 원소 제거
print(queue.dequeue())  # 1
print(queue.dequeue())  # 2

# 큐의 내용 출력
print(queue.__str__())  # [3]

# 큐의 크기 출력
print(queue.size())  # 1

# 큐가 비어 있는지 확인
print(queue.is_empty())  # False