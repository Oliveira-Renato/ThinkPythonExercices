#2. Suppose the cover price of a book is **$24.95, but bookstores get a **40% discount. Shipping costs **$3 for the 
#  first copy and **75 cents for each additional copy. What is the total wholesale cost for **60 copies?

cover_price = 24.95
bkstore_dis = cover_price - (cover_price * 40)/100 
ship_cost = 3 #only for the first copy
ship_cost_normal = 0.75 
copies = 60
ship_calc =(ship_cost_normal * (copies - 1)) + ship_cost #charge 3 only one time
books_purchase = bkstore_dis * copies
whole_sale = books_purchase + ship_calc #cost of the total purchase


print('The total wholesale cost ${:.2f}'.format(whole_sale))
