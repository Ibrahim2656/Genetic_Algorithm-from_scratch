import random
import Chromosome as ch

#create random chromosomes (we will shuffle node list randomly)
def create_random_list(n_list):
    start=n_list[0] #start and points and should be same ,so keep first point before shuffling
    temp=n_list[1:]
    temp=random.sample(temp,len(temp)) # shuffle the node list to achieve the randmaize
    temp.insert(0,start)# add the start point at the first 
    temp.append(start) # add the start point to the end
    return temp

#creat the population
def creat_pop(data,pop_size):
    init_pop=[]
    for i in range(0,pop_size):#creat chomosomes as much as population size
        temp=create_random_list(data)
        new_chromo=ch.chromosome(temp)
        init_pop.append(new_chromo)
    return init_pop

#selection of parents chromosomes to create childs
def selection(population): #tournament selction
    f1,f2,f3,f4=random.sample(range(0,len(population)-1),4)
    #create candidate chromosomes based on the fighters
    candidate1=population[f1]
    candidate2=population[f2]
    candidate3=population[f3]
    candidate4=population[f4]
    # select the winner 
    if candidate1.fitness>candidate2.fitness:
        winner=candidate1
    else:
        winner=candidate2
    if candidate3.fitness>winner.fitness:
        winner=candidate3
    if candidate4.fitness>winner.fitness:
        winner=candidate4
    return winner

#cross over (one point,two point ,mixed)
# one point
def crossover(parent1,parent2):
    one_point=random.randint(2,14)
    #first part from crossover
    child1=parent1.chromosome[1:one_point]
    child2=parent2.chromosome[1:one_point]
    #second part from crossover
    child1_remain=[genes for genes in parent2.chromosome[1:-1] if genes not in child1]
    child2_remain=[genes for genes in parent1.chromosome[1:-1] if genes not in child2]
    #combine them to each other
    child1+=child1_remain
    child2+=child2_remain
    #adding the start point and end points
    #bc they are they should be the same 
    child1.insert(0,parent1.chromosome[0])
    child1.append(parent1.chromosome[0])

    child2.insert(0,parent2.chromosome[0])
    child2.append(parent2.chromosome[0])
    return child1,child2
# two points crossover
def crossover_twopoints(parent1,parent2):
    point1,point2=random.sample(range(1,len(parent1.chromosome)-1),2)
    begin=min(point1,point2)
    end=max(point1,point2)
    
    child1=parent1.chromosome[begin:end+1]
    child2=parent2.chromosome[begin:end+1]
    
    child1_remain=[genes for genes in parent2.chromosome if genes not in child1]
    child2_remain=[genes for genes in parent1.chromosome if genes not in child2]
    
    child1+=child1_remain
    child2+=child2_remain
    
    child1.insert(0,parent1.chromosome[0])
    child1.append(parent1.chromosome[0])
    
    child2.insert(0,parent2.chromosome[0])
    child2.append(parent2.chromosome[0])
    return child1,child2

# 3 mixed two  points crossover
def crossover_mix(parent1,parent2):
    point_1, point_2 = random.sample(range(1, len(parent1.chromosome)-1), 2)
    begin = min(point_1, point_2)
    end = max(point_1, point_2)

    child_1_1 = parent1.chromosome[:begin]
    child_1_2 = parent1.chromosome[end:]
    child_1 = child_1_1 + child_1_2
    child_2 = parent2.chromosome[begin:end+1]

    child_1_remain = [item for item in parent2.chromosome[1:-1] if item not in child_1]
    child_2_remain = [item for item in parent1.chromosome[1:-1] if item not in child_2]

    child_1 = child_1_1 + child_1_remain + child_1_2
    child_2 += child_2_remain

    child_2.insert(0, parent2.chromosome[0])
    child_2.append(parent2.chromosome[0])

    return child_1, child_2

def mutation(m_chromosome):# swap two nodes of the chromosome
    mutation_idx_1,mutation_idx_2=random.sample(range(1,19),2)
    m_chromosome[mutation_idx_1],m_chromosome[mutation_idx_2]=m_chromosome[mutation_idx_2],m_chromosome[mutation_idx_1]
    return m_chromosome

#find the best chromosome of the genration based on the cost
def find_best(generation):
    best=generation[0]
    for i in range(1,len(generation)):
        if generation[i].cost < best.cost:
            best=generation[i]
    return best
# use elitism ,crossover ,mutation operators to create  new genration based on the previous one 
def create_new_genration(pre_genraition,mutation_rate,crossover_method):
    new_genration=[find_best(pre_genraition)] #this is for elitism(keep the best of the previous)
    for i in range(0,int(len(pre_genraition)/2)):
        parent1=selection(pre_genraition)
        parent2 =selection(pre_genraition)
        
        if crossover_method=="crossover":
            child1,child2=crossover(parent1,parent2)
        elif crossover_method=="crossover_twopoints":
            child1,child2=crossover_twopoints(parent1,parent2)
        else:#deafult
            child1,child2=crossover_mix(parent1,parent2)
        
        child1=ch.chromosome(child1)
        child2=ch.chromosome(child2)
        
        if random.random() <mutation_rate:
            mutated=mutation(child1.chromosome)
            child1=ch.chromosome(mutated)
        new_genration.append(child1)
        new_genration.append(child2)
    return new_genration
        


