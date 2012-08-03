import dice

roll = dice.DiceRoll(3, [3])

# print str(roll + 1)
# print str(roll - 1)
# print str(roll * 1)
# print str(roll > 1)
# print str(roll >= 1)
# print str(roll < 1)
# print str(roll <= 1)
# print str(roll == 1)
# print str(roll != 1)
# print str(1 + roll)
# print str(1 - roll)
# print str(1 * roll)
# print str(1 // roll)

print str((roll + 1) == (1 + roll))
print str((roll * 1) == (1 * roll))

print str((roll == 1) == (1 == roll))
print str((roll != 1) == (1 != roll))

# print roll[0]