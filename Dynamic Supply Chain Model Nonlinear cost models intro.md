#   Dynamic Supply Chain Model Nonlinear cost model <br>
資料來源 : [kaggle -- Credit Card Fraud Detection](https://www.kaggle.com/mlg-ulb/creditcardfraud)


## :black_nib: Why need Nonlinear cost model ?(Background and Motivation) <br>

In the supply chain, there are often the following costs

1.material costs \ 
2.transportation costs from suppliers to facilities\
3.material inventory costs，
4.inventory costs of products in facilities，
5.transportation costs from facilities to warehouses，
6.inventory costs of products in warehouses，
7.transportation costs from warehouses to customers，


This function calculates the cost of using y_pred on y_true with cost-matrix cost-mat. It differ from traditional classification evaluation measures since measures such as accuracy asing the same cost to different errors, but that is not the real case in several real-world classification problems as they are example-dependent cost-sensitive in nature, where the costs due to misclassification vary between examples.
* Savings score.

This function calculates the savings cost of using y_pred on y_true with cost-matrix cost-mat, as the difference of y_pred and the cost_loss of a naive classification model.
