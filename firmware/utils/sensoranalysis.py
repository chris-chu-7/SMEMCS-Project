import matplotlib.pyplot as plt 
import csv
import statistics 


time = []
temp = []
humidity = []
ldr = []

def main(): 
    analyze_sensor_data('C:/Users/chris/Documents/SMEMCS/logs/sensor_log.csv')
    get_sensor_data_average()
    plot_sensor_data()


def analyze_sensor_data(file_path):
    with open(file_path, 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # skip header row 
        for row in reader:
            time.append(float(row[0]))
            temp.append(float(row[1]))
            humidity.append(float(row[2]))
            ldr.append(float(row[3]))
    return


def get_sensor_data_average(): 
    temp_avg = statistics.mean(temp)
    humidity_avg = statistics.mean(humidity)
    ldr_avg = statistics.mean(ldr)

    print(f"Average Temperature: {temp_avg: .2f} °F")
    print(f"Average Humidity: {humidity_avg: .2f} %")
    print(f"Average LDR: {ldr_avg: .2f} %")


def plot_sensor_data():
    fig, axs = plt.subplots(3, 1, figsize=(10, 10), sharex=True)

    # Temperature
    axs[0].plot(time, temp, color='red')
    axs[0].set_title("Temperature Over Time")
    axs[0].set_ylabel("Temperature (°F)")
    axs[0].grid(True)

    # Humidity
    axs[1].plot(time, humidity, color='blue')
    axs[1].set_title("Humidity Over Time")
    axs[1].set_ylabel("Humidity (%)")
    axs[1].grid(True)

    # LDR
    axs[2].plot(time, ldr, color='green')
    axs[2].set_title("LDR Over Time")
    axs[2].set_xlabel("Time (s)")
    axs[2].set_ylabel("LDR (%)")
    axs[2].grid(True)

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()