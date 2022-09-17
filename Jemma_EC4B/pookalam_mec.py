# import joy Library in python to run this code

# canvas
r = rectangle(w=300, h=300, fill="lightgray", stroke="none")
show(r)


def mec():
    r2 = rectangle(x=0, y=-20, w=40, h=7, fill="tomato",
                   stroke="none") | repeat(3, translate(x=0, y=10))
    r3 = rectangle(x=27, y=-20, w=20, h=7, fill="red",
                   stroke="none") | repeat(3, translate(x=0, y=10)) | rotate(5)
    r4 = rectangle(x=-27, y=-20, w=20, h=7, fill="red",
                   stroke="none") | repeat(3, translate(x=0, y=10)) | rotate(-5)
    p11, p12, p13, p14 = point(
        x=-20, y=7), point(x=20, y=7), point(x=15, y=15), point(x=-15, y=15)
    t1 = polygon([p11, p12, p13, p14], fill="tomato", stroke="none")
    p21, p22, p23, p24 = point(
        x=-15, y=17), point(x=15, y=17), point(x=9, y=22), point(x=-9, y=22)
    t2 = polygon([p21, p22, p23, p24], fill="tomato", stroke="none")
    show(r2, r3, r4, t1, t2)


# outer
o1 = rectangle(x=0, y=0, h=13, w=300, fill="brown",
               stroke_width="0") | rotate(0)
o2 = rectangle(x=0, y=0, h=13, w=300, fill="red", stroke_width="0") | rotate(5)
o3 = rectangle(x=0, y=0, h=13, w=300, fill="darkorange",
               stroke_width="0") | rotate(10)
o4 = rectangle(x=0, y=0, h=13, w=300, fill="orange",
               stroke_width="0") | rotate(15)
o5 = rectangle(x=0, y=0, h=13, w=300, fill="#ffde05",
               stroke_width="0") | rotate(20)
o6 = rectangle(x=0, y=0, h=13, w=300, fill="#fffade",
               stroke_width="0") | rotate(25)
o = combine([o1+o2+o3+o4+o5+o6]) | repeat(7, rotate(30))
outer = o | repeat(2, scale(0.95) | rotate(5))
cir = circle(r=135, fill="darkgreen", stroke="none")
e0 = ellipse(x=15, y=0, w=80, h=270, fill="#f2f28c",
             stroke="none") | repeat(30, rotate(20)) | scale(0.92)
e1 = ellipse(x=0, y=0, w=90, h=270, fill="violet",
             stroke="none") | repeat(3, rotate(60))
e2 = ellipse(x=0, y=0, w=30, h=270, fill="magenta",
             stroke="none") | repeat(3, rotate(60))

# inner
r1 = rectangle(w=100, h=100, fill="tomato",
               stroke="none") | repeat(2, rotate(45))
r2 = rectangle(w=100, h=100, fill="orange", stroke="none") | repeat(
    2, rotate(45)) | rotate(22.5)
r3 = rectangle(w=82, h=82, fill="red", stroke="none") | repeat(
    2, rotate(45)) | rotate(22.5)
c11 = circle(r=48, fill="#f4f49a", stroke="none")

# middle
c = circle(r=71, fill="purple", stroke="none")
c1 = rectangle(w=125, b=175, fill="darkgreen",
               stroke="none") | repeat(25, rotate(125))
c21 = circle(x=30, y=40, r=45, fill="darkorange",
             stroke="none") | repeat(5, rotate(75))
c22 = circle(x=30, y=45, r=50, fill="orange",
             stroke="none") | repeat(5, rotate(75))
c23 = circle(x=30, y=50, r=55, fill="yellow",
             stroke="purple") | repeat(5, rotate(75))
c3 = circle(x=60, y=5, r=50, fill="purple", stroke="purple") | repeat(
    20, rotate(75)) | rotate(10)

show(outer, cir)
show(e0, e1, e2, c3, c23, c22, c21, c1, c)
show(r2, r1, r3, c11)
mec()
print("\n               Happy Onam")
