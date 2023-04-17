def display_arrays(names, averages):
    for i in range(len(names)):
        print(f"{names[i]}: {averages[i]}")
def search_name(name, names, averages):
    for i in range(len(names)):
        if names[i] == name:
            return i
    return -1
  
def main():
    names = []
    averages = []

    with open('player_data.txt', 'r') as file:
        for line in file:
            name, average = line.strip().split()
            names.append(name)
            averages.append(float(average))
    display_arrays(names, averages)
    while True:
        user_input = input("Enter a player's last name or 'q' to quit: ")
        if user_input == 'q':
            break
        index = search_name(user_input, names, averages)
        if index != -1:
            print(f"{names[index]} has a batting average of {averages[index]}.")
        else:
            print("Player not found.")
if __name__ == '__main__':
    main()