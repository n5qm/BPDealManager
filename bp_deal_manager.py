from py3cw.request import Py3CW
import time

### CONFIGURE 3C API KEY and BOT NAME HERE ###
API_KEY = ''
API_SECRET = ''
BOT_NAME = 'Block Party Testing'
DEBUG = 0


### DO NOT MODIFY ANYTHING BELOW HERE UNLESS YOU KNOW WHAT YOU ARE DOING ###


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
def deal_update_tp(deal_id, tp_level):
        print('Updating deal', deal_id, 'take profit to', tp_level)

        # sending request to update the deal
        error, data = p3cw.request(
            entity='deals',
            action='update_deal',
            action_id=str(deal_id),
            payload={
                "take_profit": tp_level
            }
        )
        if (error):
            print('Error while updating deal:', error)
        else:
            print('Deal:', deal_id, 'successfully updated.')

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
        print('Error while requesting active deals: ', error)
        return

    return data

try:
    while True:
        # request active deals
        deals = get_active_deals()

        for deal in deals:
            # print all deals and details for debugging
            if (DEBUG):
                for key in deal:
                    print(key, '->', deal[key])

            # display current status
            if (deal['bot_name'] == BOT_NAME):
                print('Deal:', deal['id'], ' Pair:', deal['pair'], ' Completed SOs:', deal['completed_safety_orders_count'], ' TP:', deal['take_profit'])

            if (deal['completed_safety_orders_count'] == 3 and deal['take_profit'] != '1.0'):
                # this deal needs to be updated
                deal_update_tp(deal['id'], 1.0)

            elif (deal['completed_safety_orders_count'] == 4 and deal['take_profit'] != '2.0'):
                # this deal needs to be updated
                deal_update_tp(deal['id'], 2.0)

            elif (deal['completed_safety_orders_count'] == 5 and deal['take_profit'] != '3.0'):
                # this deal needs to be updated
                deal_update_tp(deal['id'], 3.0)

            elif (deal['completed_safety_orders_count'] == 6 and deal['take_profit'] != '4.0'):
                # this deal needs to be updated
                deal_update_tp(deal['id'], 4.0)

            elif (deal['completed_safety_orders_count'] == 7 and deal['take_profit'] != '5.0'):
                # this deal needs to be updated
                deal_update_tp(deal['id'], 5.0)

            elif (deal['completed_safety_orders_count'] == 8 and deal['take_profit'] != '6.0'):
                # this deal needs to be updated
                deal_update_tp(deal['id'], 6.0)

        print('')
        # sleep for 60 seconds and start again
        time.sleep(60)

except KeyboardInterrupt:
    print('Stopping by user request due to keyboard interupt.')

except:
    print('Something went wrong, look above this message for more details... stopping!')
