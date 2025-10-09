from __future__ import annotations
import math
from typing import Optional, Tuple, List

EPS = 1e-9

# ---------------------------
# Helper utilities
# ---------------------------

def almost_equal(a: float, b: float, eps: float = EPS) -> bool:
    return abs(a - b) <= eps

# ---------------------------
# Point
# ---------------------------
class Point:
    __slots__ = ("x", "y")

    def __init__(self, x: float, y: float):
        self.x = float(x)
        self.y = float(y)

    def distance_to(self, other: "Point") -> float:
        dx = self.x - other.x
        dy = self.y - other.y
        return math.hypot(dx, dy)

    def translate(self, dx: float, dy: float) -> "Point":
        return Point(self.x + dx, self.y + dy)

    def scale(self, sx: float, sy: Optional[float] = None, center: Optional["Point"] = None) -> "Point":
        if sy is None:
            sy = sx
        if center is None:
            cx, cy = 0.0, 0.0
        else:
            cx, cy = center.x, center.y
        nx = cx + sx * (self.x - cx)
        ny = cy + sy * (self.y - cy)
        return Point(nx, ny)

    def rotate(self, angle_degrees: float, center: Optional["Point"] = None) -> "Point":
        if center is None:
            cx, cy = 0.0, 0.0
        else:
            cx, cy = center.x, center.y
        theta = math.radians(angle_degrees)
        cos_t = math.cos(theta)
        sin_t = math.sin(theta)
        dx = self.x - cx
        dy = self.y - cy
        rx = cx + dx * cos_t - dy * sin_t
        ry = cy + dx * sin_t + dy * cos_t
        return Point(rx, ry)

    def as_tuple(self) -> Tuple[float, float]:
        return (self.x, self.y)

    def __repr__(self) -> str:
        return f"Point({self.x:.6f}, {self.y:.6f})"

# ---------------------------
# Line: Ax + By + C = 0
# ---------------------------
class Line:
    __slots__ = ("A", "B", "C")

    def __init__(self, A: float, B: float, C: float):
        self.A = float(A)
        self.B = float(B)
        self.C = float(C)

    @classmethod
    def from_points(cls, p1: Point, p2: Point) -> "Line":
        # (y2-y1)x - (x2-x1)y + (x2-x1)*y1 - (y2-y1)*x1 = 0
        A = p2.y - p1.y
        B = -(p2.x - p1.x)
        C = (p2.x - p1.x) * p1.y - (p2.y - p1.y) * p1.x
        return cls(A, B, C)

    def is_parallel(self, other: "Line") -> bool:
        # Two lines are parallel if their A,B are proportional
        return almost_equal(self.A * other.B, self.B * other.A)

    def is_coincident(self, other: "Line") -> bool:
        # Coincident if parallel and C ratios match as well
        return self.is_parallel(other) and almost_equal(self.A * other.C, self.C * other.A) and almost_equal(self.B * other.C, self.C * other.B)

    def evaluate(self, p: Point) -> float:
        return self.A * p.x + self.B * p.y + self.C

    def intersection_with_line(self, other: "Line") -> Optional[Point]:
        det = self.A * other.B - other.A * self.B
        if almost_equal(det, 0.0):
            # parallel or coincident
            return None
        x = (self.B * other.C - other.B * self.C) / det
        y = (other.A * self.C - self.A * other.C) / det
        return Point(x, y)

    def direction_vector(self) -> Tuple[float, float]:
        # a direction vector parallel to the line is (-B, A)
        return (-self.B, self.A)

    def normalize(self) -> "Line":
        # Normalize so that sqrt(A^2+B^2) == 1 and sign deterministic
        norm = math.hypot(self.A, self.B)
        if norm < EPS:
            return Line(self.A, self.B, self.C)
        A, B, C = self.A / norm, self.B / norm, self.C / norm
        # ensure A>0 or if A==0 then B>0 for determinism
        if A < -EPS or (almost_equal(A, 0.0) and B < -EPS):
            A, B, C = -A, -B, -C
        return Line(A, B, C)

    def translate(self, dx: float, dy: float) -> "Line":
        # Substitute x -> x - dx, y -> y - dy
        # A(x-dx) + B(y-dy) + C = 0 -> Ax + By + (C - A*dx - B*dy) = 0
        return Line(self.A, self.B, self.C - self.A * dx - self.B * dy)

    def __repr__(self) -> str:
        return f"Line({self.A:.6f}x + {self.B:.6f}y + {self.C:.6f} = 0)"

