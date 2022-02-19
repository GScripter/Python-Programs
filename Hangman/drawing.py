def desenho(num):
    if num == 0:
        print('''
            + ---+
            |    |
            |
            |
            |''')
    elif num == 1:
        print('''
        + ---+
        |    |
        |    0
        |
        |''')
    elif num == 2:
        print('''
        + ---+
        |    |
        |    0
        |    |
        |''')
    elif num == 3:
        print('''
        + ---+
        |    |
        |    0
        |    |
        |   / \	''')
    elif num == 4:
        print(f'''
        + ---+
        |    |
        |    0        \033[31mVocê Perdeu!\033[m
        |  --|--
        |   / \	''')
