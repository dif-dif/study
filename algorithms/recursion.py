'''
Abstract task about a big box with smaller boxes and 
one key somewhere in there.
Solution with recursion.
'''

def look_for_key(box):
    for item in box:
        if item.is_a_box():
            look_for_key(item)
        elif item.is_a_key():
            print('We found the key!')