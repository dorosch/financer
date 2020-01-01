AMOUNT_CATEGORY_REGEXP = "([\d\.$]+) (.*)"

COMMANDS = (
    "View spending today - /today\n"
    "View weekly spending - /week\n"
    "View spending per month - /month\n"
    "View the current status - /status\n"
    "Add a cost participant - /share\n"
    "View the categories of expense - /categories\n"
)

START_TEXT = (
    "Hi, I'm your financial assistant!\n"
    "I will help you calculate your cash flows.\n"
    "Now I work only with dollars, sorry(\n"
    "Just send me a message like:\n"
    "amount$ category\n"
    "\n"
    "For example:\n"
    "1.5$ coffee\n"
    "\n"
    "I also support commands:\n" + COMMANDS
)

ANSWERS = (
    "Ok I got this",
    "I understood",
    "Wrote down",
    "Done",
    "Spend too much, but it's not my business",
    "Okay :(",
    "I like it",
    "As you say",
    "So let",
    "Maybe you are right",
    "I wrote down but do not confuse going to and will",
    "Okay smartassy",
)

CATEGORIES = {
    'eat': (
        'chocolate', 'goodies', 'sweets', 'milk', 'bread',
        'meat', 'vegetables', 'fruit', 'products', 'food'
    ),
    'sport': (
        'subscription', 'membership', 'climbing', 'run'
    ),
    'transport': (
        'metro', 'bus', 'train', 'tram', 'travel', 'taxi'
    ),
    'health': (
        'medicine', 'doctor', 'dental', 'tablets'
    ),
    'others': (

    )
}
