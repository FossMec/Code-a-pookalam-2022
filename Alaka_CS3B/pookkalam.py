#outer-section

def outer_layer(w,h,f,s,n):
    r = rectangle(w=w,h=h,fill=f,stroke=s) | rotate(n)
    r1 = r | repeat(12, rotate(30))
    show(r1)

def dec_small_circle(r,x,f,n):
    c = circle(r=r,fill=f,stroke='none',x=x,y=0) | rotate(n)
    c1 = c|repeat(12,rotate(30))
    show(c1)
    
c1 = circle(r=150,stroke='none',fill="#580000")
show(c1)
outer_layer(200,200,'#f89b23','none',0)
outer_layer(175,175,'#eee204','none',15)
outer_layer(140,140,'#e9f1fd','none',0)
dec_small_circle(5,135,'yellow',0)

#inner-section

def inner_circle(r,f,s):
    c2 = circle(r=r,fill=f,stroke=s)
    show(c2)
    
inner_circle(80,"#580000",'none')

outer_layer(100,100,'#f89b23','none',15)
outer_layer(87,87,'#eee204','none',0)
outer_layer(55,55,'#e9f1fd','none',15)

inner_circle(25,"#3f0000",'none')
inner_circle(10,'red','none')
inner_circle(5,'yellow','none')
inner_circle(2.5,'white','none')

dec_small_circle(2,15,'#f89b23',0)
dec_small_circle(3,70,'yellow',15)
