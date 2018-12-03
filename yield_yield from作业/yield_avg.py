def avg():
    print('start >>')
    num = 0
    sum = 0
    while 1:
        val = yield
        num += 1
        sum += val
        avg = sum / num
        print('平均值是{}'.format(avg))


if __name__=='__main__':
    cal = avg()
    next(cal)
    while 1:
        n = input('请输入数字')
        try:
            n = float(n)
            cal.send(n)
        except Exception:
            print('输入不是数字')
            continue