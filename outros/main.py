import dog

def main():
    dog1 = dog.Dog("Hector", 5)
    # print(dog1.description())
    print(dog1)
    print(dog1.speak('Ruf, ruf'))

    dog2 = dog.Bulldog("Avarez", 3)
    print(dog2)
    print(type(dog2))
    print(isinstance(dog2, dog.Dog))
    print(dog2.speak())

if __name__ == "__main__":
    main()
