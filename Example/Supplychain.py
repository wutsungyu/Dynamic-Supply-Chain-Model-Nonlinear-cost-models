# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 17:43:10 2020

@author: wutsungyu
"""
import pandas as pd
import numpy as np
from pulp import*

def reest_name(df):
    df = df.reset_index()
    df.columns = [np.arange(0,df.shape[1])]
    return df

df=pd.read_excel('C:/Users/tsungyu/_______ORA/ORA_Assignment_02_2020/ORA_Assignment_02_Supplychain.xlsx',sheet_name=None)

''''--------------------------dataframe--------------------------'''

Mcost_tvp=df['Data'].iloc[:5,:-1].set_index('Mcost_tvp')
VF_Tcost_tvfp=df['VF_Tcost_tvfp'].iloc[:,:-1].set_index('VF_Tcost_tvfp')
Pcost_tfg=df['Pcost_tfg'].iloc[:,:-1].set_index('Pcost_tfg')
FM_Icost_tfp=df['FM_Icost_tfp'].iloc[:,:-1].set_index('FM_Icost_tfp')
FG_Icost_tfg=df['FG_Icost_tfg'].iloc[:,:-1].set_index('FG_Icost_tfg')
W_Icost_twg=df['W_Icost_twg'].iloc[:,:-1].set_index('W_Icost_twg')
FW_Tcost_tfwg=df['FW_Tcost_tfwg'].iloc[:,:-1].set_index('FW_Tcost_tfwg')
WC_Tcost_twcg=df['WC_Tcost_twcg'].iloc[:,:-1].set_index('WC_Tcost_twcg')

#BOM=df['Data'].iloc[6:7,:-4]
#BOM=reest_name(BOM)
BOMgp = pd.DataFrame({'BOMgp': ['p1','p2','p3'],'g1':[1,2,3]}).set_index('BOMgp')

#T_bomfg=df['Data'].iloc[8:9,:-5]
#T_bomfg=reest_name(T_bomfg)
T_bomfg = pd.DataFrame({'leadtime_T_bomfg': ['f1','f2'],'g1':[1,1]}).set_index('leadtime_T_bomfg')

#T_vf=df['Data'].iloc[9:11,:-5]
#T_vf=reest_name(T_vf)
T_vf = pd.DataFrame({'leadtime_Tvf': ['v1', 'v2'],'f1':[1,1],'f2':[1,1]}).set_index('leadtime_Tvf')

#T_fw=df['Data'].iloc[11:13,:-5]
#T_fw=reest_name(T_fw)
T_fw = pd.DataFrame({'leadtime_Tfw': ['f1', 'f2'],'w1':[1,1],'w2':[1,1]}).set_index('leadtime_Tfw')

#T_wc=df['Data'].iloc[13:15,:-4]
#T_wc=reest_name(T_wc)
T_wc = pd.DataFrame({'leadtime_T_wc': ['w1', 'w2'],'c1':[1,1],'c2':[1,1],'c3':[1,1]}).set_index('leadtime_T_wc')


LC_tcg=df['LC_tcg'].iloc[:,:-1].set_index('LC_tcg')
LW_twg_UpBound=df['LW_twg_UpBound'].iloc[:,:-1].set_index('LW_twg_UpBound')
R_tfg_UpBound=df['R_tfg_UpBound'].iloc[:,:-1].set_index('R_tfg_UpBound')
LV_tvp_UpBound=df['LV_tvp_UpBound'].iloc[:,:-1].set_index('LV_tvp_UpBound') #這應該是LV_tvp 不是Mcost

'''--------------------------decesion variable--------------------------'''
t=[1,2,3,4,5]
v=[1,2]
p=[1,2,3]
f=[1,2]
w=[1,2]
g=[1]
c=[1,2,3]


LVtvp = [(tt,vv,pp) for tt in t for vv in v for pp in p]
LVtvp = LpVariable.dicts("LVtvp_var",LVtvp,0,None,LpInteger)

LVtfp = [(tt,ff,pp) for tt in t for ff in f for pp in p]
LVtfp = LpVariable.dicts("LVtfp_var",LVtfp,0,None,LpInteger)

LVtfg = [(tt,ff,gg) for tt in t for ff in f for gg in g]
LVtfg = LpVariable.dicts("LVtfg_var",LVtfg,0,None,LpInteger)

LVtwg = [(tt,ww,gg) for tt in t for ww in w for gg in g]
LVtwg = LpVariable.dicts("LVtwg_var",LVtwg,0,None,LpInteger)

LVtcg = [(tt,cc,gg) for tt in t for cc in c for gg in g]
LVtcg = LpVariable.dicts("LVtcg_var",LVtcg,0,None,LpInteger)

Rtvfp = [(tt,vv,ff,pp) for tt in t for vv in v for ff in f for pp in p]
Rtvfp = LpVariable.dicts("Rtvfp_var",Rtvfp,0,None,LpInteger)

Rtfg = [(tt,ff,gg) for tt in t  for ff in f for gg in g]
Rtfg = LpVariable.dicts("Rtfg_var",Rtfg,0,None,LpInteger)

Rtfwg = [(tt,ff,ww,gg) for tt in t  for ff in f for ww in w for gg in g]
Rtfwg = LpVariable.dicts("Rtfwg_var",Rtfwg,0,None,LpInteger)

Rtwcg = [(tt,ww,cc,gg) for tt in t  for ww in w for cc in c for gg in g]
Rtwcg = LpVariable.dicts("Rtwcg_var",Rtwcg,0,None,LpInteger)

LF_tfp_df=df['Variable'].iloc[:,0:7].set_index('LF_tfp')
LF_tfg_df=df['Variable'].iloc[:,8:11].set_index('LF_tfg')
LW_twg_df=df['Variable'].iloc[:,12:15].set_index('LW_twg')

LF_tfp = [(tt,ff,pp) for tt in t  for ff in f for pp in p ]
LF_tfp = LpVariable.dicts("LF_tfp_var",LF_tfp,0,None,LpInteger)

for tt in t  :
    for ff in f :
        for pp in p:
            if tt==1:    
                LF_tfp[tt,ff,pp]=LF_tfp_df['LF_t'+str(ff)+str(pp)]['t'+str(tt)]


LF_tfg = [(tt,ff,gg) for tt in t  for ff in f for gg in g ]
LF_tfg = LpVariable.dicts("LF_tfg_var",LF_tfg,0,None,LpInteger)

for tt in t  :
    for ff in f :
        for gg in g:
            if tt==1:    
                LF_tfg[tt,ff,gg]=LF_tfg_df['LF_t'+str(ff)+str(gg)+'.1']['t'+str(tt)]

LW_twg = [(tt,ww,gg) for tt in t  for ww in w for gg in g ]
LW_twg = LpVariable.dicts("LW_twg_var",LW_twg,0,None,LpInteger)

for tt in t  :
    for ww in w :
        for gg in g:
            if tt==1:    
                LW_twg[tt,ww,gg]=LW_twg_df['LW_t'+str(ww)+str(gg)]['t'+str(tt)]

'''--------------------------建模--------------------------'''

problem = LpProblem('Total_Cost', LpMinimize) # Objective function

Mcost_X_LVtvp=[ LVtvp[t,v,p]* Mcost_tvp['Mcost_t'+str(v)+str(p)]['t'+str(t)] for (t,v,p) in LVtvp]
VF_Tcost_X_Rtvfp=[ Rtvfp[t,v,f,p]* VF_Tcost_tvfp[VF_Tcost_tvfp['Unnamed: 1']=='v'+str(v)]['VF_Tcost_tv'+str(f)+str(p)]['t'+str(t)] for (t,v,f,p) in Rtvfp]
Pcost_tfg_X_Rtfg=[ Rtfg[t,f,g]* Pcost_tfg['Pcost_t'+str(f)+str(g)]['t'+str(t)] for (t,f,g) in Rtfg]
FM_Icost_tfp_X_LF_tfp=[ LF_tfp[t,f,p]* FM_Icost_tfp['FM_Icost_t'+str(f)+str(p)]['t'+str(t)] for (t,f,p) in LF_tfp]
FG_Icost_tfg_X_LF_tfg=[LF_tfg[t,f,g]* FG_Icost_tfg['FG_Icost_t'+str(f)+str(g)]['t'+str(t)] for (t,f,g) in LF_tfg]
W_Icost_twg_X_LW_twg=[LW_twg[t,w,g]* W_Icost_twg['W_Icost_t'+str(w)+str(g)]['t'+str(t)] for (t,w,g) in LW_twg]
FW_Tcost_tfwg_X_Rtfwg=[Rtfwg[t,f,w,g]* FW_Tcost_tfwg[FW_Tcost_tfwg['Unnamed: 1']=='f'+str(f)]['FW_Tcost_tf'+str(w)+str(g)]['t'+str(t)] for (t,f,w,g) in Rtfwg]
WC_Tcost_twcg_X_Rtwcg=[Rtwcg[t,w,c,g]* WC_Tcost_twcg[WC_Tcost_twcg['Unnamed: 1']=='w'+str(w)]['WC_Tcost_tw'+str(c)+str(g)]['t'+str(t)] for (t,w,c,g) in Rtwcg]

'''----------目標----------'''

problem += lpSum(Mcost_X_LVtvp + VF_Tcost_X_Rtvfp + Pcost_tfg_X_Rtfg + FM_Icost_tfp_X_LF_tfp + FG_Icost_tfg_X_LF_tfg + W_Icost_twg_X_LW_twg + FW_Tcost_tfwg_X_Rtfwg + WC_Tcost_twcg_X_Rtwcg)

'''----------限制----------'''
for t2,v2,f2,p2 in Rtvfp :
#    print(f2)
    problem += lpSum(Rtvfp[t2,v2,ff,p2] for ff in f)==lpSum(LVtvp[t2,v2,p2])    #內部tt沒用到 

for t2,f2,p2 in LF_tfp:
#    print(t2,f2,p2)
    for gg in g:
#        print(t2,f2,p2,gg)
#        for vv in v:
            if t2 <=1:
                problem += lpSum(LF_tfp[t2,f2,p2]-BOMgp['g'+str(gg)]['p'+str(p2)]* Rtfg[t2,f2,gg]) == lpSum(LF_tfp[t2+1,f2,p2])
            elif t2 <=4:
                problem += lpSum(LF_tfp[t2,f2,p2]-BOMgp['g'+str(gg)]['p'+str(p2)]* Rtfg[t2,f2,gg]+[Rtvfp[t2-1,vv,f2,p2] for vv in v]) == lpSum(LF_tfp[t2+1,f2,p2])
           
for t2,f2,g2 in LF_tfg:
    if t2 <=1:
        problem += lpSum(LF_tfg[t2,f2,g2]-[Rtfwg[t2,f2,ww,g2] for ww in w]) == lpSum(LF_tfg[t2+1,f2,g2])
    elif t2 <=4:
        problem += lpSum(LF_tfg[t2,f2,g2]+Rtfg[t2-1,f2,g2]-[Rtfwg[t2,f2,ww,g2] for ww in w]) == lpSum(LF_tfg[t2+1,f2,g2])
   
for t2,w2,g2 in LW_twg:
    if t2 <=1:
        problem += lpSum(LW_twg[t2,w2,g2]-[Rtwcg[t2,w2,cc,g2] for cc in c]) == lpSum(LW_twg[t2+1,w2,g2])
    elif t2 <=4:
        problem += lpSum(LW_twg[t2,w2,g2]+[Rtfwg[t2-1,ff,w2,g2]for ff in f]-[Rtwcg[t2,w2,cc,g2] for cc in c]) == lpSum(LW_twg[t2+1,w2,g2])


for t2,c2,g2 in LVtcg : ##Rtwcg 用 LVtcg替代為了索引
    if t2 >1 and t2 <6: 
#        print( t2,c2,g2)
        problem += lpSum(Rtwcg[t2-1,ww,c2,g2] for ww in w)==lpSum(LC_tcg['LC_t'+str(c2)+str(g2)]['t'+str(t2)])    #內部tt沒用到 

'''----------非負限制----------'''

LW_twg_UpBound
R_tfg_UpBound
LV_tvp_UpBound

LW_twg
Rtfg
LVtvp

for (t,w,g) in LW_twg:
#    print((t,w,g))
    problem += lpSum(LW_twg[t,w,g]) <= lpSum(LW_twg_UpBound['LW_t'+str(w)+str(g)+'_UpBound']['t'+str(t)])

for (t,f,g) in Rtfg:
#    print((t,f,g))
    problem += lpSum(Rtfg[t,f,g]) <= lpSum(R_tfg_UpBound['R_t'+str(f)+str(g)+'_UpBound']['t'+str(t)])

for (t,v,p) in LVtvp:
#    print((t,f,g))
    problem += lpSum(LVtvp[t,v,p]) <= lpSum(LV_tvp_UpBound['LV_tvp_t'+str(v)+str(p)]['t'+str(t)])

problem.solve()
#problem.writeLP("WhiskasModel.lp")             #打印出来相关信息



print("Status:", LpStatus[problem.status])     #最优解
print('------------------------------------')

object_value=value(problem.objective)
print('object_value',object_value)

print('------------------------------------')
for v in problem.variables():
    print(v.name, "=", v.varValue)              #打印每个变量名字








































