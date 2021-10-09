"""Crypto Interview Assessment Module."""

import os

from dotenv import find_dotenv, load_dotenv


import crypto_api
from model.base import Base,engine,Session
from model.coin import Coin
from model.user import User
from model.order import Order
from model.current_price import CurrentPrice
from utils import convert_to_dictionary,get_user,calculate_portfolio,check_to_buy_coins
import datetime 
import time

load_dotenv(find_dotenv(raise_error_if_not_found=True))
sleep_interval = os.getenv("INTERVAL")

import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("storage/logs/app.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("app.py")

try:
    sleep_interval_int = int(sleep_interval)
except ValueError:
    logger.error('exception reading interval defaulting to an hour')
    sleep_interval_int=3600
# You can access the environment variables as such, and any variables from the .env file will be loaded in for you to use.
# os.getenv("DB_HOST")

# Start Here

#drop tables
#Base.metadata.drop_all(engine)

#create tables
#Base.metadata.create_all(engine)

#while loop for sleep interval
while True:
    session  = Session()
    now = datetime.datetime.now()

    #creating dummy user
    user = get_user(session,'tim','timuy@yahoo.com')
    session.add(user)

    coins_list = crypto_api.get_coins()

    #convert coins list to a dictionary for easier lookup for portfolio calculation
    coins_dict = convert_to_dictionary(coins_list)


    #check to make sure size of coins_list and slice if needed to get only three
    coins_to_buy_list = coins_list[:3] if len(coins_list) >3 else coins_list

    check_to_buy_coins(session,coins_to_buy_list,now,user,logger)
            

    #calculate user's portfolio
    #query database first
    user_orders = session.query(Order) \
        .filter(Order.user_id == user.id) \
        .all()    
            
    coin_inventory_dict = calculate_portfolio(user_orders,coins_dict)
        
    for key,value in coin_inventory_dict.items():
        
            logger.info('for coin: %s' %(key))
            user_inventory = value
            logger.info('total quantity is %s' %user_inventory.total_number_of_coins)
            
            for order in user_inventory.purchase_orders:
                logger.info('date purchased: %s quantity: %s profit percentage: %s purchase price: %s' %(order['date_purchased'],order['quantity'],order['profit_percentage'],order['purchase_price']))

    session.commit()
    session.close()

    time.sleep(sleep_interval_int)

   
