# Created using Joy Library

def cir(r,c):
    return circle(r=r,fill=c,stroke='none')
def sqr(side,c,rot,rep,reprot):
    m1 = rectangle(w=side,h=side,fill=c,stroke='none')
    m1 = m1 | rotate(rot) | repeat(rep,rotate(reprot))
    return m1

m = cir(150,'#0a0632')
m1 = sqr(141.4*1.5,'#ff1111',45,10,9)
m2 = sqr(197,'#ff6f00',22.5,10,9)
m3 = sqr(183,'yellow',45,10,9)
m4 = sqr(170,'white',22.5,10,9)

mm = [m,m1,m2,m3,m4]
mm = combine(mm)

def center():
    c = circle(r=100,fill='#ff6d00',stroke='red',stroke_width=3)
    color = 'white'
    c1 = rectangle(w=141.4,h=141.4,fill=color,stroke='none')
    c1 = c1 | rotate(45) | repeat(4,rotate(22.5))

    size = 120
    c2 = rectangle(w=size,h=size,fill='#ffff00',stroke='none')
    c2 = c2 | repeat(4,rotate(22.5))
    c2 = c2 | rotate(11.25)

    size = 100
    c3 = rectangle(w=size,h=size,fill='#ff6d00',stroke='none')
    c3 = c3 | repeat(4,rotate(22.5))

    size = 80
    c4 = rectangle(w=size,h=size,fill='red',stroke='none')
    c4 = c4 | repeat(4,rotate(22.5))
    c4 = c4 | rotate(11.25)

    c5 = circle(r=46,fill='#0B5F0B',stroke='none')

    size = 60
    c6 = rectangle(w=size,h=size,fill='white',stroke='none')
    c6 = c6 | repeat(3,rotate(30))

    size = 45
    c7 = rectangle(w=size,h=size,fill='#0a0632',stroke='none')
    c7 = c7 | repeat(3,rotate(30))

    c8 = circle(r=20,fill='yellow',stroke='none')
    c9 = circle(r=10,fill='#0B5F0B',stroke='none')

    ccc = combine([c,c1,c2,c3,c4,c5,c6,c7,c8,c9])
    
    return ccc

ccc = center()
ccc = ccc | scale(1.1)

show(mm,ccc)
