from py3cw.request import Py3CW
import logging
import time

### CONFIGURE 3C API KEY and BOT NAME HERE ###
API_KEY = ''
API_SECRET = ''
BOT_NAME = 'Block Party Testing'
DEBUG = 0


### DO NOT MODIFY ANYTHING BELOW HERE UNLESS YOU KNOW WHAT YOU ARE DOING ###

# configure logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# enable the 3C api module
p3cw = Py3CW(
    key=API_KEY, 
    secret=API_SECRET,
    request_options={
        'request_timeout': 10,
        'nr_of_retries': 3,
        'retry_status_codes': [502]
    }
)

# function to update the take profit value for a deal
def deal_update_tp(deal_id, deal_new_tp_level, deal_pair, deal_completed_so, deal_tp_level):
    logging.info('Deal %u on pair %s has %d completed safety orders and a take profit value of %s which is below the strategy recommended value.', 
                 deal_id, deal_pair, deal_completed_so, deal_tp_level)
    logging.info('Updating deal %u take profit to %s', deal_id, deal_new_tp_level)

    # sending request to update the deal
    error, data = p3cw.request(
        entity='deals',
        action='update_deal',
        action_id=str(deal_id),
        payload={
            "take_profit": deal_new_tp_level
        }
    )
    if (error):
        logging.error('Error while updating deal: %u', error)
    else:
        logging.info('Deal %u successfully updated', deal_id)

# function to get active deals
def get_active_deals():
    error, data = p3cw.request(
        entity='deals',
        action='',
        payload={
            "scope": "active"
        }
    )
    if (error):
        logging.error('Error while requesting active deals: %s', error)
        return

    return data

try:
    while True:
        logging.info('Checking the status of the active deals.')

        # reset counters
        active_deals = 0
        updated_deals = 0

        # request active deals
        deals = get_active_deals()

        for deal in deals:
            # print all deals and details for debugging
            if (DEBUG):
                for key in deal:
                    print(key, '->', deal[key], '->', type(deal[key]))

            # display current status
            if (deal['bot_name'] == BOT_NAME):
                active_deals +=1

            # look for deals that need updating
            if (deal['completed_safety_orders_count'] == 3 and deal['take_profit'] != '1.0'):
                updated_deals += 1
                deal_update_tp(deal['id'], 1.0, deal['pair'], deal['completed_safety_orders_count'], deal['take_profit'])

            elif (deal['completed_safety_orders_count'] == 4 and deal['take_profit'] != '2.0'):
                updated_deals += 1
                deal_update_tp(deal['id'], 2.0, deal['pair'], deal['completed_safety_orders_count'], deal['take_profit'])

            elif (deal['completed_safety_orders_count'] == 5 and deal['take_profit'] != '3.0'):
                updated_deals += 1
                deal_update_tp(deal['id'], 3.0, deal['pair'], deal['completed_safety_orders_count'], deal['take_profit'])

            elif (deal['completed_safety_orders_count'] == 6 and deal['take_profit'] != '4.0'):
                updated_deals += 1
                deal_update_tp(deal['id'], 4.0, deal['pair'], deal['completed_safety_orders_count'], deal['take_profit'])

            elif (deal['completed_safety_orders_count'] == 7 and deal['take_profit'] != '5.0'):
                updated_deals += 1
                deal_update_tp(deal['id'], 5.0, deal['pair'], deal['completed_safety_orders_count'], deal['take_profit'])

            elif (deal['completed_safety_orders_count'] == 8 and deal['take_profit'] != '6.0'):
                updated_deals += 1
                deal_update_tp(deal['id'], 6.0, deal['pair'], deal['completed_safety_orders_count'], deal['take_profit'])

        logging.info('Check complete, there are %d active deals and %d required updating.', active_deals, updated_deals)
        # sleep for 60 seconds and start again
        time.sleep(60)

except KeyboardInterrupt:
    print('Stopping by user request due to keyboard interupt.')

except:
    print('Something went wrong, look above this message for more details... stopping!')
