import csv 
from pathlib import Path 

csv_file = Path("Premier 16-17.csv")

def check_file_exists(csv_file): 
    return csv_file.is_file()
        
def read_csv(csv_file):
    csv_contents = []
    if check_file_exists(csv_file):
        with open(csv_file) as csvfile:
            reader = csv.reader(csvfile, delimiter=",")
            next(reader)                  ###   skip first row (header)
            for row in reader:
                csv_contents.append(row)
    return csv_contents

def process(csv_contents):
    dictionary_a = {}
    for row in csv_contents:
        hometeam = row[1]
        awayteam = row[2]
        homegoal = row[3]
        awaygoal = row[4]
        winner = row[5]
        
        
        if hometeam not in dictionary_a:
            dictionary_a[hometeam] = [0, 0, 0, 0, 0] #Wins, Draws, Losses, GD, Points
        if awayteam not in dictionary_a:
            dictionary_a[awayteam] = [0, 0, 0, 0, 0]
        if winner == "D":
            dictionary_a[hometeam][1]+= 1
            dictionary_a[awayteam][1]+= 1
            dictionary_a[hometeam][4]+= 1
            dictionary_a[awayteam][4]+= 1
        if winner == "A":
            dictionary_a[hometeam][2] += 1
            dictionary_a[awayteam][0] += 1
            dictionary_a[hometeam][4] += 0
            dictionary_a[awayteam][4] += 3
            
        if winner == "H":
            dictionary_a[hometeam][0] += 1
            dictionary_a[awayteam][2] += 1
            dictionary_a[hometeam][4] += 3
            dictionary_a[awayteam][4] += 0

        goal_difference1 = int(homegoal) - int(awaygoal)
        goal_difference2 = int(awaygoal) - int(homegoal)
        dictionary_a[hometeam][3] += goal_difference1
        dictionary_a[awayteam][3] += goal_difference2

        
            
            
        
    return dictionary_a

def printdictinrow(dictionary_a):
    for key, value in dictionary_a.items():
        print(f"{key:<20} {value[0]:<30} {value[1]:<40} {value[2]:<50} {value[3]:<60} {value[4]:<70}")

if __name__ == "__main__":
    file_contents = read_csv(csv_file)
    league_dictionary = process(file_contents)
    final = printdictinrow(league_dictionary)
    

