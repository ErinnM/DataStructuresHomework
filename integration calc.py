from graphics import *
import math

#set up window
win=GraphWin("Numerical Integration Calculator",800,800)
win.setBackground("lightsteelblue")
title=Text(Point(400,30),"Numerical Integration Calculator")
title.setSize(30)
title.setFace("times roman")
title.setStyle("bold italic")
title.draw(win)

#bounds entry boxes
def entryBox(x):
    x.setFill("ghostwhite")
    x.setFace("times roman")
    x.setSize(15)
    x.setTextColor("dimgray")
    x.draw(win)
    
lower=Entry(Point(300,140),10)
entryBox(lower)
low=Text(Point(220,140),"Lower Bound:")
low.setSize(10)
low.draw(win)
             
upper=Entry(Point(500,140),10)
entryBox(upper)
up=Text(Point(420,140),"Upper Bound:")
up.setSize(10)
up.draw(win)

#function entry box
fninput=Entry(Point(400,85),45)
entryBox(fninput)
fn1=Text(Point(85,70),"Function to")
fn1.setFace("times roman")
fn2=Text(Point(85,90),"integrate:")
fn2.setFace("times roman")
fn1.draw(win)
fn2.draw(win)

#methods
def box(x):
    x.setFill("lightslategray")
    x.setOutline("ghostwhite")
    x.draw(win)
def methodText(x):
    x.setStyle("bold italic")
    x.setSize(15)
    x.draw(win)    

trap=Rectangle(Point(120,200),Point(230,275))
box(trap)
traptext=Text(Point(175,237.5),"Trapezoid")
methodText(traptext)

rom=Rectangle(Point(120,310),Point(230,385))
box(rom)
romtext=Text(Point(175,347.5),"Romberg")
methodText(romtext)

gauss=Rectangle(Point(120,420),Point(230,495))
box(gauss)
gtext=Text(Point(175,457.5),"Gaussian")
methodText(gtext)

#output box
outbox=Rectangle(Point(448,255),Point(652,440))
box(outbox)
answerspot=Point(550,347.5)

#instructions for use
def ins(x):
    x.setSize(13)
    x.setStyle("italic")
    x.draw(win)
    
ins1=Text(Point(120,180),"Choose Method:")
ins(ins1)
ins2=Text(Point(120,550), "Instructions:")
ins(ins2)
ins3=Text(Point(400,570), "1. Enter your function using Python operators and the math module. For example, to integrate")
ins(ins3)
ins4=Text(Point(400,590),"2cos(x^2), enter 2*math.cos(x**2).")
ins(ins4)
ins5=Text(Point(400,610), "2. The upper bound must be greater than the lower bound. Also, use Python operators and the")
ins(ins5)
ins6=Text(Point(400,630),"math module to enter bounds if neccesary.")
ins(ins6)
ins7=Text(Point(400,650),"3. You will the the numpy module to use this calculator.                                                             ")
ins(ins7)
ins8=Text(Point(400,670),"4. Enter your function in terms of x. This calculator integrates functions of one varaible with      ")
ins(ins8)
ins9=Text(Point(400,690),"respect to x.")
ins(ins9)
          
#note on mathematical methods
def note(x):
    x.setSize(13)
    x.setFace("times roman")
    x.draw(win)
    
note1=Text(Point(400,740),"This calculator is implementing methods of numerical integration that approximate a given integral. The Trapezoid method is")
note2=Text(Point(400,760),"utlizing the recursive trapezoid rule, the Romberg method combines the Newton-Cotes method of Richardson extrapolation and ")
note3=Text(Point(400,780),"the trapezoidal rule, and the Gaussian method is using Gauss-Legendre quadrature with m=100 nodes.                         ")
note(note1)
note(note2)
note(note3)

def showAnswer():
    global out
    try: out.undraw()
    except NameError: pass
    out=Text(answerspot,answer)
    out.setFace("times roman")
    out.setStyle("bold")
    out.setSize(20)
    out.draw(win)

while True:  
    go=win.getMouse()
    if go.x>120 and go.x<230:
        #Trapezoid
        if go.y>200 and go.y<275:
            from trapezoid import *
            def f(x): return eval(fninput.getText())
            print(type(f))
            Iold=0.0
            a=eval(lower.getText())
            print(type(a))
            b=eval(upper.getText())
            print(type(b))
            for k in range(1,21):
                Inew=trapezoid(f,a,b,Iold,k)
                if (k>1) and (abs(Inew-Iold))<1.0e-6: break
                Iold=Inew
            print("Trapezoidal Integral =",Inew)
            answer=Inew
            showAnswer()

        #Romberg
        if go.y>310 and go.y<385:
            from romberg import *
            def f(x): return eval(fninput.getText())
            print(type(f))

            I,n=romberg(f,eval(lower.getText()),eval(upper.getText()))
            print("Romberg Integral =",I)
            answer=I
            showAnswer()

        #Gaussian
        if go.y>420 and go.y<495:
            pass
##        else:
