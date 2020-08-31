from shapes import Paper, Triangle, Rectangle, Oval

paper = Paper()

rect1 = Rectangle()
rect1.set_width(200)
rect1.set_height(100)
rect1.set_color("blue")
rect1.draw()

rect2 = Rectangle()
rect2.set_width(50)
rect2.set_height(150)
rect2.set_color("yellow")
rect2.draw()
rect2.set_x(300)
rect2.set_y(100)

ov1 = Oval()
ov1.set_width(200)
ov1.set_height(100)
ov1.set_color("black")
ov1.set_x(200)
ov1.draw()

ov2 = Oval()
ov2.randomize()
ov2.draw()

tri = Triangle(5, 5, 100, 200)
tri.set_x(350)
tri.set_color("red")
tri.draw()

paper.display()
