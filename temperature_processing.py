'''
------------------------------------------------------------------------------------------------------------------------
#➥Author : Alae Boufarrachene
#➥Project : Modular Heated Tiles
#➥Description : Python script used to automate computations using the temperature data gathered from the MCU
------------------------------------------------------------------------------------------------------------------------
'''


def log_to_datapoints():
    log_file = open("putty.log")
    file_content = [line.split("\n") for line in
                    log_file.readlines()]  # Converts all the file content into a 2D list of strings (each line being a list)
    datapoints = []  # List of floats that contains all temperature data points gathered from the sensor

    for i in range(1, len(
            file_content) - 1):  # Used to populate the datapoints list by converting all string temperatures into floats
        temp_float = float(file_content[i][0])
        datapoints.append(temp_float)

    return datapoints


def execution_period():
    period = len(log_to_datapoints())
    return period


def average_temperature():
    temperatures = log_to_datapoints()
    number_of_datapoints = len(temperatures)
    raw_average = sum(temperatures) / number_of_datapoints #Computes the average temperature
    rounded_average = round(raw_average) #Rounds the obtained temperature average to the nearest two decimals
    return rounded_average


def highest_temperature():
    temperatures = log_to_datapoints()
    max_temperature = max(temperatures)
    return max_temperature


def lowest_temperature():
    temperatures = log_to_datapoints()
    min_temperature = min(temperatures)
    return min_temperature

if __name__ == '__main__':
    print("----------------MHS Temperature Script Results----------------")
    print("➥Period of execution : "+str(execution_period())+"s")
    print("➥Average temperature : "+str(average_temperature())+"°C")
    print("➥Highest temperature : "+str(highest_temperature())+"°C")
    print("➥Lowest temperature : " + str(lowest_temperature()) + "°C")
    print("--------------------------------------------------------------")
