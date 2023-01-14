
things = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
def displayInventory(inventory):
    print("Inventory:")
    total = 0
    for k, v in inventory.items():
      print(v, k)
      total += v
    print("Total number of items: " + str(total))
displayInventory(things)