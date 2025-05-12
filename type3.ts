 
interface Shape {
    calculateArea(): number;
}
 
class Rectangle implements Shape {
    private width: number;
    private height: number;

    constructor(width: number, height: number) {
        this.width = width;
        this.height = height;
    }

    calculateArea(): number {
        return this.width * this.height;
    }
}
 
const rectangle = new Rectangle(10, 5);
console.log(`Area of the rectangle: ${rectangle.calculateArea()}`);
 