DAYS= ['twelve Drummers Drumming',
         'eleven Pipers Piping',
         'ten Lords-a-Leaping',
         'nine Ladies Dancing',
         'eight Maids-a-Milking',
         'seven Swans-a-Swimming',
         'six Geese-a-Laying',
         'five Gold Rings',
         'four Calling Birds',
         'three French Hens',
         'two Turtle Doves',
         'a Partridge in a Pear Tree']

ORDER = [None, 'first', 'second', 'third', 'fourth', 'fifth', 'sixth',
           'seventh', 'eighth', 'ninth', 'tenth', 'eleventh', 'twelfth']

def line(gift_day):
    gifts=DAYS[-gift_day:]
    if len(gifts) > 1:
        gifts[:-1] = [', '.join(gifts[:-1])]
    gifts = ', and '.join(gifts)
    return 'On the {} day of Christmas my true love gave to me: {}.'.format(
        ORDER[gift_day], gifts)

def recite(start_verse, end_verse):
    return [line(n) for n in range(start_verse, end_verse + 1)]
