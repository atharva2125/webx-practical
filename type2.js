var Student = /** @class */ (function () {
    function Student(name, rollNo, course) {
        this.name = name;
        this.rollNo = rollNo;
        this.course = course;
    }
    Student.prototype.displayDetails = function () {
        console.log("Name: ".concat(this.name));
        console.log("Roll No: ".concat(this.rollNo));
        console.log("Course: ".concat(this.course));
    };
    return Student;
}());
var student = new Student("John Doe", 101, "Computer Science");
student.displayDetails();
