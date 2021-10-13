from matplotlib import pyplot as plt
from matplotlib import dates
from api_key import get_humidity


def init_plot():
    plt.figure('PyOWM Weather', figsize=(5,4))
    plt.xlabel('Day')
    plt.ylabel(f'Humidity (%)')
    plt.title('Humidity Forecast')

def plot_humidity(day, humidity):

    bar_humidity = plt.bar(day, humidity,align='center')
    return (bar_humidity)

def label_xaxis(day):
    # Use the days as the x-axis labels
    plt.xticks(day)
    # Set format for axis label to just month and day
    axes = plt.gca()
    xaxis_format = dates.DateFormatter('%m/%d')
    axes.xaxis.set_major_formatter(xaxis_format)

def write_humidity_on_bar_chart(bar_humidity):
    axes = plt.gca()
    y_axis_max = axes.get_ylim()[1]
    label_offset = y_axis_max * .1
    # Write the temperatures on the chart
    for index, bar in enumerate(bar_humidity):
        height = bar.get_height()
        xpos = bar.get_x() + bar.get_width()/2.0
        ypos = height - label_offset
        label_text = str(int(height)) + "%"
        label = plt.text(xpos, ypos, label_text,
                         horizontalalignment='center',
                         verticalalignment='bottom',
                         color='white')

if __name__ == '__main__':
    City= input("Enter the City name: ")
    day, humidity = get_humidity(City)
    init_plot()
    bar_humidity = plot_humidity(day, humidity)
    label_xaxis(day)
    write_humidity_on_bar_chart(bar_humidity)
    plt.show()
