'''
Mini-module housing visualisation code for timetrends and boxplots
'''

# Stadard library imports
from os.path import join
import os
import math

# External library imports
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pandas.plotting import register_matplotlib_converters

def draw_boxplot(board, data, savedir):
    '''
    data should come in as a pandas dataframe
    savedir should be a path
    '''
    
    rc = {'figure.figsize':(3, 0.6),
          'axes.facecolor':'white',
          'ytick.labelleft':False,
          'ytick.left':False,
          'xtick.labelbottom':False,
          'xtick.bottom':False,
          'savefig.pad_inches':0.05}

    plt.rcParams.update(rc)

    fig, ax = plt.subplots(1, 1)
    sns.boxplot(x="board_rate", ax=ax, data=data, color="white", showfliers=False)
    #swarmplot can throw up warnings about gutter and points
    with np.errstate(invalid='ignore'):
        sp = sns.swarmplot(x="board_rate", ax=ax, data=data)

    board_rate = data[data['board_name'] == board].iloc[0]['board_rate']
    swarm_offsets = sp.collections[0].get_offsets()
    swarm_colors = list(sp.collections[0].get_facecolors())

    swarm_pos = None

    #get a matching positing of the board in the swarm
    for i, rate in enumerate(swarm_offsets):
        if math.isclose(rate[0], board_rate, rel_tol=1e-06):
            swarm_pos = i

    board_color = matplotlib.colors.to_rgba('red')
    swarm_colors_new = (
        swarm_colors[:swarm_pos] +
        [board_color] + 
        swarm_colors[swarm_pos:]
    )

    sp.collections[0].set_facecolors(swarm_colors_new)

    #Remove labels
    ax.set_ylabel('')    
    ax.set_xlabel('')
    
    fig.savefig(savedir, format='png', bbox_inches="tight")
    plt.close(fig)


def draw_timetrend(data, savedir):
    '''
    data should come in as a pandas dataframe
    savedir should be a path
    '''
    
    rc = {'figure.figsize':(2, 0.6),
          'axes.facecolor':'white',
          'ytick.labelleft':False,
          'ytick.left':False,
          'xtick.labelbottom':False,
          'xtick.bottom':False,
          'savefig.pad_inches':0.05,
          'lines.linewidth': 1}

    plt.rcParams.update(rc)

    fig, ax = plt.subplots(1, 1)

    sns.lineplot(x='time', y='board_rate', estimator=None, data=data)
    #Remove labels
    ax.set_ylabel('')    
    ax.set_xlabel('')
    
    fig.savefig(savedir, format='png', bbox_inches="tight")
    plt.close(fig)


def generate_viz(breaches):
    '''
    Doc string
    '''
    register_matplotlib_converters()
    root_path = join(os.getcwd(), 'pyalerts', 'temp')

    for hb in breaches.keys():
        for breach in breaches[hb].keys():

            d = breaches[hb][breach]

            boxplot_data = pd.DataFrame(
                data=d['boxplot'],
                columns=['board_name', 'board_rate']
            )

            timetrend_data = pd.DataFrame(
                data=d['timetrend'],
                columns=['time', 'board_rate']
            )

            boxplot_savedir = join(
                root_path,
                f"temp_{hb}",
                f"temp_boxplot_{d['indicator_id']}.png")

            timetrend_savedir = join(
                root_path,
                f"temp_{hb}",
                f"temp_timetrend_{d['indicator_id']}.png")

            draw_boxplot(hb, boxplot_data, boxplot_savedir)
            draw_timetrend(timetrend_data, timetrend_savedir)
