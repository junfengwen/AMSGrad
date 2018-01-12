import matplotlib.pyplot as plt

def plot_results(y_values, names, y_label):
  for m in range(len(names)):
    plt.plot(range(len(y_values[m])), y_values[m], label=names[m])
  plt.ylabel(y_label)
  plt.legend()
  plt.show()
