def display(player_data):
    high_var = 0
    for i in range(len(player_data)):
        if player_data[i] > high_var:
            high_var = player_data[i]
            high_index = i
    low_var = 999
    low_index = 0
    for i in range(len(player_data)):
        if player_data[i] < low_var:
            low_var = player_data[i]
            low_index = i
    sum_var = 0
    for i in range(len(player_data)):
        sum_var = sum_var + player_data[i]
    avg_var = sum_var / len(player_data)
    print("Your Last Name")
    print("Scores Array = ", player_data)
    print("Highest value = ", high_var)
    print("Lowest value = ", low_var)
    print("Average value = ", avg_var)
  
player_data = [456, 123, 231, 455, 440, 312, 231, 230]
display(player_data)