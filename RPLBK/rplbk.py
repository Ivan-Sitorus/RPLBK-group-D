from abc import ABC, abstractmethod

# Antarmuka terpisah sesuai fungsionalitas spesifik

class Work(ABC):
    @abstractmethod
    def work(self):
        pass

class Eat(ABC):
    @abstractmethod
    def eat(self):
        pass

class Rest(ABC):
    @abstractmethod
    def rest(self):
        pass

# Kelas pekerja kantor yang bekerja, makan, dan beristirahat
class OfficeWorker(Work, Eat, Rest):
    def work(self):
        print("OfficeWorker is working.")

    def eat(self):
        print("OfficeWorker is eating.")

    def rest(self):
        print("OfficeWorker is resting.")

# Kelas robot yang hanya bekerja, tidak makan dan tidak beristirahat
class Robot(Work):
    def work(self):
        print("Robot is working.")

# Kelas hewan yang bisa makan dan istirahat, tapi tidak bekerja
class Animal(Eat, Rest):
    def eat(self):
        print("Animal is eating.")

    def rest(self):
        print("Animal is resting.")

# Kelas atlet yang bekerja (berlatih), makan, dan beristirahat
class Athlete(Work, Eat, Rest):
    def work(self):
        print("Athlete is training.")

    def eat(self):
        print("Athlete is eating.")

    def rest(self):
        print("Athlete is resting.")


def main():
    # Instance OfficeWorker
    office_worker = OfficeWorker()
    office_worker.work()  # Output: OfficeWorker is working.
    office_worker.eat()   # Output: OfficeWorker is eating.
    office_worker.rest()  # Output: OfficeWorker is resting.

    print("-" * 30)

    # Instance Robot
    robot = Robot()
    robot.work()          # Output: Robot is working.

    print("-" * 30)

    # Instance Animal
    animal = Animal()
    animal.eat()          # Output: Animal is eating.
    animal.rest()         # Output: Animal is resting.

    print("-" * 30)

    # Instance Athlete
    athlete = Athlete()
    athlete.work()        # Output: Athlete is training.
    athlete.eat()         # Output: Athlete is eating.
    athlete.rest()        # Output: Athlete is resting.

if __name__ == "__main__":
    main()
