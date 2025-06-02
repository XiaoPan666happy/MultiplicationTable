with open('30x30乘法表.csv', 'w') as f:
    for y in range(1, 31):
        for x in range(1, 31):
            f.write('{}*{}={},'.format(x, y, x*y))
            print('{}*{}={}\t'.format(x,y,x*y), end='')
        f.write('\n')
        print()
