// Implement the Person class
var Person = /** @class */ (function () {
    function Person(name, age) {
        this.name = name;
        this.age = age;
    }
    Person.prototype.displayInfo = function () {
        console.log("Name: ".concat(this.name, ", Age: ").concat(this.age));
    };
    return Person;
}());
// Example usage
var person = new Person("Alice", 30);
person.displayInfo();
// Output: Name: Alice, Age: 30
