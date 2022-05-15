import matplotlib.pyplot as pylot

BAR_WIDTH = 0.35
teamA_result = (60, 75, 56, 62, 58)
teamB_result = (55, 68, 80, 73, 55)

#index team
index_teamA = (1, 2, 3, 4, 5)
index_teamB = [i + BAR_WIDTH for i in index_teamA]

#tick team
ticks = [i + BAR_WIDTH / 2 for i in index_teamA]
tick_label = ('lab1', 'lab2', 'lab3', 'lab4', 'lab5')

pylot.bar(index_teamA, teamA_result, BAR_WIDTH, color='g', label='team A')
pylot.bar(index_teamB, teamB_result, BAR_WIDTH, color='c', label='team B')

pylot.xlabel('Labs')
pylot.ylabel('Score')
pylot.title('score by lab')
pylot.xticks(ticks, tick_label)
pylot.legend()
pylot.show()
