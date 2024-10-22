# main.py
from animals.mammals import Dog
from animals.birds import Eagle

def main():
    dog = Dog("Buddy", "Golden Retriever")
    eagle = Eagle("Freedom", 2.3)

    print(dog)
    print(dog.speak())
    print(eagle)
    print(eagle.fly())

if __name__ == "__main__":
    main()