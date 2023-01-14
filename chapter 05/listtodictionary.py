
def addToInventory(inventory, addedItems):
    for item in dragonLoot:
      inventory.setdefault(item,0)
      inventory[item] = inventory[item]+1
    return inventory
def displayInventory(inventory):
    print("Inventory:")
    total = 0
    for k, v in inventory.items():
      print(v, k)
      total += v
    print("Total number of items: " + str(total))


inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)