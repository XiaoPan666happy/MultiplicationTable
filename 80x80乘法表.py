with open('80x80乘法表.csv', 'w') as f:
    for y in range(1, 81):
        for x in range(1, 81):
            f.write('{}*{}={},'.format(x, y, x*y))
            print('{}*{}={}\t'.format(x,y,x*y), end='')
        f.write('\n')
        print()
