cars=["toyota","bentley","mazda","mercedes","toyota"]
print(f"toyota appears {cars.count("toyota")} times on the list above")

morecars=["BMW","ferari"]
cars.extend(morecars)
print(cars)

print(f"'mazda' is found at the index {cars.index('mazda')}")