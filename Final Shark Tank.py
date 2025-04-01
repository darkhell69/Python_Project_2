#!/usr/bin/env python
# coding: utf-8

# # Shark Tank India
# ---

# ### About
# Shark Tank India is an Indian Hindi-language business reality television series that airs on Sony Entertainment Television. The show is the Indian franchise of the American show Shark Tank. It shows entrepreneurs making business presentations to a panel of investors or sharks, who decide whether to invest in their company. This data is about the  first season of Shark Tank India premiered on 20 December 2021, and concluded on 4 February 2022

# ## Importing Required Modules 
# 1. importing numpy for mathematical operation on arrays and dataframe.
# 2. importing pandas for reading data and data manipualtion.
# 3. importing matplotlib and seaborn to show the insights and  visualization from the dataset.
# 3. importing warnings for Warning messages that are typically issued in dataframe where it is useful to alert the user of some condition in a program, where that condition (normally) doesn t warrant raising an exception and terminating the program.

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")


# In[2]:


sns.set(style = 'darkgrid')


# In[5]:


pd.set_option('display.max_columns',None)


# ## Reading Dataset and Checking the NaN Values , Data Types , and Statistical Analysis
# 
# 1. Since data is in form of excel file we have to use pandas read_excel to load the data
# 2. After loading it is important to check the complete information of data as it can indication many of the hidden infomation such as null values in a column or a row
# 3. Check whether any null values are there or not. if it is present then following can be done,
#     1. Filling NaN values with mean, median and mode using fillna() method
# 4. Describe data --> which can give statistical analysis

# In[6]:


df=pd.read_csv('Shark Tank India Dataset.csv')


# In[7]:


df


# In[41]:


(50.0/5.0)*100


# In[42]:


df.shape


# In[43]:


df.info()


# In[44]:


df.isnull().sum()


# In[45]:


df.describe()


# # Exploratory Data Analysis (EDA)

# ## How many deals done in the whole season

# In[14]:


done=df[df['deal']==1].count()[0]
print('Succesfull deals....',done)
not_done=df[df['deal']==0].count()[0]
print('Rejected deals....',not_done)


# In[15]:


deal=df['deal'].value_counts().values[0]
no_deal=df['deal'].value_counts().values[1]


# In[9]:


df['deal'].value_counts()


# In[17]:


v=df['deal'].value_counts().values
i=df['deal'].value_counts().index


# In[18]:


plt.pie(v,labels=i,autopct='%.2f%%');


# In[19]:


print('hello')


# In[20]:


df['deal'].value_counts().values[0]


# In[21]:


df['deal'].value_counts(normalize=True)*100


# In[22]:


d=df['deal'].value_counts().values[0]
nd=df['deal'].value_counts().values[1]
print('Succesfull deals....',d)
print('UnSuccesfull deals....',nd)


# In[23]:


df['deal'].value_counts().plot(autopct='%.2f%%',kind='pie')


# ### Deals percentages

# ##  Most Dealing Episode

# In[24]:


best_episodes=df.groupby(['episode_number'])['deal'].sum().sort_values(ascending=False).reset_index()
best_episodes


# In[ ]:


df['episode_number'].value_counts()


# In[25]:


sns.catplot(x = 'deal', y = 'episode_number',kind='swarm',hue='deal', data = df)


# ## Most Expensive dealing Episodes

# In[26]:


A=df.groupby(df['episode_number'])['deal_amount'].sum().sort_values(ascending=False).reset_index()#.head(10)
A


# In[27]:


plt.figure(figsize=(10,6),dpi=200)
plt.bar(A['episode_number'],A['deal_amount'])
plt.xticks(A['episode_number'],rotation=90,fontsize=8)
plt.show()


# ##  All Sharks in

# In[14]:


df[df['total_sharks_invested']==5]


# In[30]:


df['total_sharks_invested'].value_counts()


# In[31]:


plt.figure(figsize=(10,6))
plt.title('Maximum Sharks in')
plt.bar(df['episode_number'],df['total_sharks_invested'])
plt.xticks(df['episode_number'].unique(),rotation=30);


# In[ ]:


df[df['total_sharks_invested']==5]


# In[ ]:


df.columns


# ## No Bargain Deal

# In[35]:


df[(df['pitcher_ask_amount']==df['deal_amount']) & (df['ask_equity']==df['deal_equity'])]


# ## No of Sharks invested with respect to Business

# In[46]:


df['total_sharks_invested'].value_counts()


# In[47]:


plt.figure(figsize =(20, 6))
sns.countplot(x=df['total_sharks_invested'])
plt.title('Number of Sharks invested', fontsize = 15)
plt.show()


# In[48]:


df.head(1)


# ### Created a function that show the Equity and Amount per shark

# In[52]:


