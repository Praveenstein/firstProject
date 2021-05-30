# Duck Typing and Easier to ask forgiveness than permission (EAFP)


class Duck:

    def quack(self):
        print('Quack, quack')

    def fly(self):
        print('Flap, Flap!')


class Person:

    def quack(self):
        print("I'm Quacking Like a Duck!")

    def fly(self):
        print("I'm Flapping my Arms!")


def quack_and_fly(thing):
    # LBYL (Non-Pythonic)
    # if hasattr(thing, 'quack'):
    #         thing.quack()
    #
    # if hasattr(thing, 'fly'):
    #         thing.fly()

        try:
            thing.quack()
            thing.fly()
            thing.bark()
        except AttributeError as e:
            print(e)

d = Duck()
p = Person()

quack_and_fly(d)
quack_and_fly(p)
