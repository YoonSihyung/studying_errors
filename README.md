# studying_errors
공부하면서 겪었던 실수들을 모아놓았다.

BJ 1920
- 21번 줄에서 find = find[n//2+1:]을 해야 find가 새로운 리스트로 업데이트 되면서 이진탐색을 할 수 있는데 find = find[n//2+1]로 오타를 냈다. TypeError: object of type 'int' has no len()
- 9번 줄 반복을 진행할 때 이진 탐색에서 n을 사용하여 새로운 수를 탐색할 때 n이 초기화 되지 않았다. l = n을 사용하여 l을 계속 초기화 해야 한다.
- 이진 탐색에서 계속 찾지 못해서 리스트가 두 개로 줄어들었을 때 두 개 다 확인하지 않고 loop가 종료되게 했다.
- 이진 탐색은 직접 리스트를 변형시키는 것이 아니라 left, right, mid를 이용해 찾는 것이다.
- 이진 탐색 loop 종료 조건은 left <= right가 깨질 때.
