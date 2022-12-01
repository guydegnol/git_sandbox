
import numpy as np
import matplotlib.pyplot as plt
def plot_sinus():
  angle = np.arange(360)
  sinus = np.sin(2 * np.pi * angle /360)

  plt.plot(angle, sinus)    
  