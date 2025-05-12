var Rectangle = /** @class */ (function () {
    function Rectangle(width, height) {
        this.width = width;
        this.height = height;
    }
    Rectangle.prototype.calculateArea = function () {
        return this.width * this.height;
    };
    return Rectangle;
}());
var rectangle = new Rectangle(10, 5);
console.log("Area of the rectangle: ".concat(rectangle.calculateArea()));
