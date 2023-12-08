from collections import namedtuple

Item = namedtuple('Item', 'weight price')


def check(items, target, ans, func):
    import codewars_test as test
    from collections import Counter
    
    msg        = f'Tested with: n={target} and items={items}'
    user_items = [*items]
    user       = func(user_items, target)
    
    
    if user_items != items:
        return test.fail(f"You should not modify the argument items. {user_items} should equal {items}")
    
    if not isinstance(user, list):
        return test.fail(f"Your result should be an array, but was: {user}")
    
    if any(not isinstance(item,Item) for item in user):
        return test.fail(f"Your result should be an array of Item instances, but was: {user}")
    
    
    weight = sum(it.weight for it in user)
    price  = sum(it.price for it in user)
    max_price = sum(it.price for it in ans)
    
    if weight > target:
        return test.fail(f"The bag is too heavy: {weight} is greater than {target=}")
    if price != max_price:
        return test.fail(f"You should get the max possible price: {price} should be {max_price}")
    
    counts = Counter(items)
    counts.subtract(Counter(user))
    
    if any(n<0 for n in counts.values()):
        s = ', '.join( str(it) for it,n in counts.items() if n<0)
        return test.fail(f"Some items have been used too many times or do not exist in the original list: {s}")
    
    test.pass_()