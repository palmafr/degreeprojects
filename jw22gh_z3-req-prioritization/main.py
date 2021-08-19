from z3 import *
from get_pairs import get_pairs
from get_requirements import get_requirements
from get_prio import get_prio
from get_dep import get_deps
from calc_disagree import calc_dis
from calc_avdist import calc_avdist
from get_GS import get_GS
import time
import random

print("Welcome!")
print("Please choose requirement scenario")
print("1. MON")
print("2. ESC")
print("3. FAL")
print("4. ALL")

print("Enter answer(number): ")

scenario = input()

if scenario == str(1):
    reqs = get_requirements("Req_monitor_Priority")
    prios = get_prio("Req_monitor_Priority")
    deps = get_deps("Req_monitor_Depend")
elif scenario == str(2):
    reqs = get_requirements("Req_escape_Priority")
    prios = get_prio("Req_escape_Priority")
    deps = get_deps("Req_escape_Depend")
elif scenario == str(3):
    reqs = get_requirements("Req_fall_Priority")
    prios = get_prio("Req_fall_Priority")
    deps = get_deps("Req_fall_Depend")
elif scenario == str(4):
    reqs = get_requirements("Req_all_Priority")
    prios = get_prio("Req_all_Priority")
    deps = get_deps("Req_all_Depend")    



print("Please choose maximum elicited pairs")
print("Enter answer: ")

max_eli = input()
if max_eli == '':
    max_eli = 100

population_size = 20
number_of_req = len(reqs)
solutions = 0

# Get all sets with same minimum cost.
def solva(eli_list):
    solver = Optimize()
    random.shuffle(reqs)
    # Array size is N.
    # No value can be less than 0 or more than N. Representing index numbers in an array with the span of 0 - N.
    for i in (reqs):
        solver.add(i >= 0)

    for i in (reqs):
        solver.add(i < len(reqs))

    # No duplications, only distinct unique values.
    for i, j in zip(reqs, reqs[1:]):
        solver.add(i != j)

    # Adding constraints for prioritizations. Default is soft constraints with weight 1
    for i in prios:
        for j in prios:
            if i[1] < j[1]:
                for r in reqs:
                    if i[0] == r.__str__():
                        temp = r
                    if j[0] == r.__str__():
                        temp2 = r   
                solver.add_soft(temp2 < temp, 1)

    # Adding constraints for dependencies. Default is soft constraints with weight 1
    index = 1
    hej = 1
    for i in deps:
        if hej == 1:
            on = "RT"
            if index < 10:
                on = on + "00" + str(index)
            else:
                on = on + "0" + str(index)
            for r in reqs:
                if on == r.__str__():
                    index2 = 1
                    for j in deps[index - 1]:
                        if j == 1:
                            on1 = "RT"
                            if index2 < 10:
                                on1 = on1 + "00" + str(index2)
                            else:
                                on1 = on1 + "0" + str(index2)
                            for r1 in reqs:
                                if on1 == r1.__str__():
                                    solver.add_soft(r1 < r, 1)
                        index2 += 1
            index += 1

    if len(eli_list[0]) > 1:
        ine = 0
        for pair in eli_list:
            if pair[0] == 0:
                #Then there are no more pairs
                break
            higher = pair[0]
            lower = pair[1]
            solver.add_soft(lower < higher, 1)
            ine += 0


    cost = 0
    currentcost = 0
    lists = []
    sets = 0
    while cost == currentcost:
        solver.check()
        random.shuffle(reqs)
        m = solver.model()
        cost = m.evaluate(solver.objectives()[0]).as_long()
        if cost <= currentcost or currentcost == 0:
            requirements_list = {}
            for i in range(number_of_req):
                d = {reqs[i].__str__(): m[reqs[i]].as_long()}
                requirements_list.update(d)
            currentcost = cost

            # Sort the list so that the prioritization is in descending order.
            sorted_list = sorted(requirements_list.items(), key=lambda x: x[1], reverse=True)

            # Add the solution to a list
            temp = []
            for i in sorted_list:
                temp.append(i[0])
            lists.append(temp)

            # Ignore the previous model by adding the current as constraints.
            solution = []
            index = 0
            for r in reqs:
                solution.append(r != solver.model()[reqs[index]])
                index += 1
            solver.add(Or(solution))
            sets += 1
            solutions = sets
            if solutions == population_size:
                break 
        print(currentcost)
    return lists

eli_list = [[0 for i in range(2)] for j in range(100)]
elicited = 0
exit = False
solutions = 0
error = 0
erroramount = 0


while solutions != 1 and elicited <= int(max_eli):
    pairs_list = []
    elicited_pairs = []
    lists = solva(eli_list)
    solutions = len(lists)
    if solutions == 1:
        break
    if exit == True:
        break

    if solutions != 1:
        #Do elicitation
        pairs_list = get_pairs(lists, eli_list)
        print(len(pairs_list))
        while len(elicited_pairs) != len(pairs_list):
            for pair in pairs_list:
                if pair not in elicited_pairs:
                    test = pair.split()
                    print("Elicitation between: 1. " + test[0] + " and 2. " + test[1] + ". Which is most important?")
                    choice = input()

                    if choice == str(1):
                        for r in reqs:
                            if r.__str__() == test[0]:
                                higher = r
                        for r2 in reqs:
                            if r2.__str__() == test[1]:
                                lower = r2
                        eli_list[elicited][0] = higher
                        eli_list[elicited][1] = lower
                        elicited += 1
                        elicited_pairs.append(pair)

                    if choice == str(2):
                        for r in reqs:
                            if r.__str__() == test[1]:
                                higher = r
                        for r2 in reqs:
                            if r2.__str__() == test[0]:
                                lower = r2

                        eli_list[elicited][0] = higher
                        eli_list[elicited][1] = lower
                        elicited += 1
                        elicited_pairs.append(pair)

                    if elicited == int(max_eli):
                        exit = True
                        break
                    if len(elicited_pairs) == len(pairs_list):
                        break
            if exit == True:
                break        
    if pairs_list == []:
        break      
  

disagree = []
averagedist = []
gold_standard = []
if scenario == str(1):
    gold_standard = get_GS("Req_monitor_gold")
if scenario == str(2):
    gold_standard = get_GS("Req_escape_gold")
if scenario == str(3):
    gold_standard = get_GS("Req_fall_gold")
if scenario == str(4):
    gold_standard = get_GS("Req_all_gold")

f = open("result.txt", "a")
f.write("\n")
f.write("\n")
f.write("Requirement sets")
f.write("\n")
for orders in lists:
    f.write(str(orders))
    f.write("\n")
f.write("Disagreement")
f.write("\n")
for list in lists:
    disagree.append(calc_dis(list, gold_standard))
    f.write(str(calc_dis(list, gold_standard)))
    f.write("\n")
f.write("Average distance")
f.write("\n")    
for list in lists:
    averagedist.append(calc_avdist(list, gold_standard))
    f.write(str(calc_avdist(list, gold_standard)))
    f.write("\n")
f.write("Lowest disagreement: " + str(min(disagree)) + "\n")
f.write("Lowest average distance: " + str(min(averagedist)) + "\n")
f.write("------------------------ END ------------------------")
f.close()




