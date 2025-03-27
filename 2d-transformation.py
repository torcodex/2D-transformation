import numpy as np

# Define points and transformation matrices
points = {
    "A": np.array([2, 3, 1]),
    "B": np.array([5, 7, 1]),
    "C": np.array([8, 3, 1])
}
scaling_matrix = np.array([[2, 1, 0], [0, 4, 0], [1, 0, 1]])
theta = np.radians(90)
rotation_matrix = np.array([
    [np.cos(theta), -np.sin(theta), 0],
    [np.sin(theta), np.cos(theta), 0],
    [0, 0, 1]
])
translation_matrix = np.array([[2, 0, 7], [0, 3, -1], [0, 1, 2]])

def transform_points(points, matrix):
    return {key: matrix @ point for key, point in points.items()}

scaled_points = transform_points(points, scaling_matrix)
print("Scaling Results:")
for key, point in scaled_points.items():
    print(f"Scaled {key}: {tuple(map(int, point[:2]))}")
print()

rotated_points = transform_points(scaled_points, rotation_matrix)
print("Rotation Results:")
for key, point in rotated_points.items():
    print(f"Rotated {key}: {tuple(map(int, point[:2]))}")
print()

translated_points = transform_points(rotated_points, translation_matrix)
print("Translation Results:")
for key, point in translated_points.items():
    print(f"Translated {key}: {tuple(map(int, point[:2]))}")
