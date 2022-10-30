#outer
c = circle(r=150,fill="#2b2b2b")

sqr1=rectangle(h=210,w=210 ,fill="#cc1616")|rotate(0)| repeat(15,rotate(50))
sqr2=rectangle(h=195,w=195 ,fill="#ed6a0c")|rotate(15)| repeat(15,rotate(20))
sqr3=rectangle(h=180,w=180 ,fill="#fa9519")|rotate(0)| repeat(15,rotate(20))
sqr4=rectangle(h=166,w=166 ,fill="#fac105")|rotate(15)| repeat(15,rotate(20))
sqr5=rectangle(h=155,w=155 ,fill="#f5ed14")|rotate(0)| repeat(15,rotate(20))

show(c,sqr1,sqr2,sqr3,sqr4,sqr5)
#next circle

p1=point(x=0,y=95)
p2=point(x=-85,y=-45)
p3=point(x=85,y=-45)
l1=polygon([p1,p2,p3],fill="#ed6a0c")|repeat(3,rotate(40))
l2= l1|scale(0.95)|rotate(20)

c1=circle(r=95,fill="#f4fa9b")

cc1=circle(r=65,fill="#fff5e6")
cc2=circle(x=0,y=40,r=9,fill="#f4fa9b")|repeat(6,rotate(60))
e1=ellipse(x=20,y=0, w=90,h=40, fill="#008000")| repeat(6, rotate(60))
e2=ellipse(x=20,y=0, w=90,h=40, fill="#800080")|rotate(30)| repeat(6, rotate(60))
e3=ellipse(x=20,y=0, w=60,h=30, fill="#004080")| repeat(6, rotate(60))
sq1=rectangle(h=40,w=40, fill="#008000")|repeat(10, rotate(30))
c11=circle(r=30 ,fill="#fff5e6")
c12=circle(r=20 ,fill="#f5ed14")

show(c1,l1,l2,cc1,e1,e2,cc2,e3,c11,sq1,c12)
#inside
ee1=ellipse(x=0,y=4,w=10,h=20 ,fill="#cc1616")|repeat(6, rotate(60))#f51453
c13=circle(r=5,fill="green")
show(ee1,c13)

