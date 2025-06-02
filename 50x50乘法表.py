with open('50x50乘法表.csv', 'w') as f:
    for y in range(1, 51):
        for x in range(1, 51):
            f.write('{}*{}={},'.format(x, y, x*y))
            print('{}*{}={}\t'.format(x,y,x*y), end='')
        f.write('\n')
        print()
