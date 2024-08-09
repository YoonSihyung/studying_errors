# studying_errors
공부하면서 겪었던 실수들을 모아놓았다.

BJ1920-error1.py
- 21번 줄에서 find = find[n//2+1:]을 해야 find가 새로운 리스트로 업데이트 되면서 이진탐색을 할 수 있는데 find = find[n//2+1]로 오타를 냈다.
- TypeError: object of type 'int' has no len()