def sharks(data):
    list= ['anupam_deal','aman_deal','namita_deal','vineeta_deal','peyush_deal','ghazal_deal','ashneer_deal']
    for i in list:
        deal = data[['amount_per_shark','equity_per_shark']][data[i]==1]
#         print("{} deals with {}".format(len(deal),i[:-5]))
        print('\n',len(deal),'deals with',i[:-5])
        print(deal)
    


# In[ ]:


len(df[(df['ashneer_deal']==1) & (df['anupam_deal']==1)][['amount_per_shark','equity_per_shark']])
# len(df[(df['ashneer_deal']==1) & (df['aman_deal']==1)][['amount_per_shark','equity_per_shark']])


# In[ ]:


ash_grover[['amount_per_shark','equity_per_shark']][ash_grover['anupam_deal']==1]


# In[ ]:


# print(ash_grover[['amount_per_shark','equity_per_shark']][ash_grover['anupam_deal']==1])


# In[ ]:


ash_grover


# # Ashneer Deals

# In[18]:


ash_grover = df[df['ashneer_deal']==1]
ash_grover


# In[53]:


sharks(ash_grover)


# In[ ]:


df


# In[54]:


amt=ash_grover['amount_per_shark'].sum()
print("Total amount invested on shark tank by Ashneer",amt,"lakhs")


# In[55]:


eqt=ash_grover['equity_per_shark'].sum()
print("Total equity buy on shark tank by Ashneer",eqt,'%')


# In[56]:


eqt = df.groupby('ashneer_deal')['equity_per_shark'].sum()[1]
amt = df.groupby('ashneer_deal')['amount_per_shark'].sum()[1]
print("Total equity buy on shark tank by Ashneer",eqt,'%')
print("Total amount invested on shark tank by Ashneer",amt,"lakhs")


# In[ ]:


ash_grover['amount_per_shark'].sum()


# In[ ]:


ash_grover['amount_per_shark'].max()


# In[ ]:


# ash_grover[ash_grover['amount_per_shark']==70.0]


# In[ ]:


ash_grover.sort_values(by='amount_per_shark',ascending=False).head(1)


# In[ ]:


ash_grover['amount_per_shark'].max()


# In[57]:


ash_grover[ash_grover['amount_per_shark']==ash_grover['amount_per_shark'].max()]


# In[58]:


ash_grover[ash_grover['equity_per_shark']==ash_grover['equity_per_shark'].max()]


# # Anupam Deals

# In[59]:


anupam = df[df['anupam_deal']==1]
anupam


# In[60]:


sharks(anupam)


# In[61]:


eqt = df.groupby('anupam_deal')['equity_per_shark'].sum()[1]
amt = df.groupby('anupam_deal')['amount_per_shark'].sum()[1]
print("Total equity buy on shark tank by Anupam",eqt,'%')
print("Total amount invested on shark tank by Anupam",amt,"lakhs")


# In[ ]:


anupam['amount_per_shark'].sum()


# In[ ]:


anupam['equity_per_shark'].sum()


# In[62]:


anupam[anupam['amount_per_shark']==anupam['amount_per_shark'].max()]


# In[64]:


anupam[anupam['equity_per_shark']==anupam['equity_per_shark'].max()]


# # Aman Deals

# In[65]:


aman = df[df['aman_deal']==1]
aman


# In[66]:


sharks(aman)


# In[67]:


eqt = df.groupby('aman_deal')['equity_per_shark'].sum()[1]
amt = df.groupby('aman_deal')['amount_per_shark'].sum()[1]
print("Total equity buy on shark tank by Aman",eqt,'%')
print("Total amount invested on shark tank by Aman",amt,"lakhs")


# In[ ]:


aman['amount_per_shark'].sum()


# In[ ]:


aman['equity_per_shark'].sum()


# In[68]:


aman[aman['amount_per_shark']==aman['amount_per_shark'].max()]


# In[69]:


aman[aman['deal_equity']==aman['deal_equity'].max()]


# # Namita Deals

# In[70]:


namita = df[df['namita_deal']==1]
namita


# In[71]:


sharks(namita)


# In[72]:


eqt = df.groupby('namita_deal')['equity_per_shark'].sum()[1]
amt = df.groupby('namita_deal')['amount_per_shark'].sum()[1]
print("Total equity buy on shark tank by namita",eqt,'%')
print("Total amount invested on shark tank by namita",amt,"lakhs")


# In[73]:


namita[namita['amount_per_shark']==namita['amount_per_shark'].max()]


# In[74]:


namita[namita['equity_per_shark']==namita['equity_per_shark'].max()]


# # Vineeta Deals

# In[75]:


vineeta = df[df['vineeta_deal']==1]
vineeta


# In[76]:


vineeta['amount_per_shark'].sum()


# In[77]:


vineeta['equity_per_shark'].sum()


