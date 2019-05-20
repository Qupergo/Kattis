count = int(input())
planets = []

for _ in range(count):
	planets.append(input().split())

for planet in planets:
	population, growth_rate, food_per_year = int(planet[0]), int(planet[1]), int(planet[2])

	years = 0
	while population <= food_per_year:
		population *= growth_rate
		years += 1

	print(years)
