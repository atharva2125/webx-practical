// Define the PersonInfo interface
interface PersonInfo {
    name: string;
    age: number;
}

// Implement the Person class
class Person implements PersonInfo {
    name: string;
    age: number;

    constructor(name: string, age: number) {
        this.name = name;
        this.age = age;
    }

    displayInfo(): void {
        console.log(`Name: ${this.name}, Age: ${this.age}`);
    }
}

// Example usage
const person = new Person("Alice", 30);
person.displayInfo();
// Output: Name: Alice, Age: 30