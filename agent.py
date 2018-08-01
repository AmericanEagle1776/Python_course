import random


class Agent:
    """there will be shorter and taller agents"""

    def __init__(self):
        """my secret agents have the characteristics name height and their dead/alive status"""
        self.name = ''
        self.height = 0
        self.situation = 'alive'

    def set_name(self):
        """names are given"""
        namelist = ['greg', 'gregg', 'gregory', 'gregster', 'genadine ysrup', 'jane', 'janet', 'jan', 'big j']
        self.name = random.choice(namelist)
        return self.name

    def set_height(self):
        "height is random and between 1.4 and 2.1m"
        self.height = random.uniform(1.4, 2.1)
        return self.height

    def chopperino(self):

        if self.height > 1.8:
            self.situation = 'dead'

        return self.situation



agent1 = Agent()
agent1.set_height()
agent1.set_name()
agent1.chopperino()
print('agent name:', agent1.name, ', agent height in m:', agent1.height)
print('agent status:', agent1.situation)

x = 0
while x < 10:
    x += 1
    agent = Agent()

    agent.set_height()
    agent.set_name()
    agent.chopperino()
    
    agent = "agent{}".format(x)


#if  __name__ =='__main__':

#agentlist = []
#l = []
#for thing in l[1:10]:
#
#    agent = Agent()
#    agent.name = agent.set_name()
#    agent.height = agent.set_height()
#    agentlist.append(agent)
#    a =1
#    agent = 'agent'+str(a)
#    a+=1
#
#for x in agentlist:
#    chopperino(x)
#
#for y in agentlist:
#    print(y.situation)