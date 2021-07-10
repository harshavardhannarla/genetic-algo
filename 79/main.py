import client1
import numpy as np  
import random
import math

population_sz=10
strtgne=278
generations =50
gnome_len =11
team_key ="THAt98zM1b3icQ1ai0cH9gkdnzDEFoMgspHYasoHHdpw2iChpl"


population =np.empty((population_sz,11))

population = np.array([[0.0, -1.0460172422404952e-12, -1.3834235839810128e-13, 2.3715753221091636e-11, -4.549537304155811e-11, -4.669174679337759e-16, 3.155401095167029e-16, 1.7794262377702856e-05, -1.4700710303389147e-06, -9.927932941915639e-09, 6.336563988741462e-10],
[0.0, -1.159712009301162e-12, -1.3338768810992083e-13, 3.1229539214990914e-11, -4.2240725065362273e-11, -4.4338501479136483e-16, 2.692758336403245e-16, 1.864164579436363e-05, -1.5507269869286544e-06, -9.922793976829005e-09, 6.546930781078044e-10],
[0.0, -1.0465009645866616e-12, -1.3784540818270984e-13, 2.4107321395975675e-11, -5.0437427663329934e-11, -4.621205127708679e-16, 2.9923676388248376e-16, 1.7828015370490633e-05, -1.6604440592630714e-06, -9.928515044090427e-09, 7.212426272851862e-10],
[0.0, -1.1260646309787744e-12, -1.5111934977323482e-13, 2.4107238148416907e-11, -4.226746769040594e-11, -4.674599849814754e-16, 3.1307619264767357e-16, 1.539056250525894e-05, -1.474296254666533e-06, -9.40532324636257e-09, 6.347779107358939e-10],
[0.0, -1.1320763436627143e-12, -1.3839871606070884e-13, 2.5275998724884432e-11, -4.9283523883402116e-11, -4.693041390318637e-16, 3.1567675443723242e-16, 1.4148083507490842e-05, -1.3279778758947486e-06, -9.374145853338194e-09, 5.805281270905425e-10],
[0.0, -1.1348988202752062e-12, -1.3921576079330747e-13, 2.301597156269311e-11, -5.112283256692137e-11, -4.772683117087704e-16, 2.839665065798019e-16, 1.760848394796253e-05, -1.4621703136312468e-06, -8.774009377654883e-09, 6.316290350302175e-10],
[0.0, -9.913581536352492e-13, -1.1978395894694268e-13, 2.770288435016976e-11, -3.9621468131985574e-11, -3.2676933995217423e-16, 2.517922954252555e-16, 1.5981458458380236e-05, -1.5819526939731573e-06, -9.938816543523618e-09, 6.626307460769624e-10],
[0.0, -1.0418401345310036e-12, -1.4263369327728633e-13, 2.0073447707461568e-11, -4.6242990167209624e-11, -5.083408145123835e-16, 3.227959158514242e-16, 1.7502793754205084e-05, -1.431716271532482e-06, -1.0868455208858067e-08, 6.063590869437246e-10],
[0.0, -1.064730353344615e-12, -1.1890353710775887e-13, 3.9032452779919674e-11, -4.796349690220912e-11, -2.395449626382315e-16, 2.826727719919815e-16, 1.911484589945004e-05, -1.5334615844805423e-06, -9.952041884720208e-09, 6.78705996968254e-10],
[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]])


def create_gnome():
    ans =  [random.uniform(-10.0,10.0) for _ in range(gnome_len)]
    return np.array(ans)

def sort_fn(population,f):
    return population[f.argsort()]

def mate(sel_parents):
    children = np.zeros((10,11))
    """for i in range(int(population_sz/2)):
        p1i =  random.randint(0,int(population_sz/2)-1)
        p2i =  random.randint(0,int(population_sz/2)-1)
        p1 = sel_parents[p1i]
        p2 = sel_parents[p2i]

        temp = random.random()
        if(temp <0.5):
            k = (2*temp)**((4)**-1)
        else:
            k = ((2*(1-temp))**-1)**((4)**-1)
            
        children[i] = 0.5*((1+k)*p1 + (1-k)*p2)
        children[i*2+1] = 0.5*((1-k)*p1 + (1+k)*p2)"""
    for i in range(population_sz):
        p1i =  random.randint(0,int(population_sz/2)-1)
        p2i =  random.randint(0,int(population_sz/2)-1)
        p1 = sel_parents[p1i]
        p2 = sel_parents[p2i]
        cut_index = 6
        child = np.zeros((11))
        child[:cut_index]=p1[:cut_index]
        child[cut_index:] = p2[cut_index:]
        children[i] =child
    
    return children





def mutate(population,sz):
    for i in range(1,sz):
        for j in range(11):
            p= random.random()
            if p > 0.68 :
                population[i][j] += random.uniform(-0.2,0.2)*population[i][j]
                if population[i][j] <-10:
                    population[i][j] = -10
                elif population[i][j] > 10:
                    population[i][j] =10

    return population



def intialmutate(population):
    for i in range(2,population_sz):
        for j in range(11):
            p= random.random()
            if p < 0.68 :
                p1 = random.random()
                if p1 > 0.5:
                    population[i][j] += 0.3*population[i][j]
                else:
                    population[i][j] -= 0.3*population[i][j]
                if population[i][j] <-10:
                    population[i][j] = -10
                elif population[i][j] > 10:
                    population[i][j] =10

    return population




fitness =np.empty((12))



f=np.empty((10))
for i in range(population_sz):
    a= client1.get_errors(team_key,list(population[i]))
    f[i] = a[0]+a[1]

population = sort_fn(population,f)

for generation in range(1,generations+1):
    
    print("Generation: ",generation+strtgne)
    print()  
    print("Intial popln: ",)
    for i in range(int(population_sz)):
       print(list(population[i]))
    print()
    print("After Selection:")    
    for i in range(int(population_sz/2)):
       print(list(population[i]))



    t = np.empty((12,11))
    t[0:2,:]=population[0:2,:]
    t[2:12,:] = mate(population[:int(population_sz/2)])

    print()
    print("After CrossOver:")    
    for i in range(12):
       print(list(t[i]))
    
    t= mutate(t,12)
    
    
    for i in range(12):
        a= client1.get_errors(team_key,list(t[i]))
        fitness[i] = a[0]+a[1]

    t =  sort_fn(t,fitness)
    population = t[0:10,:]

    print()
    print("After Mutation:")    
    for i in range(10):
       print(list(population[i]))


    client1.submit(team_key,list(population[0]))

    print("Min of Generation:",generation+strtgne ,": ", min(fitness))
    print("Best vector of this gen ",list(population[0]))
    print()


            



