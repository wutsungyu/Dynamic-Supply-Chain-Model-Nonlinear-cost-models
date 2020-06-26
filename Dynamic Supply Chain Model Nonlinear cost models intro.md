#   Dynamic Supply Chain Model Nonlinear cost model <br>

資料來源 : [kaggle -- Credit Card Fraud Detection](https://www.kaggle.com/mlg-ulb/creditcardfraud)


## :black_nib: Why need Nonlinear cost model ?(Background and Motivation) <br>

In the supply chain, there are often the following costs

1. Material costs<br>
2. Transportation costs from suppliers to facilities<br>
3. Production cost paid to facilities<br>
4. Material inventory costs<br>
5. Inventory costs of products in facilities<br>
6. Transportation costs from facilities to warehouses<br>
7. Inventory costs of products in warehouses<br>
8. Transportation costs from warehouses to customers<br>


These costs are often assumed to be linear in the SCM model, as shown in the following figure:


<br>
<div align=center>
<img src="https://github.com/wutsungyu/Dynamic-Supply-Chain-Model-Nonlinear-cost-models-/blob/master/PIC/linear%20model.png"
width="500" height="350">
</div>
<br>

The horizontal axis is the order quantity, and the vertical axis is the unit cost. It can be seen from the above figure that regardless of the order quantity, the unit cost is a fixed value. Obviously, this assumption is very unreasonable in real life.

In real life, we have different pricing strategies for different suppliers and different products. In addition, there will be quantity discounts. Generally, the more purchases, the greater the price discounts, to encourage customers to increase purchases, so we have to use nonlinear cost model to calculate various costs, it will be more reasonable.

## :black_nib: What types of Nonlinear cost model ?(Methodology) <br>

Here the purchase quantity will change from intput data to variable

Different types of cost will have different cost models. Generally, the common Nonlinear cost models have the following three types:

* Nonlinear cost model 1

The original purchase cost is 𝑝1. Then, the cost drops gradually with the increase of purchasing quantities and remain constant at 𝑝2 while the quantity reaches 𝑞1.

<br>
<div align=center>
<img src="https://github.com/wutsungyu/Dynamic-Supply-Chain-Model-Nonlinear-cost-models-/blob/master/PIC/nonlinear%20model%201.png"
width="700" height="350">
</div>
<br>

The purchase cost under the linear model is p (unit cost) X q (quantity)

But in this example, the purchase cost p (unit cost) has different prices under different quantities, so it has become variable, so here req is used to represent p (unit cost)

The unit cost (req) restriction formula at this time is as follows:

<br>
<div align=center>
<img src="https://github.com/wutsungyu/Dynamic-Supply-Chain-Model-Nonlinear-cost-models-/blob/master/PIC/nonlinear%20model%2011.png"
width="200" height="80">
</div>
<br>

For example:
When the purchase quantity is q or q1 or 2*q1, the price of unit cost is as follows

<br>
<div align=center>
<img src="https://github.com/wutsungyu/Dynamic-Supply-Chain-Model-Nonlinear-cost-models-/blob/master/PIC/nonlinear%20model%2012.png"
width="400" height="350">
</div>
<br>

* Nonlinear cost model 2

This type of cost model is often used in Price-volume relationship is graded ,the relationship between costs and quantities is in fix-quantity-fix-price.  
(e.g. Customized class clothes  
if Within 10 pieces of clothes , 500 dollars per piece ； 10~50 pieces , 400 dollars per piece ； more than 50 pieces , 300 dollars per piece )

<br>
<div align=center>
<img src="https://github.com/wutsungyu/Dynamic-Supply-Chain-Model-Nonlinear-cost-models-/blob/master/PIC/nonlinear%20model%202.png"
width="700" height="350">
</div>
<br>

In this example, the above figure shows that 
when the purchase volume (q) is between 0 to q1, the unit cost is p1;   

when the purchase volume (q) is between q1 to q2, the unit cost is p2;  

when the purchase volume (q) is In q2 to q3, unit cost is p3


The purchase cost under Linear model is p (unit cost) * q (quantity)

But in this example, the purchase cost p (unit cost) has different prices under different quantities, so it has become variable, so here we use the function price(q) to represent p(unit cost)

The purchase cost function of model2 is as follows:

price(q) * q = (p1 u1 + p2 u2 + p3 u3) * q  

u1,u2,u3 € (0,1)  
u1 + u2 + u3 =1  

Expand price(q) * q  

price(q) * q = p1 u1 q+ p2 u2 q + p3 u3 q  

Where u1 q, u2 q, u3 q are variables multiplied by variables , therefore it is non-linear, replace them with z1, z2, z3 respectively  

price(q) X q = (p1 z1 + p2 z2 + p3 z3)  

Where u1 q (z1), u2 q (z2), u3 q (z3) can be expressed by the following inequalities:  

M(u1-1) ≤ q < q1 + M(1-u1)  
q1 + M(u2-1) ≤ q < q2 + M(1-u2)  
q2 + M(u3-1) ≤ q < q3 + M(1-u3)  
0 ≤ zi ≤ M * ui ,(i=1~3)   
q = z1+z2+z3  

Where M =Max(q1,q2,q3)  

u1,u2,u3€ (0,1)  
u1 + u2 + u3 =1  

if u1=1 (u2,u3=0) ； then 0 ≤ q < q1   
   q1-M ≤ q < q2+M  
   q2-M ≤ q < q3+M  
   q=z1  
   price(q)*q = p1*q  
if u2=1 (u1,u3=0) ； then q1 ≤ q < q2   
   q=z2  
   price(q)*q = p2*q  
if u3=1 (u1,u2=0) ； then q2 ≤ q < q3   
   q=z3  
   price(q)*q = p3*q  

* Nonlinear cost model 3

This type of cost model is often used in the production cost of the factory. The unit cost is higher when the product is first produced.  

With the increase in production, the unit cost of products will fall, but after a limit amount of production

The factory may not be able to load, so it may need to hire manpower or buy the machine, so the unit cost has increased

<br>
<div align=center>
<img src="https://github.com/wutsungyu/Dynamic-Supply-Chain-Model-Nonlinear-cost-models-/blob/master/PIC/nonlinear%20model%203.png"
width="700" height="350">
</div>
<br>

The purchase cost under Linear is p (unit cost) X q (quantity)
But in this example, the purchase cost p (unit cost) has different prices under different quantities, so it has become variable, so here we use the function price(q) to represent p(unit cost)

<br>
<div align=center>
<img src="https://github.com/wutsungyu/Dynamic-Supply-Chain-Model-Nonlinear-cost-models-/blob/master/PIC/nonlinear%20model%2031.png"
width="400" height="60">
</div>
<br>

## :black_nib: Comments <br>



## :black_nib: Reference <br>

<li>Handout of Operations Research Applications, ORA_03_Capacity_Scheduling_SCM_2020, Dr. Chia-Yen Lee</li>
<li>黎漢林, 供應鏈管理與決策, 儒林</li>

    














