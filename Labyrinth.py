import random

print("ИГРА ЛАБИРИНТ ТЕНЕЙ")
print("ты странник, очнулся в подземном лабиринте древних.")
print("где-то в глубине спит портал, ведущий домой.")
print("чтобы открыть его, нужен ключ древних.")
print("найди ключ. не умри. вернись домой.")

empty = "пустая"
chest = "сундук"
monster = "монстр"
trap = "ловушка"
key = "ключ"
portal = "портал"

symbols = {}
symbols[empty] = "."
symbols[chest] = "c"
symbols[monster] = "m"
symbols[trap] = "t"
symbols[key] = "k"
symbols[portal] = "p"


def createmaze(n):
    maze = []
    for r in range(n):
        row = []
        for c in range(n):
            row.append(empty)
        maze.append(row)

    positions = []
    for r in range(n):
        for c in range(n):
            positions.append((r, c))

    def place(roomtype, count):
        placed = 0
        while placed < count:
            r, c = random.choice(positions)
            if maze[r][c] == empty:
                maze[r][c] = roomtype
                placed += 1

    place(chest, max(2, n))
    place(monster, max(1, n // 2))
    place(trap, max(2, n))
    place(key, 1)
    place(portal, 1)
    return maze


def createseen(n):
    seen = []
    for r in range(n):
        row = []
        for c in range(n):
            row.append(False)
        seen.append(row)
    return seen


def showmap(maze, seen, px, py):
    n = len(maze)
    header = "    "
    for c in range(n):
        header = header + str(c) + " "
    print(header)
    
    for r in range(n):
        line = "  " + str(r) + " "
        for c in range(n):
            if px == r and py == c:
                line = line + "@ "
            elif seen[r][c]:
                line = line + symbols[maze[r][c]] + " "
            else:
                line = line + "? "
        print(line)
        
    print("легенда: @ ты  . пустая  c сундук  m монстр  t ловушка  k ключ  p портал  ? неизвестно")


def pickup(inventory, items):
    if isinstance(items, list):
        inventory.extend(items)
    else:
        inventory.append(items)
    return inventory


def drop(inventory, itemname):
    if itemname in inventory:
        inventory.remove(itemname)
    elif inventory:
        dropped = inventory.pop()
        print(f"предмета '{itemname}' нет. выброшен последний: {dropped}")
    return inventory


def sortinventory(inventory):
    inventory.sort()
    inventory.reverse()
    print("инвентарь отсортирован по убыванию.")
    return inventory


def finditem(inventory, itemname):
    if itemname in inventory:
        idx = inventory.index(itemname)
        print(f"найдено '{itemname}' на позиции {idx}.")
        return True
    print(f"предмет '{itemname}' не найден.")
    return False


def copyinventory(inventory):
    backup = inventory.copy()
    firsttwo = inventory[:2]
    print(f"копия инвентаря: {backup}")
    print(f"первые два предмета: {firsttwo}")
    return backup


def asksize():
    while True:
        try:
            n = int(input("введи размер лабиринта n (n x n, от 3 до 10): "))
        except ValueError:
            print("нужно целое число. попробуй снова.")
            continue
        if n < 3:
            print("слишком маленький лабиринт. минимум 3.")
            continue
        if n > 10:
            print("слишком большой. максимум 10.")
            continue
        return n


def gameloop():
    print("=" * 40)
    print("лабиринт теней")
    print("=" * 40)
    print("ты очнулся в подземелье древних. найди ключ и портал,")
    print("чтобы вернуться домой. берегись монстров и ловушек!\n")

    n = asksize()

    maze = createmaze(n)
    seen = createseen(n)

    px = 0
    py = 0
    maze[px][py] = empty
    seen[px][py] = True

    hp = 100
    inventory = []
    step = 0

    totalrooms = 0
    for r in range(n):
        for c in range(n):
            totalrooms += 1
            
    print(f"размер лабиринта: {n}x{n}, всего комнат: {totalrooms}\n")
    showmap(maze, seen, px, py)

    while True:
        step += 1
        print(f"\n--- ход {step} | позиция ({px},{py}) | hp: {hp} ---")
        print("команды: w/a/s/d - идти, inv - инвентарь, "
              "drop <имя> - выбросить, sort - сортировать, "
              "find <имя> - найти, copy - копия, quit - выход")

        cmd = input("> ").strip().lower()

        if cmd == "quit":
            print("ты покидаешь лабиринт... но это не конец истории.")
            break

        if cmd == "inv":
            print(f"инвентарь: {inventory}")
            continue
        if cmd.startswith("drop "):
            drop(inventory, cmd[5:])
            continue
        if cmd == "sort":
            sortinventory(inventory)
            continue
        if cmd.startswith("find "):
            finditem(inventory, cmd[5:])
            continue
        if cmd == "copy":
            copyinventory(inventory)
            continue

        dx = 0
        dy = 0
        if cmd == "w":
            dx = -1
        elif cmd == "s":
            dx = 1
        elif cmd == "a":
            dy = -1
        elif cmd == "d":
            dy = 1
        else:
            print("неизвестная команда.")
            continue

        nx = px + dx
        ny = py + dy
        if not (0 <= nx < n and 0 <= ny < n):
            print("стена! туда нельзя.")
            continue

        px = nx
        py = ny
        seen[px][py] = True
        room = maze[px][py]
        print(f"ты вошёл в комнату: {room}")

        won = False
        if room == empty:
            print("пустая комната. тишина...")
        elif room == chest:
            lootoptions = []
            lootoptions.append(["зелье", "монета"])
            lootoptions.append(["меч", "монета", "зелье"])
            lootoptions.append(["карта"])
            lootoptions.append(["зелье"])
            loot = random.choice(lootoptions)
            print(f"ты открыл сундук и нашёл: {loot}")
            pickup(inventory, loot)
            maze[px][py] = empty
        elif room == monster:
            print("на тебя напал монстр!")
            if "меч" in inventory:
                print("ты сразил монстра мечом!")
            else:
                hp -= 25
                print(f"получено 25 урона. hp: {hp}")
            maze[px][py] = empty
        elif room == trap:
            print("ловушка! шипы ранят тебя.")
            hp -= 15
            print(f"получено 15 урона. hp: {hp}")
            maze[px][py] = empty
        elif room == key:
            print("ты нашёл ключ древних!")
            pickup(inventory, "ключ древних")
            maze[px][py] = empty
        elif room == portal:
            if "ключ древних" in inventory:
                print("\nпортал открывается! ты возвращаешься домой. победа!")
                won = True
            else:
                print("портал закрыт. нужен ключ древних.")

        if hp <= 0:
            print("\nты погиб в лабиринте... история обрывается.")
            break

        if won == True:
            break

        showmap(maze, seen, px, py)


if __name__ == "__main__":
    gameloop()
