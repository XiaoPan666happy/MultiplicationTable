with open('70x70乘法表.csv', 'w') as f:
    for y in range(1, 71):
        for x in range(1, 71):
            f.write('{}*{}={},'.format(x, y, x*y))
            print('{}*{}={}\t'.format(x,y,x*y), end='')
        f.write('\n')
        print()
