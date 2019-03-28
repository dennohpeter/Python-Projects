import itertools

games = ['France - Germany']
case = ["1","X","2"]
results = []
for eachcase in case:
    for game in games:
        results.append("%s %s" % (game, eachcase))


print("\n".join(results)+ "\n %s" %len(results))
