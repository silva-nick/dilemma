import dilemma
import random
import numpy as np

class Main:

    def __init__(self):

        self.display_one_trial()
        pass

    def q_equilibrium(self, firm1, firm2):

        epsilon = 1 #rate at which it randomly explores

        for i in range(1000): #number of iterations
            if(epsilon > random.random()): #should we explore or not
                action1 = random.randint(0, 2)
                action2 = random.randint(0, 2)
                firm1.run(action1, action2)
                firm2.run(action2, action1)
            else:
                action1 = firm1.best_action()
                action2 = firm2.best_action()
                firm1.run(action1, action2)
                firm2.run(action2, action1)
            epsilon -= .001 #decreasing the exploration rate so that it learns using previous q values

    def nash_equilibrium(self, firm1n, firm2n):
        #attempts to find the nash equilbrium for the two tables so that it can be compared to the qTable
        output = []
        for i in range (len(firm1n)):
            if firm1n[i] == firm2n[i]:
                output.append((firm1n[i], firm2n[i]))
        return output

    def display_one_trial(self):
        #display the results\
        firm1 = dilemma.Firm()
        firm2 = dilemma.Firm()
        firm1.create()
        firm2.create()

        self.q_equilibrium(firm1, firm2)

        print(firm1.best_action())
        print(firm1.printp())
        print(firm1.getq())
        print(firm1.find_nash())
        print()
        print(firm2.best_action())
        print(firm2.printp())
        print(firm2.getq())
        print(firm2.find_nash())
        print()

        self.print_dmatrix(firm1, firm2)
        print(self.nash_equilibrium(firm1.find_nash(), firm2.find_nash()))

    def print_dmatrix(self, firm1, firm2):

        x = firm1.getp()
        y = firm2.getp()
        z = [[], [], []]
        for i in range(3):
            for j in range(3):
                z[i].append( (x[i][j], y[i][2-j] ))
            print(z[i])


    def test(self, n): #number of tests

        success_count = 0
        for i in range(n):
            firm1 = dilemma.Firm()
            firm2 = dilemma.Firm()
            firm1.create()
            firm2.create()

            self.q_equilibrium(firm1, firm2)

            q_decision = ( firm1.best_action(), firm2.best_action() )
            n_decision = self.nash_equilibrium(firm1.find_nash(), firm2.find_nash())
            if q_decision in n_decision:
                success_count += 1

        print( str(success_count * 100 / n) + "% success rate" )

test = Main()
test.test(500)
