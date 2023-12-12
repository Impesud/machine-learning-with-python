# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

moves = {}
def player(prev_play, opponent_history=[]):
    opponent_history.append(prev_play)

    guess = "R"
    if len(opponent_history) > 3:
        schema = join(opponent_history[-3:])

        if join(opponent_history[-4:]) in moves:
          moves[join(opponent_history[-4:])] += 1
        else:
          moves[join(opponent_history[-4:])] = 1

        possibilities = [schema + "R", schema + "P", schema + "S"]

        for i in possibilities:
          if not i in moves:
            moves[i] = 0

        predict = max(possibilities, key=lambda key: moves[key])

        if predict[-1] == "P":
          guess = "S"
        elif predict[-1] == "S":
          guess = "R"
        else:
          guess = "P"
          
    return guess

def join(list):
  return "".join(list)
