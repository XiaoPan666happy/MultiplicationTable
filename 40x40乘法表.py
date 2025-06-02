with open('40x40乘法表.csv', 'w') as f:
    for y in range(1, 41):
        for x in range(1, 41):
            f.write('{}*{}={},'.format(x, y, x*y))
            print('{}*{}={}\t'.format(x,y,x*y), end='')
        f.write('\n')
        print()
