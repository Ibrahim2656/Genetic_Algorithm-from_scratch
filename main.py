import numpy as np
import matplotlib.pyplot as plt
import Chromosome as ch
import Genetic_Algorithm as GA
from tkinter import filedialog
def gentic_algorithm(no_genartion,pop_size,mutation_rate,data,crossover_method,stopping_method
                     ,number_of_saturation,number_of_stopgen):
    new_gen=GA.creat_pop(data,pop_size)
    costs_for_plot=[]
    for i in range(0,no_genartion):
        new_gen=GA.create_new_genration(new_gen,mutation_rate,crossover_method)
        print(str(i) + ". generation --> " + "cost --> " + str(new_gen[0].cost))
        costs_for_plot.append(GA.find_best(new_gen).cost)
        if stopping_method=='Saturation' and i>=number_of_saturation:
            cost=costs_for_plot[len(costs_for_plot)-1]
            counter=0
            for i in range(1,number_of_saturation+1):
                if cost==costs_for_plot[(len(costs_for_plot)-1)-i]:
                    counter+=1
            if counter==number_of_saturation:
                break
        elif stopping_method=='number_of_generation':
            if (i+1)==number_of_stopgen:
                break
    return new_gen,costs_for_plot

def draw_cost_generation(y_list):
    x_list=np.arange(1,len(y_list)+1)
    plt.plot(x_list,y_list)
    plt.title("Route Cost through Generations")
    plt.xlabel("Generations")
    plt.ylabel("Cost")
    plt.show()

def draw_path(solution):
    x_list=[]
    y_list=[]
    for i in range(0,len(solution.chromosome)):
        x_list.append(solution.chromosome[i].x_axis)
        y_list.append(solution.chromosome[i].y_axis)
    fig, ax = plt.subplots()
    plt.scatter(x_list,y_list)
    ax.plot(x_list, y_list, '--', lw=2, color='black', ms=10)
    ax.set_xlim(0, 1650)
    ax.set_ylim(0, 1300)
    plt.show()




numbers_of_generations=int(input("Enter the number of genrations : ")) #the iteration size of the for loop 
population_size=int(input("Enter the size of your population : ")) #this shows how many solutoins will be available in a genration
mut_rate=float(input("Enter the mutation rate from (0-1) : ")) #mutation rate for solution diversity.It should be btw 0 and 1. 0.2
crossmethod=None
stopping_method=None
Flag=False # for the loop to take the input of methods
number_of_saturation=None
number_of_stopgen=None
while(True):
    if Flag==False:
        print("1-crossover with one point")
        print("2-crossover with two points")
        print("3-crossover with mixed points")
        crossover_meth=int(input("Enter the Id of the method : "))
    if crossover_meth==1 and Flag==False:
        method="crossover"
        Flag=True
    elif crossover_meth==2 and Flag==False:
        method="crossover_twopoints"
        Flag=True
    elif crossover_meth==3 and Flag==False:
        method="crossover_mix"
        Flag=True
    elif crossover_meth not in [1,2,3] and Flag==False:
        print("In valild input please try again.")
    if Flag==True:
        print("Please choose the method of stoping :")
        print("1-saturation")
        print("2-numbers of generations")
        id=int(input("Enter the id of your choice :"))
        if id==1:
            stopping_method='Saturation'
            number_of_saturation=int(input("Enter the number of generation to check : "))
            break
        elif id==2:
            stopping_method='number_of_generation'
            number_of_stopgen=int(input("Enter the number of generation that after it the code will stop :"))
            break
        else:
            print("In valild input please try again.")
            
        
dataset=ch.dataset 

last_gen,y_axis=gentic_algorithm(numbers_of_generations ,population_size,mut_rate,dataset,method,stopping_method,number_of_saturation,number_of_stopgen)
best_sol=GA.find_best(last_gen)
draw_cost_generation(y_axis)
draw_path(best_sol)

