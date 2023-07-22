from booking.booking import Booking

with Booking() as bot:
    bot.land_first_page()
    bot.wait_until_popup()
    bot.select_place_to_go('New York')
    bot.select_acomm_dates('2023-07-27', '2023-07-29')
    # bot.select_currency_button()
    # bot.select_currency()
    print('Quiting...')