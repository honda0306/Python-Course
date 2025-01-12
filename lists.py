wood_tools = ['handsaw', 'chisel', 'hammer', 'drawknife']

print(wood_tools)
print(wood_tools[2])
print(wood_tools[0].title())
print(wood_tools[-1])

favorite_tool = f"My favorite woodworking tool is the {wood_tools[1]}."
print(favorite_tool)

# Manipulating lists

## Changing individual indices
print(wood_tools[3])
wood_tools[3] = "spokeshave"
print(wood_tools[3])
wood_tools.insert(0, 'Japanese saw')
print(wood_tools[0])

## Add elements to end of list
wood_tools.append('drawknife')
print(wood_tools)

## Remove items
print(wood_tools)
del wood_tools[1]
print('Element removed', wood_tools)
recent_tool = wood_tools.pop()
print(f"My newest tool is a {recent_tool}.")
print(wood_tools)
wood_tools.remove('chisel')
print(wood_tools)

## Sorting lists
wood_tools.sort()
print(f"Sorted list of tools: {wood_tools}")
wood_tools.sort(reverse=True)
print(f"List sorted in reverse: {wood_tools}")
print(f"Temporarily sorted: {sorted(wood_tools)}")
wood_tools.reverse()
print(f"List reversed again: {wood_tools}")
print(f"Length of list: {len(wood_tools)}")