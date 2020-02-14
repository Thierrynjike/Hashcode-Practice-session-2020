import pulp
with open('alsobig.txt','w') as fout:
    with open('e_also_big.txt') as f:
        num=f.readline().split( )
        M=int(num[0])
        N=int(num[1])
        line=f.readline().split( )
        ligne=[int(i) for i in line]
        problem=pulp.LpProblem('hashcode',pulp.LpMaximize)
        data=[None]*N
        outp=''
        for i in range(N):
            data[i]=pulp.LpVariable(f'x{i}',lowBound=0,upBound=1,cat='Binary')
        problem+=sum([i*j for i,j in zip(ligne,data)]), "som"
        problem+=sum([i*j for i,j in zip(ligne,data)])<=M
        problem.solve()
       # outp+=(f'{print(pulp.value(problem.objective))}\n')
        j=0
        for i in range(N):
            if(data[i].varValue!=0):
                outp+=(f'{i} ')
                j+=1
        outp=(f'{j}\n')+outp
    fout.write(outp)