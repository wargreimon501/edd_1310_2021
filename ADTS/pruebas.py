from array  import
algo= Array (10)
print(algo.get_item(6))
algo.set_item(555,3)
print(algo.get_item(3))
print(f"el arreglo iene{algo.get_length()} elementos")
algo.clear(777)
print(algo.get_item(3))
print("prueba")
for x in  range(algo.get_length()):
    print(f"{x} -> {algo.get_item(x)}")
