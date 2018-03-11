#ex 1

def hello(x):
    print("Hello, {}.".format(x))

# hello("Nick")

import matplotlib
matplotlib.use("Agg")

from matplotlib import pyplot

# ex 2

def f(x):
    return 2 * x + 1

# def g(x):
#     return x + 1

def line_plots():
    f_output = []
    # g_output = []

    x_range = list(range(-3, 3))

    for x in x_range:
        f_output.append(f(x))
        # g_output.append(g(x))

    pyplot.plot(x_range, f_output)
    pyplot.savefig("plot1.png")
    pyplot.close()



# if __name__ == "__main__":
#     line_plots()

# ex 3

def h(x):
    return x**(2)

def arc_plot():

    h_output = []
    x_range = list(range(-100, 100))

    for x in x_range:
        h_output.append(h(x))

    pyplot.plot(x_range, h_output)
    pyplot.savefig("plot2.png")
    pyplot.close()

# if __name__ == "__main__":
#     arc_plot()

# ex 4

def j(x):
    if x % 2 == 0:
        return 1
    else:
        return -1

def bar_plot():

    j_output = []
    x_range = list(range(-5, 5, 1))

    for x in x_range:
        j_output.append(j(x))

    pyplot.bar(x_range, j_output)
    pyplot.savefig("plot3.png")
    pyplot.close()

# if __name__ == "main":
#     bar_plot()




