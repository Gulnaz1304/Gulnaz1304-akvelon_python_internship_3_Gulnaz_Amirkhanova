# Gulnaz1304-akvelon_python_internship_3_Gulnaz_Amirkhanova
rest api can be tested in postman
# Create User. 
POST  localhost:8000/api/users/  "email" field is required and needs to be unique
# Edit User 
PATCH localhost:8000/api/users/user_id/, u can change any field
# Delete User  
DELETE localhost:8000/api/users/user_id/
# Create Transaction
POST localhost:8000/api/transactions/  need to fill "user" field with already created user id and "amount" with the transaction amount. It can be positive ot negative.
# Edit Transaction
PATCH localhost:8000/api/transactions/transaction_id/, u can change any field
# Delete Transaction
DELETE localhost:8000/api/transactions/transaction_id/
# Ability to view all user’s payments
POST localhost:8000/api/transactions/all_transactions/ you need to send field named "user" with the id of User whose all transactions you want to get 
# Ability to view sum of income/outcome grouped by dates
POST localhost:8000/api/transactions/transaction_sum_of_date/ required fields are "user" with user id and "date" with the date 
# filter methods for users
filter_users_by_transaction_date(date requiered), filter_users_by_transaction_type(you need to send field "type" filled by "in" or "out").
# filtering and ordering methods for transactions
filter_transactions_by_date (date is requiered), filter_transactions_by_type(you need to send field "type" filled by "in" or "out"), order_transactions_by_date (get), order_transactions_by_amount(get)
