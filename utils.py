

from model.coin import Coin
from model.user import User
from model.order import Order
from model.current_price import CurrentPrice
import crypto_api

def get_user(session,name,email):
    user = session.query(User) \
        .filter(User.name==name and User.email_address == email) \
        .all()
    return user[0] if user else User(name,email)
    
def get_coin(session,id,name,symbol):
    coin = session.query(Coin) \
        .filter(Coin.id==id) \
        .all()
    return coin[0] if coin else Coin(id,name,symbol)



def check_to_buy_coins(session, coins_to_buy_list,purchase_time,user,logger):
    for x in coins_to_buy_list:
        id = x.get('id')
        name = x.get('name')
        symbol = x.get('symbol')
        given_current_price = x.get('current_price')
        coin = get_coin(session,id,name,symbol)
        session.add(coin)
        current_price = CurrentPrice(coin,given_current_price,purchase_time)
        session.add(current_price)

        price_history_list = crypto_api.get_coin_price_history(id)

        average_price = get_average_price(price_history_list)
        #logger.info(given_current_price)
        #logger.info(average_price)
        if given_current_price < average_price:
            logger.info('buying for %s as current price: %s is less than average price: %s' %(id,given_current_price,average_price))
            quantity = 1
            results = crypto_api.submit_order(id,quantity,given_current_price)
            logger.info(results)
            order = Order(user, coin, results,purchase_time,quantity)
            session.add(order)
        else:
            logger.info('not buying for %s as current price: %s is not less than average price: %s' %(id,given_current_price,average_price))
        
def convert_to_dictionary(coins_list):
    coins_dict={}
    for item in coins_list:
        id = item.get('id')
        name = item.get('name')
        symbol = item.get('symbol')
        current_price = item.get('current_price')
        #if id does not exist, then do not put in list
        if id:
            coins_dict[id] = {'name':name,'symbol':symbol,'current_price':current_price}
    return coins_dict
        
def get_average_price(price_history_list):
    average = 0
    count=0
    sum = 0
    for price in price_history_list:
        price_per_day = price[1]
        count = count+1
        sum = sum + price_per_day
        
    average = sum/count
    return average

def calculate_portfolio(user_orders,coins_dict):
    from dto.user_inventory import UserInventory
    
    coin_inventory_dict = {}
    for order in user_orders:
        coin = order.coin
        quantity = order.quantity
        purchase_price = order.purchase_price
        date_purchased = order.date_purchased
        
        #check to make sure the coins dict has the coin in interest
        #only calculate if we have the price
        coin_price_dict = coins_dict.get(coin.id)
        if coin_price_dict:
            current_price  = coin_price_dict.get('current_price')
            
            if current_price:
                profit = current_price - purchase_price
                profit_percentage =  "{:.2f}%".format(profit/purchase_price *100)
        else:
            profit_percentage="0.00%"
            
        user_inventory = coin_inventory_dict[coin.id] if coin_inventory_dict.get(coin.id) else UserInventory(coin.id)
        user_inventory.add_to_inventory(quantity,date_purchased,purchase_price,profit_percentage)
        
        coin_inventory_dict[coin.id] = user_inventory
    
    return coin_inventory_dict
    