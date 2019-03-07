import pandas as pd
import matplotlib.pyplot as plt

x=range(5)
state_list=['VA','OH','PA','KY','WV']
tot_reposts=[41462,70999,89981,29588,8668]
plt.bar(state_list,tot_reposts)
plt.title("total drug reports of each state")

plt.savefig('tot_report.png')

