def Runge_Kutta(a=0, b=1, al=-1, N=5, inf=lambda x,y: x+y) ->list:
    x=[a]
    y=[al]
    h=(b-a)/N
    for i in range(0,N+1):
        K1 = h*inf(x[i], y[i])
        K2 = h*inf(x[i] + h/2, y[i] + K1/2)
        K3 = h*inf(x[i] + h/2, y[i] + K2/2)
        K4 = h*inf(x[i] + h, y[i] + K3)
        y += [y[i] + (K1 + K2*2 + K3*2 + K4)/6]
        x += [x[i] + h]
    
    return  y

def real_func_value(a, b, N, func):
    x=[a]
    y=[]
    h=(b-a)/N
    for i in range(0, N):
        x += [x[i] + h]
    for i in range(0,N+1):
        y += [func(x[i])]
    
    return y,x

if __name__=="__main__" :
    a=0 #start p
    b=0.2 # ebd p
    al=1 # f(a) = al
    inf=lambda x,y: x+y # infinitiv f(x,y) from real function F(x)
    func = lambda x: 1/(x+1)
    N=2
    runge_kutt=Runge_Kutta(a=a, b=b, al=al, N=N, inf=inf)
    for i in range(0,N+1):
        print("%.4f"%runge_kutt[i])
    print("\n")
    real_y,x_list = real_func_value(a=a, b=b, N=N, func=func)
    for i in range(0,N+1):pass
        #print("%.4f"%real_y[i])

    for i in range(0,N+1):pass
        #print("%.10f"%(abs(real_y[i] - runge_kutt[i])))