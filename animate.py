import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.image as mpimg
import glob

# Collect all PNG frames (sorted by filename like 01.png, 02.png, ...)
frames = sorted(glob.glob("frames/darwin_fourier/*.png"))

fig, ax = plt.subplots()
img = mpimg.imread(frames[0])       # first frame
im = ax.imshow(img)
ax.axis("off")  # hide axes

def update(frame_path):
    im.set_array(mpimg.imread(frame_path))
    return [im]

ani = animation.FuncAnimation(
    fig, update, frames=frames, interval=100, blit=True
)

# Save as video (requires ffmpeg installed)
ani.save("video/darwin_fourier.mp4", writer="ffmpeg", fps=10)
