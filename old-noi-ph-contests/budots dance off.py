from itertools import product
rounds = int(input())
opponent_sequence = input().split()
num_sequences = 0
all_sequences = list(product(["1", "2", "3"], repeat=rounds))
def super_effective(move_1, move_2):
    if (move_1 == "1" and move_2 == "2") or (move_1 == "2" and move_2 == "3") or (move_1 == "3" and move_2 == "1"):
        return "Yes"
    elif (move_1 == "1" and move_2 == "3") or (move_1 == "2" and move_2 == "1") or (move_1 == "3" and move_2 == "2"):
        return "No"
    else:
        return "Tie"
def tournament(seq_1, seq_2):
    points_1 = 0
    points_2 = 0
    for i in range(len(seq_1)):
        if super_effective(seq_1[i], seq_2[i]) == "Yes":
            points_1 += 1
        elif super_effective(seq_1[i], seq_2[i]) == "No":
            points_2 += 1
        else:
            points_1 -= 1
            points_2 -= 1
    return [points_1, points_2]

for j in range(len(all_sequences)):
    if tournament(all_sequences[j], opponent_sequence)[0] > tournament(all_sequences[j], opponent_sequence)[1]:
        num_sequences += 1
print(num_sequences)
