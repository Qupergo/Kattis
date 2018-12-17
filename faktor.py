import math
Articles, CitationsPerArticle = map(int, input().split())

print(math.ceil((Articles * (CitationsPerArticle - 0.99))))
