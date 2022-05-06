"""simpeople"""


class Passenger :
    """Creates a passenger object."""
    def __init__(self, idNum, arrivalTime):
        self._idNum = idNum
        self._arrivalTime = arrivalTime


    def idNum(self):
        """
        Gets the passenger's id number.
        """
        return self._idNum


    def timeArrived(self):
        """
        Gets the passenger's arrival time.
        """
        return self._arrivalTime


class TicketAgent :
    """Creates a ticket agent object."""
    def __init__(self, idNum):
        self._idNum = idNum
        self._passenger = None
        self._stopTime = -1


    def idNum(self):
        """
        Gets the ticket agent's id number.
        """
        return self._idNum


    def isFree(self):
        """
        Determines if the ticket agent is free to assist a passenger.
        """
        return self._passenger is None


    def isFinished(self, curTime):
        """
        Determines if the ticket agent has finished helping the passenger.
        """
        return self._passenger is not None and self._stopTime == curTime


    def startService(self, passenger, stopTime):
        """
        Indicates the ticket agent has begun assisting a passenger.
        """
        self._passenger = passenger
        self._stopTime = stopTime


    def stopService(self):
        """
        Indicates the ticket agent has finished helping the passenger.
        """
        thePassenger = self._passenger
        self._passenger = None
        return thePassenger
