from queue import Queue


def main():
    file = open('db.txt', 'r')
    struct = Queue()

    print(struct)
    print("-Задание 1-")
    print("Всего в очереди:", len(struct))
    tmp = Queue()
    min_elem = struct.dequeue()
    min_sum = min_elem[2]
    tmp.enqueue(min_elem)
    for i in range(len(struct)):
        elem = struct.dequeue()
        if elem[2] < min_sum:
            min_sum = elem[2]
            min_elem = elem
        tmp.enqueue(elem)
    print("Минимальная сумма:", min_sum)
    print("Элемент с минимальной суммой:", min_elem)
    new_elem = [1, 2, 3, 'New Element']
    for i in range(len(tmp)):
        elem = tmp.dequeue()
        struct.enqueue(elem)
        if elem == min_elem:
            struct.enqueue(new_elem)
    print("Новая очередь:", struct)
    print("-Задание 2-")
    tmp = Queue()
    cassier = input("Введите имя кассира: ")
    for i in range(len(struct)):
        elem = struct.dequeue()
        if elem[3] != cassier:
            tmp.enqueue(elem)
    print("Новая очередь:", tmp)
    print("-Задание 3-")
    file = open('db.txt', 'r')
    struct = Queue()
    tmp = []
    count = 0
    for line in file:
        count += 1
        if count == 1 or count == 3:
            tmp.append(int(line.strip()))
        elif count == 4:
            tmp.append(line.strip())
            struct.enqueue(tmp)
            tmp = []
            count = 0
        else:
            tmp.append(int(line.strip()))
    file.close()
    print("Очередь:", struct)
    tmp = Queue()
    date = int(input("Введите дату: "))
    for i in range(len(struct)):
        elem = struct.dequeue()
        if elem[1] == date:
            tmp.enqueue(elem)
    print("Новая очередь:", tmp)

if __name__ == '__main__':
    main()