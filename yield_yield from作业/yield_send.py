str_list = []
int_list = []
def f1():
    print('function start')
    while 1:
        try:

            a = yield
            print(a)
            if isinstance(a,str):
                str_list.append(a)
            else:
                int_list.append(a)
        except StopIteration:
            return  str_list,int_list

if __name__=='__main__':
    f = f1()
    next(f)
    f.send(1)
    f.send(2)
    f.send('saf')
    f.send('13')
    try:
        f.throw(StopIteration)
    except Exception as e:
        x = e.value
    print(x)

