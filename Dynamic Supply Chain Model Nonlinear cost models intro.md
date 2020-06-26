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

