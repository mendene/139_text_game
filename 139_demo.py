def stats(health, bag):   # abstraction to calculate stats
    print "You have", health, "health points."
    print "Here's what your bag contains:", bag

def choose():
    ''' a text-based game in which you attempt to survive lunch
    by choosing real, healthy foods and avoiding common lunchtime 
    pitfalls '''

    health = 0
    bag = []
    
    # set main course options
    lunch = int(raw_input("Late to lunch!  There's only fries (1) or fish sticks (2) left.  Do you choose 1 or 2? "))
    if lunch == 1:
        print 'Good choice.  Gain 1 health point.'
        health = health + 1
    else:
        print 'The fish sticks are fake.  Lose one health point.'
        health = health - 1

    stats(health, bag)    # call stats function (an abstraction)
