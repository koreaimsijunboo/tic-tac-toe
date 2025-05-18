if True:
    tt = turtle.Turtle()
    tt.hideturtle()
    S = turtle.Screen()
    S.register_shape("board.gif")
    board = turtle.Turtle()
    board.shape("board.gif")
    board.stamp()

    did = [None, None, None, None, None, None, None, None, None]

    shape = turtle.Turtle()
    shape.hideturtle()
    shape.pensize(10)

    win = False
    turn = "O"

    # 승리 체크 함수
    def check_win(player):
        win_conditions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8], # 가로
            [0, 3, 6], [1, 4, 7], [2, 5, 8], # 세로
            [0, 4, 8], [2, 4, 6]             # 대각선
        ]
        for idx, condition in enumerate(win_conditions):
            if all(did[i] == player for i in condition):
                return idx  # 이긴 조건 번호 리턴
        return None

    # 무승부 체크 함수
    def check_draw():
        return all(cell is not None for cell in did)

    # 승리한 줄에 선 긋는 함수
    def draw_line(idx):
        line = turtle.Turtle()
        line.hideturtle()
        line.pensize(15)
        line.color("red")
        line.speed(0)
        line.penup()

        if idx == 0:
            line.goto(-250, 166.67)
            line.pendown()
            line.goto(250, 166.67)
        elif idx == 1:
            line.goto(-250, 0)
            line.pendown()
            line.goto(250, 0)
        elif idx == 2:
            line.goto(-250, -166.67)
            line.pendown()
            line.goto(250, -166.67)
        elif idx == 3:
            line.goto(-166.67, 250)
            line.pendown()
            line.goto(-166.67, -250)
        elif idx == 4:
            line.goto(0, 250)
            line.pendown()
            line.goto(0, -250)
        elif idx == 5:
            line.goto(166.67, 250)
            line.pendown()
            line.goto(166.67, -250)
        elif idx == 6:
            line.goto(-250, 250)
            line.pendown()
            line.goto(250, -250)
        elif idx == 7:
            line.goto(250, 250)
            line.pendown()
            line.goto(-250, -250)

    # 보드 셀 좌표
    grid = [
        [(-166.67, 166.67), (0.00, 166.67), (166.67, 166.67)],
        [(-166.67, 0.00),   (0.00, 0.00),   (166.67, 0.00)],
        [(-166.67, -166.67), (0.00, -166.67), (166.67, -166.67)]
    ]

    # 게임 시작
    while not win:
        ip = turtle.textinput("Tic Tac Toe", f"{turn} 차례! 좌표 입력 (열,행)\n예: 0,2")
        if ip is None:
            break

        col, row = map(int, ip.split(","))
        if 0 <= row < 3 and 0 <= col < 3:
            x, y = grid[row][col]
            x_y = None
            shape.penup()
            shape.goto(x, y)
            shape.pendown()
            idx = 0
            for row_g in grid:
                for cell in row_g:
                    if (x, y) == cell:
                        x_y = idx
                    idx += 1

            if did[x_y] is None:
                # 빈 칸이면 그리기
                if turn == "O":
                    shape.color("white")
                    shape.penup()
                    shape.goto(x, y - 75)
                    shape.pendown()
                    shape.circle(75/2)
                    did[x_y] = "O"
                else:
                    shape.color("yellow")
                    size = 75/2
                    shape.penup()
                    shape.goto(x - size, y + size)
                    shape.pendown()
                    shape.goto(x + size, y - size)
                    shape.penup()
                    shape.goto(x - size, y - size)
                    shape.pendown()
                    shape.goto(x + size, y + size)
                    did[x_y] = "X"

                # 승리 체크
                win_idx = check_win(turn)
                if win_idx is not None:
                    print(f"🎉 {turn} 승리! 🎉")
                    draw_line(win_idx)
                    win = True
                # 무승부 체크
                elif check_draw():
                    print("😐 무승부입니다!")
                    win = True
                else:
                    turn = "X" if turn == "O" else "O"
            else:
                print("⚠️ 이미 선택된 칸입니다.")
    turtle.mainloop()
