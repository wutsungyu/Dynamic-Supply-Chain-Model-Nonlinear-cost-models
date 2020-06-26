#   Dynamic Supply Chain Model Nonlinear cost model <br>
資料來源 : [kaggle -- Credit Card Fraud Detection](https://www.kaggle.com/mlg-ulb/creditcardfraud)


## :black_nib: Why need Nonlinear cost model ?(Background and Motivation) <br>

In the supply chain, there are often the following costs

1.material costs  
2.transportation costs from suppliers to facilities  
3.material inventory costs  
4.inventory costs of products in facilities  
5.transportation costs from facilities to warehouses  
6.inventory costs of products in warehouses  
7.transportation costs from warehouses to customers  


These costs are often assumed to be linear in the SCM model, as shown in the following figure:

圖片 : [kaggle -- Credit Card Fraud Detection](https://www.kaggle.com/mlg-ulb/creditcardfraud)

The horizontal axis is the order quantity, and the vertical axis is the unit cost. It can be seen from the above figure that regardless of the order quantity, the unit cost is a fixed value. Obviously, this assumption is very unreasonable in real life.

In real life, we have different pricing strategies for different suppliers and different products. In addition, there will be quantity discounts. Generally, the more purchases, the greater the price discounts, to encourage customers to increase purchases, so we have to use nonlinear cost model to calculate various costs, it will be more reasonable.

## :black_nib: What types of Nonlinear cost model ?(Methodology) <br>

Here the purchase quantity will change from intput data to variable

Different types of cost will have different cost models. Generally, the common Nonlinear cost models have the following three types:

* Nonlinear cost model 1

The original purchase cost is 𝑝1. Then, the cost drops gradually with the increase of purchasing quantities and remain constant at 𝑝2 while the quantity reaches 𝑞1.

圖片 : [kaggle -- Credit Card Fraud Detection](https://www.kaggle.com/mlg-ulb/creditcardfraud)

The purchase cost under the linear model is p (unit cost) X q (quantity)

But in this example, the purchase cost p (unit cost) has different prices under different quantities, so it has become variable, so here req is used to represent p (unit cost)

The unit cost (req) restriction formula at this time is as follows:

圖片 : [kaggle -- Credit Card Fraud Detection](https://www.kaggle.com/mlg-ulb/creditcardfraud)

For example:
When the purchase quantity is q or q1 or 2*q1, the price of unit cost is as follows

圖片 : [kaggle -- Credit Card Fraud Detection](https://www.kaggle.com/mlg-ulb/creditcardfraud)

* Nonlinear cost model 2

This type of cost model is often used in Price-volume relationship is graded ,the relationship between costs and quantities is in fix-quantity-fix-price.  
(e.g. Customized class clothes  
if Within 10 pieces of clothes , 500 dollars per piece ； 10~50 pieces , 400 dollars per piece ； more than 50 pieces , 300 dollars per piece )


