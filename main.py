class MyList():
    def __init__(self):
        self.capacity = 2# myList의 용량 (저장할 수 있는 원소 개수)
        self.n = 0# myList의 현재 가지고있는 원소의 개수
        self.A = [None]*self.capacity# myList의 실제 저장공간
        
    def append(self,a):
        if(self.capacity == self.n):
            self.change_size(self.capacity * 2)
        self.A[self.n] = a
        self.n = self.n + 1
        
    # 더 이상 빈 칸이 없을땐 capacity 2배로 doubling
    # 맨 뒤에 삽입
    # n 값 1 증가
    def pop(self, a=-1):
        x = self.A[a]
        for i in range( a+1 ,self.n):
            self.A[i-1] = self.A[i]
            self.A[i] = None
        self.n = self.n - 1
        return(x)
    # 1. k 값이 주어진 경우와 주어지지 않은 경우 구별해야 함
      # 2. x = self.A[k] (없앨 타겟 지정)
      # 3. A[k]의 오른쪽의 값들이 한 칸씩 왼쪽으로 이동해 메꿈
      # 4. self.n -= 1
      # 5. return x 
    def insert(self,a,b):
        if(self.a > len(self.capacity)):
            print(raise IndexError)
        if(self.n == self.capacity):
            self.change_size(self.capacity * 2)
     # 주의: k 값이 음수값일 수도 있음
      # k 값이 올바른 인덱스 범위를 벗어나면, raise IndexError
      # 1. k의 범위가 올바르지 않으면 IndexError 발생시킴
      # 2. self.n == self.capacity이면 self.change_size(self.capacity*2) 호출해 doubling
      # 3. A[k]와 오른쪽 값을 한 칸씩 오른쪽으로 이동
      # 4. self.A[k] = x
      # 5. self.n += 1
    def size(self):
        return(self.capacity)
    def change_size(self, new_capacity):
        b =[None] * new_capacity # 1. new_capacity의 크기의 리스트 B를 만듬
        for i in range(self.n):# 2. self.A의 값을 B로 옮김
            b[i] = self.A[i]
        del self.A# 3. del self.A  (A 지움)
        self.A = b
        self.capacity = new_capacity
      # 1. new_capacity의 크기의 리스트 B를 만듬
      # 2. self.A의 값을 B로 옮김
      # 3. del self.A  (A 지움)
      # 4. self.A = B
      # 5. self.capacity = new_capacity

L = MyList()
while True:
    cmd = input().strip().split()
    if cmd[0] == 'append':
        L.append(int(cmd[1]))
        print(f"  + {cmd[1]} is appended.")
    elif cmd[0] == 'pop':
        if len(cmd) == 1:
            idx = -1
        else:
            idx = int(cmd[1])
        try:
            x = L.pop(idx)
            print(f"  - {x} at {idx} is popped.")
        except IndexError:
            if len(L) == 0:
                print("  ! list is empty.")
            else:
                print(f"  ! {idx} is an invalid index.")
    elif cmd[0] == 'insert':
        try:
            L.insert(int(cmd[1]), int(cmd[2]))
            print(f"  + {cmd[2]} is inserted at index {cmd[1]}.")
        except IndexError:
            print(f"  ! {cmd[1]} is an invalid index.")
    elif cmd[0] == 'get': # getitem A[k]
        try:
            L[int(cmd[1])]
            print(f"  @ L[{cmd[1]}] --> {L[int(cmd[1])]}.")
        except IndexError:
            print(f"  ! {cmd[1]} is an invalid index.")
    elif cmd[0] == 'set': # setitem A[k] = x
        try:
            L[(int(cmd[1]))] = int(cmd[2])
            print(f"  ^ L[{cmd[1]}] <-- {cmd[2]}.")
        except IndexError:
            print(f"  ! {cmd[1]} is an invalid index.")
    elif cmd[0] == 'size':
        print("  ? capacity =", L.size())
    elif cmd[0] == 'print':
        print(L)
    elif cmd[0] == 'exit':
        print('bye~')
        break
    else:
        print(" ? invalid command! Try again.")

    
