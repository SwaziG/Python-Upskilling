import random
import pylab

# Global Variables
MAXRABBITPOP = 1000
CURRENTRABBITPOP = 500
CURRENTFOXPOP = 30

def rabbitGrowth():
    """ 
    rabbitGrowth is called once at the beginning of each time step.

    It makes use of the global variables: CURRENTRABBITPOP and MAXRABBITPOP.

    The global variable CURRENTRABBITPOP is modified by this procedure.

    For each rabbit, based on the probabilities in the problem set write-up, 
      a new rabbit may be born.
    Nothing is returned.
    """
    # you need this line for modifying global variables
    global CURRENTRABBITPOP
    
    count = 0
    for rabit in range(CURRENTRABBITPOP):
        prob_rep = 1-(CURRENTRABBITPOP/MAXRABBITPOP)
        if random.random() <= prob_rep:
            count += 1
    CURRENTRABBITPOP += count
   
            
def foxGrowth():
    """ 
    foxGrowth is called once at the end of each time step.

    It makes use of the global variables: CURRENTFOXPOP and CURRENTRABBITPOP,
        and both may be modified by this procedure.

    Each fox, based on the probabilities in the problem statement, may eat 
      one rabbit (but only if there are more than 10 rabbits).

    If it eats a rabbit, then with a 1/3 prob it gives birth to a new fox.

    If it does not eat a rabbit, then with a 1/10 prob it dies.

    Nothing is returned.
    """
    # you need these lines for modifying global variables
    global CURRENTRABBITPOP
    global CURRENTFOXPOP

    fox = 0
    d_rab = 0
    for f in range(CURRENTFOXPOP):
        if (CURRENTRABBITPOP - d_rab) > 10:
            prob_eat = ((CURRENTRABBITPOP - d_rab)/MAXRABBITPOP)
            if random.random() <= prob_eat:
                d_rab += 1
                if random.choice([1,0,0]) == 1:
                    fox += 1
            else:
                if (CURRENTFOXPOP + fox) > 10:
                    if random.random() <= 0.1:
                        fox -= 1
        else:
            if (CURRENTFOXPOP + fox) > 10:
                if random.random() <= 0.1:
                    fox -= 1
       
    CURRENTFOXPOP += fox
    CURRENTRABBITPOP -= d_rab
    
            
def runSimulation(numSteps):
    """
    Runs the simulation for `numSteps` time steps.

    Returns a tuple of two lists: (rabbit_populations, fox_populations)
      where rabbit_populations is a record of the rabbit population at the 
      END of each time step, and fox_populations is a record of the fox population
      at the END of each time step.

    Both lists should be `numSteps` items long.
    """
    rabbit_populations = []
    fox_populations = []
    
    for step in range(numSteps):
        rabbitGrowth()
        foxGrowth()
        rabbit_populations.append(CURRENTRABBITPOP)
        
        fox_populations.append(CURRENTFOXPOP)
        
    
    return (rabbit_populations, fox_populations)

random.seed(0)
time = 500
D = runSimulation(time)

time_list = []
for i in range(time):
    time_list.append(i+1)
x, y = D
pylab.plot(x, time_list, label='Rabbits')
pylab.plot(y, time_list, label='Foxes')
pylab.title("Rabbits vs Foxes")
pylab.xlabel("Pop")
pylab.ylabel("Time")
model1 = pylab.polyfit(x, time_list, 2)
estYvals = pylab.polyval(model1, x)
pylab.plot(x, estYvals,'g', label='Rab')

model2 = pylab.polyfit(y, time_list, 2)
estYvals2 = pylab.polyval(model2, y)
pylab.plot(y, estYvals2,'r-', label='fox')
pylab.legend(loc="best")
pylab.show()

