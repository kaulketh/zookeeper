# work with these variables
eugene = set(input().split())
rose = set(input().split())

out = set.symmetric_difference(eugene, rose)
print(out)
