import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

# Create a blank canvas
fig, ax = plt.subplots()
canvas = np.zeros((100, 100))  # Adjust dimensions as needed

# Function to update the canvas in each frame of the animation
def update(frame):
    # Gradually fill the canvas with colors and shapes
    canvas[np.random.randint(0, 100), np.random.randint(0, 100)] = np.random.random()

    # Display the canvas
    ax.imshow(canvas, cmap='viridis')  # You can change the colormap if desired
    return ax

# Create the animation
animation = FuncAnimation(fig, update, frames=100, interval=100)
plt.show()