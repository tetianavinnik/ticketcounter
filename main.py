
from simulation import TicketCounterSimulation

numAgents = int(input("Number of ticket agents: "))
numMinutes = int(input("Number of minutes to simulate: "))
betweenTime = int(input("Average time between passenger arrival: "))
serviceTime = float(input("Average service time per passenger: "))

model = TicketCounterSimulation(numAgents, numMinutes, betweenTime, serviceTime)

model.run()
model.printResults()
