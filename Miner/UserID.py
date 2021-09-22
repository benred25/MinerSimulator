from datetime import datetime

class UserID (object):

    """ Constructor """
    def __init__(self, name):
        """
        Construct a new object.

        :param name: STRING, The user name.
        startDate: The date of the account was created.
        """
        self.__username = name
        self.__startDate = datetime.now().date().today()    # This attributes will not be change ever once it has been initialized.

    """ Methods """
    def getName(self):
        """
        Gets the name of the user.

        :return: the username of the user.
        """
        return self.__username

    def setName(self, newName):
        """
        Change the user's username.

        :param newName: The new username that will replaced.
        :return: None
        """
        self.__username = newName

    def getStartDate(self):
        """
        Gets the birth of the account.

        :return: The date of the time the account was created.
        """
        return self.__startDate

""" TEST CASES FOR UserID CLASS """
if __name__ == '__main__':
    actor = UserID("Adrian")

    name = actor.getName()
    if name != "Adrian":
        print("Error: self.username expected value is (Adrian)")
        print("       value got is,", actor.getName())
        exit()

    actor.setName("Maicaella")
    updatedName = actor.getName()
    if updatedName != "Maicaella":
        print("Error: self.username does not change to (Maicaella)")
        print("       the value is still,", actor.getName())
        exit()

    time = actor.getStartDate()
    if time != actor.getStartDate():
        print("Error: getStartDate() does not match to self.startDate")
        print("       the value is,", actor.getStartDate())
        exit()

    print("**** TEST COMPLETE ****")