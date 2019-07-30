file = open("story_multi.txt")

print("Line 1", file.readline() )
print("Line 2", file.readline() )
print("Line 3", file.readline() )
print("Line 4", file.readline() )

print( file.seek(0) )
print("All lines", file.readlines() )