# In[78]:


sharks(vineeta)


# In[79]:


eqt = df.groupby('vineeta_deal')['equity_per_shark'].sum()[1]
amt = df.groupby('vineeta_deal')['amount_per_shark'].sum()[1]
print("Total equity buy on shark tank by vineeta",eqt,'%')
print("Total amount invested on shark tank by vineeta",amt,"lakhs")


# In[80]:


vineeta[vineeta['amount_per_shark']==vineeta['amount_per_shark'].max()]


# In[82]:


vineeta[vineeta['deal_equity']==vineeta['deal_equity'].max()]


# # Peyush Deals

# In[83]:


peyush= df[df['peyush_deal']==1]
peyush


# In[ ]:


peyush['amount_per_shark'].sum()


# In[ ]:


peyush['equity_per_shark'].sum()


# In[ ]:


sharks(peyush)


# In[84]:


eqt = df.groupby('peyush_deal')['equity_per_shark'].sum()[1]
amt = df.groupby('peyush_deal')['amount_per_shark'].sum()[1]
print("Total equity buy on shark tank by peyush",eqt,'%')
print("Total amount invested on shark tank by peyush",amt,"lakhs")


# In[85]:


peyush[peyush['amount_per_shark']==peyush['amount_per_shark'].max()]


# In[86]:


peyush[peyush['deal_equity']==peyush['deal_equity'].max()]


# In[ ]:


peyush.sort_values(by='equity_per_shark',ascending=False)


# # Ghazal Deals

# In[87]:


ghazal=df[df['ghazal_deal']==1]
ghazal


# In[ ]:


ghazal['amount_per_shark'].sum()


# In[ ]:


ghazal['equity_per_shark'].sum()


# In[ ]:


sharks(ghazal)


# In[88]:


eqt = df.groupby('ghazal_deal')['equity_per_shark'].sum()[1]
amt = df.groupby('ghazal_deal')['amount_per_shark'].sum()[1]
print("Total equity buy on shark tank by ghazal",eqt,'%')
print("Total amount invested on shark tank by ghazal",amt,"lakhs")


# In[89]:


ghazal[ghazal['amount_per_shark']==ghazal['amount_per_shark'].max()]


# In[90]:


ghazal[ghazal['deal_equity']==ghazal['deal_equity'].max()]


# In[ ]:


df.head(5)


# ## Number of Sharks Teamedup

# In[91]:


# Part-1
q=df[df['total_sharks_invested']>1]

q['total_sharks_invested'].value_counts()


# In[95]:


# Part-2
teamup=df[df['total_sharks_invested']>1]
teamup
# plt.figure(figsize=(7,7))
# plt.hist(teamup.total_sharks_invested)
# plt.yticks(q['total_sharks_invested'].value_counts().values)
# plt.title('visualization of number of Sharks teamedup')
# plt.xlabel('Number of Sharks')
# plt.ylabel('Number of Investments');


# In[99]:


# part-4
plt.figure(dpi=200)
plt.scatter(teamup['brand_name'],teamup['total_sharks_invested'],s=8);

plt.xticks(rotation=90,fontsize=6)

plt.show()


# In[ ]:


df.groupby(['ashneer_deal'])['amount_per_shark'].sum()


# In[ ]:


o=[1,2,3,45]
c=0
for i in o:
    c+=i
print(c)


# In[ ]:


df.episode_number


# ##  Total Amount invested by Sharks in Different Companies

# In[101]:


[am6,c,a]
['cc']


# In[ ]:


L=[494,887,223]
t=ash_grover['amount_per_shark'].sum()
t2=aman['amount_per_shark'].sum()
print(t)
print(t2)


# In[ ]:


e=[1,2,3,4,]


# In[103]:


a=df[df['ashneer_deal']==1]
aa=list(a['amount_per_shark'])
aa
t=0

for i in aa:
    t+=i
    

b=df[df['anupam_deal']==1]
ba=list(b.amount_per_shark)
u=0
for i in ba:
    u+=i

c=df[df['aman_deal']==1]
ca=list(c.amount_per_shark)
v=0
for i in ca:
    v+=i

d=df[df['namita_deal']==1]
da=list(d.amount_per_shark)
w=0
for i in da:
    w+=i
    
e=df[df['vineeta_deal']==1]
ea=list(e.amount_per_shark)
x=0
for i in ea:
    x+=i
    
f=df[df['peyush_deal']==1]
fa=list(f.amount_per_shark)
y=0
for i in fa:
    y+=i
    
g=df[df['ghazal_deal']==1]
ga=list(g.amount_per_shark)
z=0
for i in ga:
    z+=i


# In[ ]:


t=ash_grover['amount_per_shark'].sum()
anump['']


# In[ ]:


t


# In[ ]:


peyush


# In[104]:


