from collections import namedtuple
from random import randint
from queue import PriorityQueue

Event = namedtuple('Event','time,taxi_id,event')
class Taxi:
    def __init__(self, n = 3):
        """
        定义taxi列表，事件,初始化完成创建taxi
        """
        self.taxi_event_quene = PriorityQueue()
        self.taxi_list = []
        self.create_taxi(n)


    def taix_event(self,trips ,time,taxi_id):
        """
        taxi event,发出，上客，下客，回家
        :return:
        """
        time = yield Event(time,taxi_id,'出发')
        for i in range(trips):
            time = yield Event(time, taxi_id, '上客')
            time = yield Event(time, taxi_id, '下客')
        yield Event(time, taxi_id, '回家')

    def create_taxi(self,n):
        """
        产生taxi，开始‘出发’事件,把taxi加到list中
        :param n:
        :return:
        """
        for taxi_num in range(n):
            taxi = self.taix_event(trips=randint(10,20),taxi_id=taxi_num+1,time = randint(1,10))

            self.taxi_list.append(taxi)

    def active_taxi(self):
        """
        激活taxi，出发事件，把事件放入queue中
        :return:
        """
        for taxi in self.taxi_list:
           event =  next(taxi)
           self.taxi_event_quene.put(event)

    def log(self,time,taxi_id,event):
        """
        打印事件
        :return:
        """
        print('{}号出租车 在{}分钟 发生{}事件'.format(taxi_id, time, event))

    def start(self):
        """
        taix 开的时候要还有出发事件,激活taxi
        :return:
        """
        self.active_taxi()
        while 1:
            taxi_event = self.taxi_event_quene.get()
            time,taxi_id,event = taxi_event
            self.log(time,taxi_id,event)
            try:
                event = self.taxi_list[taxi_id-1].send(time + randint(1,10))
                self.taxi_event_quene.put(event)
            except StopIteration:
                print('出租车{}完成了任务'.format(taxi_id))


if __name__=='__main__':
    taxi =Taxi()
    taxi.start()