# ---------------------------
# Circle
# ---------------------------
class Circle:
    __slots__ = ("center", "r")

    def __init__(self, center: Point, r: float):
        self.center = center
        self.r = float(r)

    def translate(self, dx: float, dy: float) -> "Circle":
        return Circle(self.center.translate(dx, dy), self.r)

    def scale(self, s: float, center: Optional[Point] = None) -> "Circle":
        # scaling circle scales radius and center
        if center is None:
            center = Point(0, 0)
        new_center = self.center.scale(sx=s, center=center)
        return Circle(new_center, abs(self.r * s))

    def rotate(self, angle_degrees: float, center: Optional[Point] = None) -> "Circle":
        return Circle(self.center.rotate(angle_degrees, center=center), self.r)

    def __repr__(self) -> str:
        return f"Circle(center={self.center}, r={self.r:.6f})"

# ---------------------------
# Triangle
# ---------------------------
class Triangle:
    __slots__ = ("p1", "p2", "p3")

    def __init__(self, p1: Point, p2: Point, p3: Point):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def side_lengths(self) -> Tuple[float, float, float]:
        a = self.p2.distance_to(self.p3)  # opposite p1
        b = self.p1.distance_to(self.p3)  # opposite p2
        c = self.p1.distance_to(self.p2)  # opposite p3
        return (a, b, c)

    def perimeter(self) -> float:
        return sum(self.side_lengths())

    def area(self) -> float:
        # shoelace formula
        x1, y1 = self.p1.as_tuple()
        x2, y2 = self.p2.as_tuple()
        x3, y3 = self.p3.as_tuple()
        return abs((x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)) / 2.0)

    def triangle_type(self) -> str:
        a, b, c = self.side_lengths()
        sides = sorted([a, b, c])
        a_s, b_s, c_s = sides
        equilateral = almost_equal(a_s, b_s) and almost_equal(b_s, c_s)
        isosceles = almost_equal(a_s, b_s) or almost_equal(b_s, c_s) or almost_equal(a_s, c_s)
        right = almost_equal(a_s*a_s + b_s*b_s, c_s*c_s)
        if equilateral:
            return "equilateral"
        if right and isosceles:
            return "isosceles right"
        if right:
            return "right"
        if isosceles:
            return "isosceles"
        return "scalene"

    def translate(self, dx: float, dy: float) -> "Triangle":
        return Triangle(self.p1.translate(dx, dy), self.p2.translate(dx, dy), self.p3.translate(dx, dy))

    def scale(self, sx: float, sy: Optional[float] = None, center: Optional[Point] = None) -> "Triangle":
        return Triangle(self.p1.scale(sx, sy, center), self.p2.scale(sx, sy, center), self.p3.scale(sx, sy, center))

    def rotate(self, angle_degrees: float, center: Optional[Point] = None) -> "Triangle":
        return Triangle(self.p1.rotate(angle_degrees, center), self.p2.rotate(angle_degrees, center), self.p3.rotate(angle_degrees, center))

    def __repr__(self) -> str:
        return f"Triangle({self.p1}, {self.p2}, {self.p3})"

# ---------------------------
# Global computational functions
# ---------------------------

def intersect_lines(l1: Line, l2: Line) -> Tuple[str, Optional[Point]]:
    """
    Return (status, point)
    status in {"point", "parallel", "coincident"}
    """
    if l1.is_coincident(l2):
        return ("coincident", None)
    if l1.is_parallel(l2):
        return ("parallel", None)
    p = l1.intersection_with_line(l2)
    return ("point", p)


def intersect_circles(c1: Circle, c2: Circle) -> Tuple[str, List[Point]]:
    """
    Returns (status, points)
    status: "none", "one", "two", "coincident"
    """
    x0, y0 = c1.center.as_tuple()
    x1, y1 = c2.center.as_tuple()
    r0 = c1.r
    r1 = c2.r
    dx = x1 - x0
    dy = y1 - y0
    d = math.hypot(dx, dy)

    if almost_equal(d, 0.0) and almost_equal(r0, r1):
        return ("coincident", [])
    if d > r0 + r1 + EPS:
        return ("none", [])
    if d < abs(r0 - r1) - EPS:
        return ("none", [])

    # compute a = distance from center0 to the line connecting intersection points
    # a = (r0^2 - r1^2 + d^2) / (2d)
    a = (r0*r0 - r1*r1 + d*d) / (2.0 * d)
    # height from that line to intersection points
    h_sq = r0*r0 - a*a
    if h_sq < -EPS:
        return ("none", [])
    h = math.sqrt(max(0.0, h_sq))

    # midpoint
    xm = x0 + a * dx / d
    ym = y0 + a * dy / d

    if almost_equal(h, 0.0):
        return ("one", [Point(xm, ym)])

    rx = -dy * (h / d)
    ry = dx * (h / d)

    p1 = Point(xm + rx, ym + ry)
    p2 = Point(xm - rx, ym - ry)
    return ("two", [p1, p2])


