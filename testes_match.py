#este script so roda em python3.10 pra cima

def print_ponto(ponto=(0,0)):
    match ponto:
        case (0, 0):
            print("Origin")
        case (0, y):
            print(f"Y={y}")
        case (x, 0):
            print(f"X={x}")
        case (x, y):
            print(f"X={x}, Y={y}")
        case _:
            raise ValueError("Not a point")

print_ponto(ponto=(1,2))

#################################################

class Point:
    x: int
    y: int
    def __init__(self,x=0,y=0) -> None:
        self.x = x
        self.y = y

def where_is(point):
    match point:
        case Point(x=0, y=0):
            print("Origin")
        case Point(x=0, y=y):
            print(f"Y={y}")
        case Point(x=x, y=0):
            print(f"X={x}")
        case Point():
            print("Somewhere else")
        case _:
            print("Not a point")

where_is(Point(x=0,y=0))
where_is(Point(x=0,y=1))
where_is(Point(x=1,y=0))
where_is(Point(x=1,y=1))

#################################################

def where_is2(points):
    match points:
        case []:
            print("No points")
        case [Point(x=0, y=0)]:
            print("The origin")
        case [Point(x=x, y=y)]:
            print(f"Single point {x}, {y}")
        case [Point(x=0, y=y1), Point(x=0, y=y2)]:
            print(f"Two on the Y axis at {y1}, {y2}")
        case _:
            print("Something else")
            
where_is2([Point(x=0, y=0), Point(x=0,y=1)])
where_is2(Point(x=1,y=0))
where_is2(Point(x=1,y=1))

#####################################################

def where_is3(point):
    match point:
        case Point(x=x, y=y) if x == y:
            print(f"Y=X at {x}")
        case Point(x=x, y=y):
            print(f"Not on the diagonal")

where_is3(Point(x=1,y=0))
where_is3(Point(x=1,y=1))
where_is3(Point(x=1,y=2))
where_is3(Point(x=2,y=2))