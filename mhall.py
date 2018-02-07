import random
import numpy as np
import matplotlib.pyplot as plt
# random.seed(123)


def monty_hall(player_choice, switch):

    doors = [1, 2, 3]
    winning_door = random.choice(doors)

    if player_choice == winning_door:
        doors.remove(winning_door)
        doors.remove(random.choice(doors))
        switched_door = doors[0]

    else:
        host_door = [x for x in doors if x !=
                     winning_door and x != player_choice][0]
        doors.remove(host_door)
        doors.remove(player_choice)
        switched_door = doors[0]

    if switch == 1:
        if switched_door == winning_door:
            result = 1
        else:
            result = 0

    else:
        if player_choice == winning_door:
            result = 1
        else:
            result = 0

    return result


def winning_prob(n, player_choice, switch):
    all_results = []
    for trial in range(n):
        trial_results = monty_hall(player_choice, switch)
        all_results.append(trial_results)
        probability = sum(all_results) / n

    return probability


simulations = np.arange(1, 1000)
win_rate_switch = [winning_prob(n, 3, 1) for n in simulations]
win_rate_noswitch = [winning_prob(n, 3, 0) for n in simulations]
plt.plot(simulations, win_rate_switch)
plt.plot(simulations, win_rate_noswitch)
plt.xlabel('No. of Simulations')
plt.ylabel('Rate of winning')
plt.title('Monte Carlo Simulation with Door 3 choice')
plt.legend(['switch','no switch'])
plt.show()
