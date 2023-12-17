import random

dishes = {
    'soup': ['pomidorowa', 'barszcz', 'rosół'],
    'dinner': ['pulpety', 'schabowy', 'gołąbki'],
    'dessert': ['lody', 'kisiel', 'ciasto']
}

random_soup = random.choice(dishes['soup'])
random_dinner = random.choice(dishes['dinner'])
random_dessert = random.choice(dishes['dessert'])
print(random_soup)
print(random_dinner)
print(random_dessert)