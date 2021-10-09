
class UserInventory(object):
    
    def __init__(self,coin_id):
        self.coin_id = coin_id
        self.total_number_of_coins = 0
        self.purchase_orders = list()
        
        
    def add_to_inventory(self,quantity,date_purchased,purchase_price,profit_percentage):
    
        self.total_number_of_coins = self.total_number_of_coins + quantity
        self.purchase_orders.append({'quantity':quantity,'date_purchased':date_purchased,'profit_percentage':profit_percentage,'purchase_price':purchase_price})