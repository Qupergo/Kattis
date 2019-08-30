towers = map(int, input().split())

tower_blocks = towers[:6]
tower1_height = towers[6]
tower2_height = towers[7]


def create_tower(tower_blocks, height1, height2):
	tower_test = []
	tower_blocks = sorted(tower_blocks)
	index = 0
	while height1 != sum(tower_test) and len(tower_test) == 3:
		current_addition = tower_blocks[index]
		tower_test.append(current_addition)

		if sum(tower_test) > height1:
			tower_test.remove(current_addition)

		index += 1
	return tower_test

print(create_tower(tower_blocks, tower1_height, tower2_height))
