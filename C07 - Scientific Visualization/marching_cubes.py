# /// script
# dependencies = [
#   "pyvista",
#   "numpy",
# ]
# ///

import pyvista as pv
import numpy as np

isovalue = 0.8  # Change me !

x, y = np.ogrid[-np.pi : np.pi : 100j, -np.pi : np.pi : 100j]
image = np.sin(np.exp(np.sin(x) ** 3 + np.cos(y) ** 2))

grid = pv.ImageData()
grid.dimensions = np.append(image.shape, 1)
grid.point_data["values"] = image.flatten(order="F")

points = []


def interpol(val1, val2):
    # Linear interpolation of the isovalue between val1 and val2
    # Returns a value between 0 and 1
    return (isovalue - val1) / (val2 - val1)


# Isocontour processing
for line in range(len(image) - 1):
    for col in range(len(image[0]) - 1):
        # Retrieve vertex scalars
        scalars = [
            image[line + 1][col],
            image[line + 1][col + 1],
            image[line][col + 1],
            image[line][col],
        ]

        # First, we compute the score for this square
        # Add 1 to score if the bottom-left corner is higher than threshold
        # 2 if bottom-right is, 4 for top-right and 8 for top-left
        score = 0
        for i in range(4):
            if scalars[i] > isovalue:
                score |= 1 << i

        if score in [0, 15]:
            continue

        # Draw a line if point 1 is in, but not 2 and 3 (or the opposite)
        if score in [1, 10, 14]:
            points += [
                (line + interpol(scalars[3], scalars[0]), col, 0),
                (line + 1, col + interpol(scalars[0], scalars[1]), 0),
            ]

        # pont 2 in
        if score in [2, 5, 13]:
            points += [
                (line + 1, col + interpol(scalars[0], scalars[1]), 0),
                (line + interpol(scalars[2], scalars[1]), col + 1, 0),
            ]

        # point 4 in
        if score in [4, 10, 11]:
            points += [
                (line, col + interpol(scalars[3], scalars[2]), 0),
                (line + interpol(scalars[2], scalars[1]), col + 1, 0),
            ]

        # point 8 in
        if score in [5, 7, 8]:
            points += [
                (line + interpol(scalars[3], scalars[0]), col, 0),
                (line, col + interpol(scalars[3], scalars[2]), 0),
            ]

        # up and down
        if score in [3, 12]:
            points += [
                (line + interpol(scalars[3], scalars[0]), col, 0),
                (line + interpol(scalars[2], scalars[1]), col + 1, 0),
            ]

        # left and right
        if score in [6, 9]:
            points += [
                (line + 1, col + interpol(scalars[0], scalars[1]), 0),
                (line, col + interpol(scalars[3], scalars[2]), 0),
            ]

points = np.array(points)
connectivity = np.arange(points.shape[0])
offsets = np.arange(0, points.shape[0], 2)

cells = pv.core.CellArray.from_arrays(offsets, connectivity)
surf = pv.PolyData()
surf.lines = cells
surf.points = points
surf.translate((0, 0, -0.1), inplace=True)

contours = grid.contour(isovalue, "values")
contours.translate((0, 0, -0.1), inplace=True)
pl = pv.Plotter()
pl.add_mesh(grid, show_edges=True, opacity=0.85)

pl.add_mesh(surf, color="red", line_width=5)
pl.add_mesh(contours, color="white", line_width=2)
pl.enable_2d_style()
pl.camera_position = "yx"
pl.show()