def intersect_line_circle(line: Line, circle: Circle) -> Tuple[str, List[Point]]:
    """
    Return status and list of intersection points between an infinite line and a circle.
    status: "none", "one", "two"
    """
    # distance from center to line
    dist_num = abs(line.A * circle.center.x + line.B * circle.center.y + line.C)
    denom = math.hypot(line.A, line.B)
    if denom < EPS:
        return ("none", [])
    dist = dist_num / denom
    if dist > circle.r + EPS:
        return ("none", [])

    # find foot of perpendicular
    foot = find_foot_of_perpendicular(circle.center, line)

    if almost_equal(dist, circle.r):
        return ("one", [foot])

    # direction vector along the line
    dx, dy = line.direction_vector()
    dlen = math.hypot(dx, dy)
    ux, uy = dx / dlen, dy / dlen
    t = math.sqrt(max(0.0, circle.r*circle.r - dist*dist))
    p1 = Point(foot.x + ux * t, foot.y + uy * t)
    p2 = Point(foot.x - ux * t, foot.y - uy * t)
    return ("two", [p1, p2])


def perpendicular_line_from_point(point: Point, line: Line) -> Line:
    # line: Ax + By + C = 0 -> perpendicular has coefficients A' = B, B' = -A
    A_p = line.B
    B_p = -line.A
    C_p = -(A_p * point.x + B_p * point.y)
    return Line(A_p, B_p, C_p)


def find_foot_of_perpendicular(point: Point, line: Line) -> Point:
    perp = perpendicular_line_from_point(point, line)
    status, p = intersect_lines(line, perp)
    if status == "point" and p is not None:
        return p
    # degenerate: line parallel to perp? shouldn't happen
    # fallback: project using formula
    denom = line.A*line.A + line.B*line.B
    if denom < EPS:
        return Point(point.x, point.y)
    x = (line.B*(line.B*point.x - line.A*point.y) - line.A*line.C) / denom
    y = (line.A*(-line.B*point.x + line.A*point.y) - line.B*line.C) / denom
    return Point(x, y)


def verify_pythagorean_theorem(p1: Point, p2: Point, p3: Point) -> bool:
    d1 = p2.distance_to(p3)
    d2 = p1.distance_to(p3)
    d3 = p1.distance_to(p2)
    sides = sorted([d1, d2, d3])
    return almost_equal(sides[0]*sides[0] + sides[1]*sides[1], sides[2]*sides[2])

# ---------------------------
# Example usage in main
# ---------------------------
if __name__ == "__main__":
    print("Geometri Analitik & Aljabar Linier - contoh penggunaan")
    print("Prinsip: penggunaan titik, vektor, proyeksi, dan transformasi koordinat.\n")

    # Points and distance
    A = Point(0, 0)
    B = Point(3, 0)
    C = Point(3, 4)
    print("Points:", A, B, C)
    print("Distance A-B:", A.distance_to(B))
    print("Distance B-C:", B.distance_to(C))

    # Verify Pythagoras
    print("Triangle ABC is right?", verify_pythagorean_theorem(A, B, C))

    # Line from two points
    l1 = Line.from_points(A, C)
    l2 = Line.from_points(B, Point(0, 4))
    print("Line l1:", l1)
    print("Line l2:", l2)
    status, pt = intersect_lines(l1, l2)
    print("Intersection l1 & l2:", status, pt)

    # Perpendicular foot
    p = Point(1, 2)
    foot = find_foot_of_perpendicular(p, l1)
    print("Foot of perpendicular from", p, "to", l1, "is", foot)

    # Circle intersections
    c1 = Circle(Point(0, 0), 5)
    c2 = Circle(Point(8, 0), 5)
    s, pts = intersect_circles(c1, c2)
    print("Circle-Circle intersection status:", s, "points:", pts)

    # Line-circle intersection
    lin = Line.from_points(Point(-6, 0), Point(6, 0))
    circ = Circle(Point(0, 1), 2)
    s2, pts2 = intersect_line_circle(lin, circ)
    print("Line-Circle intersection:", s2, pts2)

    # Triangle
    tri = Triangle(A, B, C)
    print("Triangle sides:", tri.side_lengths())
    print("Perimeter:", tri.perimeter())
    print("Area:", tri.area())
    print("Type:", tri.triangle_type())

    # Transformations
    print("\nTransformations:")
    P = Point(1, 1)
    print("P original:", P)
    print("P translated by (2,3):", P.translate(2, 3))
    print("P scaled by 2 about origin:", P.scale(2))
    print("P rotated 90 deg about origin:", P.rotate(90))

    T = tri.rotate(90, center=Point(0,0))
    print("Triangle rotated 90 deg:", T)

    print("\nProgram Finished.\n")
    print("Note: floating-point precision enforced with EPS=", EPS)
