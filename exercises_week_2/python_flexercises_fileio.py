
# ex 1, 2

import json

import matplotlib
matplotlib.use("Agg")
from matplotlib import pyplot

# grab_file = input("What file would you like to load? ")

# user_input = input("Enter data: ")

# def load_data():
#     with open(grab_file, 'r') as fh:
#         return json.load(fh)

# def save_data(data):
#     with open(grab_file, 'w') as fh:
#         return json.dump(user_input, fh)

# data = load_data()

# data['hello'] = 'me'
# data['hello2'] = 'me'

# save_data(user_input)


# ex 3

def grab_json_data():

    with open("data.json", "r") as fh:
        data = json.load(fh)


    x_coord = []
    y_coord = []

    for i in data["data"]:
        x_coord.append(i[0])
        y_coord.append(i[1])



    pyplot.plot(x_coord, y_coord)
    pyplot.savefig("input_plot.png")
    pyplot.close()

# if __name__ == "__main__":
#     grab_json_data()