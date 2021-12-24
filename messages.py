help_message = '''
Отправьте команду /buy, чтобы перейти к покупке.
Узнать правила можно воспользовавшись командой /terms.
'''

start_message = 'Привет! Сейчас ты увидишь работу платежей в Telegram!\n' + help_message

terms = '''\
Правила!
'''

item_title = 'Ноутбук'
item_description = '''\
Купить ноутбук крутой честно правда
'''

AU_error = '''\
В данную страну доставка не оформляется. Сорри
'''

successful_payment = '''
Платеж на сумму `{total_amount} {currency}` совершен успешно!
'''


MESSAGES = {
    'start': start_message,
    'help': help_message,
    'terms': terms,
    'item_title': item_title,
    'item_description': item_description,
    'AU_error': AU_error,
    'successful_payment': successful_payment,
}