l1=['Asheer','anupam','aman','namita','vineeta','peyush','ghazal']
l2=[t,u,v,w,x,y,z]
plt.bar(l1,l2);


# In[ ]:


sns.barplot(l1,l2);


# In[ ]:


# L=[1,2,3,4,5,67,7,8,89,9]
# fo


# In[ ]:


print('total amount invested by ashneer',t)


# In[ ]:


# ash=df[df['ashneer_deal']==1]
# ash['amount_per_shark'].sum()


# In[ ]:





# In[ ]:


# print(t,u,v,w,x,y,z)
# L=[494.33333333, 533.83360253, 887.5000166929999, 648.333602533, 328.3333333300001, 719.666919163, 130.0002525]
# print(sum(L))


# In[ ]:


# (494.33333333/3742.0010600789997)*100


# In[ ]:





# ## Total equity owned by sharks in diffrent Companies

# In[105]:


h=df[df['ashneer_deal']==1]
he=list(h.equity_per_shark)
a=0
for i in he:
    a+=i

i=df[df['anupam_deal']==1]
ie=list(i.equity_per_shark)
b=0
for y in ie:
    b+=y
    
j=df[df['aman_deal']==1]
je=list(j.equity_per_shark)
c=0
for i in je:
    c+=i
    
k=df[df['namita_deal']==1]
ke=list(k.equity_per_shark)
d=0
for i in ke:
    d+=i
    
l=df[df['vineeta_deal']==1]
le=list(l.equity_per_shark)
e=0
for i in le:
    e+=i
    
m=df[df['peyush_deal']==1]
me=list(m.equity_per_shark)
f=0
for i in me:
    f+=i
    
n=df[df['ghazal_deal']==1]
ne=list(n.equity_per_shark)
g=0
for i in ne:
    g+=i


# In[ ]:


o=df[df['peyush_deal']==1]
o['equity_per_shark'].sum()


# In[ ]:


o=df[df['peyush_deal']==1]
o['equity_per_shark'].sum()


# In[ ]:


df.head(10)


# In[ ]:


peyush.sort_values(by='equity_per_shark',ascending=False)


# In[106]:


l1=['Asheer','anupam','aman','namita','vineeta','peyush','ghazal']
l2=[a,b,c,d,e,f,g]
plt.bar(l1,l2);


# In[ ]:


xyz=df[df['ashneer_deal']==1]
xyz['equity_per_shark'].sum()


# In[ ]:


df['anupam_deal'].sum()


# In[ ]:


df.head(2)


# ##  which Shark invested in most companies

# In[107]:


D=[]
list = ['anupam_deal','aman_deal','namita_deal','vineeta_deal','peyush_deal','ghazal_deal','ashneer_deal']
for i in list:
    deal = df[i].sum()
    D.append(deal)
    print(i,"deals with",deal,"companies" )


# ## Insights 8: Which Shark present at the time of Company

# In[109]:


p=[]
list = ['anupam_present','aman_present','namita_present','vineeta_present','peyush_present','ghazal_present','ashneer_present']
for i in list:
    pres = df[i].sum()
    p.append(pres)
    print(i,"present in front of",pres,"companies" )


# In[110]:


plt.bar(list,p)
plt.xticks(rotation=90);


# In[111]:


ashneer=(df['ashneer_present'])
anupam=(df['anupam_present'])
aman=(df['aman_present'])
namita=(df['namita_present'])
vineeta=(df['vineeta_present'])
peyush=(df['peyush_present'])
ghazal=(df['ghazal_present'])


xx=pd.DataFrame({'Sharks':['ASHNEER','ANUPAM','AMAN','NAMITA','VINEETA','PEYUSH','GHAZAL'],
              'Number_of_appearance':[sum(ashneer),sum(anupam),sum(aman),sum(namita),sum(vineeta),sum(peyush),sum(ghazal)]})


# In[112]:


sum(ashneer)


# In[113]:


xx


# In[114]:


plt.figure(figsize=(7,7))

sns.barplot(x='Sharks',y='Number_of_appearance',data=xx);


# In[ ]:





# # Amount invested by the shark According to the ask valuation

# In[ ]:


fig, ax =plt.subplots(figsize =(30, 10))
sns.barplot(data = df, y='ask_valuation', x='amount_per_shark',ci=None)
plt.show()


# In[ ]:


d={}
m=int(input('how many columns'))
for k in range(m):
    x=input('enter x ')
    j=0
    n=len(x)
    u=0
    for i in range(n):
        d[u]=[x[j]]
        u+=1
        
    d
    a=pd.Series(d)
    z=pd.DataFrame(a)


# In[ ]:


z


# In[ ]:


D={}
L=[]

i=0
for i in range(2):
    x=input('enter ').split(' ')
    
    D[i]=x
    i+=1
pd.DataFrame(D)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




