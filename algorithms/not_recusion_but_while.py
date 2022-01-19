'''
Abstract task about a big box with smaller boxes and 
one key somewhere in there.
Solution with "while".
'''

def look_for_key(main_box):
    pile = main_box.look_through()
    while pile == True:
        box = pile.grab_a_box()
        for item in box:
            if item.is_a_box():
                pile.append(item)
            elif item.is_a_key():
                print('We found the key!')
