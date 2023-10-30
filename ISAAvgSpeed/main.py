import avg_speed

input_distance = input("Provide distance:")
input_time = input("Provide time:")

casted_distance = float(input_distance)
casted_time = float(input_time)
# print("Type input_distance", type(casted_distance))
print("Average speed", avg_speed.average_speed(casted_distance, casted_time))
