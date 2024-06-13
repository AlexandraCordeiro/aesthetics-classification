import matplotlib.pyplot as plt
import numpy as np
import random
import os 
import csv
from tabulate import tabulate

num_plots = 302
# for test split
test = int(num_plots * 0.2)

# different types of plots
plot_type = ['plot', 'scatter', 'bar', 'stem', 'stack_plot', 'stairs']
line_styles = ['-', '--', '-.', ':']
marker_styles = ['o', 's', 'x', '^']
colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']

# rows for cvs file
row_list = [["plot_name", "plot_type", "x", "y"]]



# ---------------------------------
directory = "non-aesthetic"

if not os.path.exists(directory):
    os.makedirs(directory)

test_dir = os.path.join(directory, "test")
train_dir = os.path.join(directory, "train")

if not os.path.exists(test_dir):
    os.makedirs(test_dir)

if not os.path.exists(train_dir):
    os.makedirs(train_dir)

# ---------------------------------
random.seed(42)
np.random.seed(42)

for i in range(num_plots):
    type = random.choice(plot_type)
    color = random.choice(colors)

    if type == 'plot':
        x = np.linspace(0, np.random.randint(10, 50), np.random.randint(10, 50))
        line_style = random.choice(line_styles)

        if np.random.randint(1, 10) % 2 == 0: 
            y = np.sin(np.random.randint(1, 10) * x)
            plt.plot(x, y, line_style, color)
        else:
            y = np.random.randint(1, 100, len(x))
            plt.plot(x, y, line_style, color)
        
        
    if type == 'scatter':
        x = np.linspace(0, np.random.randint(10, 100), np.random.randint(10, 100))
        y = np.random.rand(len(x))

        marker_style = random.choice(marker_styles)
        plt.scatter(x, y, marker=marker_style, color=color)
    
    if type == 'bar':
        x = np.arange(np.random.randint(4, 30))
        y = np.random.randint(1, 10, size=len(x))
        plt.bar(x, y, color=color, width=1, edgecolor='white')
    
    if type == 'stem':
        x = np.arange(np.random.randint(4, 30))
        y = np.random.randint(1, 10, size=len(x))
        plt.stem(x, y)

    if type == 'fill_between':
        pass

    if type == 'stack_plot':
        x = np.arange(1, np.random.randint(100), np.random.randint(1, 5))
        stack = []

        a =  np.random.randint(1, 5, size=len(x))
        b =  np.random.randint(1, 5, size=len(x)) * 2
        c =  np.random.randint(1, 5, size=len(x)) * 4

        y = np.vstack([a, b, c])

        plt.stackplot(x, y)
        

    if type == 'stairs':
        # y_range = np.random.randint(10, 50)
        y_range = 5
        y = np.random.rand(y_range)
        line_width = np.random.randint(1, 4)
        x = np.arange(0, len(y) + 1)
        # print(x)
        plt.stairs(y, linewidth=line_width)
    
    
    # plt.savefig(f'plot_{i+1}.png')
    if i < test:
        new_dir = test_dir
    else:
        new_dir = train_dir

    row_list.append([f'plot_{i+1}.png', type, x , y])
    plt.savefig(os.path.join(new_dir, f'plot_{i+1}.png'))
    plt.clf()

# ---------------------------------
with open('non_aesthetic_plots_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for row in row_list:
        writer.writerow(row)

# print(tabulate(row_list, headers='firstrow', tablefmt='fancy_grid'))