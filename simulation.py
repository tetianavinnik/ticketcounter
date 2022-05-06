"""Implementation of the main simulation class"""
from arrays import Array
from linkedqueue import LinkedQueue
from simpeople import TicketAgent, Passenger
import random


class TicketCounterSimulation :
    """Create a simulation object."""
    def __init__(self, numAgents, numMinutes, betweenTime, serviceTime):
        """
        Parameters supplied by the user.
        """
        self._arriveProb = 1.0 / betweenTime
        self._serviceTime = serviceTime
        self._numMinutes = numMinutes

        # Simulation components.
        self._passengerQ = LinkedQueue()
        self._theAgents = Array(numAgents)
        for i in range(numAgents) :
            self._theAgents[i] = TicketAgent(i+1)

        # Computed during the simulation.
        self._totalWaitTime = 0
        self._numPassengers = 0
        self._passCountForId = 0
        self._surving_right_now = 0
    

    def _handleArrival(self, curTime):
        """
        Determines if a passenger arrives during the current
        time step and handles that arrival.
        """
        if random.uniform(0, 1) <= self._arriveProb:
            self._numPassengers += 1
            self._passCountForId += 1
            create_passanger = Passenger(self._passCountForId, curTime)
            self._passengerQ.add(create_passanger)
            print(f'Time {curTime}: Passenger {self._passCountForId} arrived.')


    def _handleBeginService(self, curTime):
        """
        Determines if any agents are free and allows the next
        passenger(s) in line to begin their transaction.
        """
        for agent in self._theAgents:
            if agent.isFree():
                try:
                    passanger_to_serve = self._passengerQ.pop()
                    self._surving_right_now += 1
                    agent.startService(passanger_to_serve, curTime + self._serviceTime)
                    self._totalWaitTime += curTime - passanger_to_serve.timeArrived()
                    print(f'Time {curTime}: Agent {agent.idNum()} started serving passenger {passanger_to_serve.idNum()}')
                except:
                    break


    def _handleEndService(self, curTime):
        """
        Determines which of the current transactions have
        completed, if any, and flags a passenger departure.
        """
        for agent in self._theAgents:
            if agent.isFinished(curTime):
                passenger_served = agent.stopService()
                self._surving_right_now -=1 
                print(f'Time {curTime}: Agent {agent.idNum()} stopped serving passenger {passenger_served.idNum()}.')


    def run(self):
        """
        Run the simulation using the parameters supplied earlier.
        """
        for curTime in range(self._numMinutes + 1):
            self._handleArrival(curTime)
            self._handleBeginService(curTime)
            self._handleEndService(curTime)


    def printResults(self):
        """
        Print the simulation results.
        """
        numServed = self._numPassengers - len(self._passengerQ) - self._surving_right_now
        avgWait = float(self._totalWaitTime) / numServed
        print("")
        print("Number of passengers served = ", numServed)
        print("Number of passengers remaining in line = %d" %
               len(self._passengerQ))
        print("The average wait time was %4.2f minutes." % avgWait)
