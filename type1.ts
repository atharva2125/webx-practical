
class Animal {
    makeSound(): void {
        console.log("Animal makes a sound");
    }
}

class Dog extends Animal {
    makeSound(): void {
        console.log("Dog barks");
    }
}
 
const animal = new Animal();
animal.makeSound(); 

const dog = new Dog();
dog.makeSound();  