# RRT Path Finding Project for Autonomous Driving

#### This project implements the Rapidly-exploring Random Tree (RRT) algorithm for pathfinding in autonomous driving. The algorithm efficiently computes a collision-free path from a given starting point to a specified goal point on a map image, considering obstacles.

## Example output
![alt text](https://github.com/TejasKalsait/Path_Finding_Autonomous_driving/blob/main/map2.png?raw=true)

## Table of Contents
- [Introduction](#introduction)
- [How to Use](#how-to-use)
- [Installation](#installation)
- [Dependencies](#dependencies)
- [Running the Project](#running-the-project)
- [Results](#results)
- [License](#license)

## Introduction

The goal of this project is to provide a reliable and fast path finding solution for autonomous vehicles using the RRT algorithm. RRT is particularly well-suited for high-dimensional spaces and dynamic environments, making it an excellent choice for real-world autonomous driving scenarios.

## How to Use

To use this project, follow the steps below:

1. Clone the repository to your local machine.

2. Ensure you have all the required dependencies installed. (Refer to the [Dependencies](#dependencies) section).

3. Prepare a map binary image where you want to find the path or use the one inside the maps directory. The map image should represent the environment with obstacles, and it should be in a common image format like PNG or JPEG and only contain pixel values as 255 (obstacle) and 0 (no-obstacle).

4. Run the `main.py` file with the required arguments in the following format:

```bash
python main.py start_x start_y goal_x goal_y map_image
```

- `start_x` and `start_y` are the x and y coordinates of the starting point, respectively.
- `goal_x` and `goal_y` are the x and y coordinates of the goal point, respectively.
- `map_image` is the path to the map image file.

5. The algorithm will compute the path, avoiding obstacles, and draw it on the map image.

6. The resulting map image with the path will be saved in the home directory.

## Installation

To run this project, you need to have Python installed. Follow these steps to get started:

1. Clone the repository:

```bash
git clone https://github.com/TejasKalsait/Path_Finding_Autonomous_driving.git
cd Path_Finding_Autonomous_driving
```

2. Create a virtual environment (optional but recommended):

```bash
python -m venv venv
```

3. Activate the virtual environment:

- For Windows:

```bash
venv\Scripts\activate
```

- For macOS and Linux:

```bash
source venv/bin/activate
```

4. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Dependencies

The project relies on the following Python libraries:

- OpenCV (cv2): For image processing and visualization.
- NumPy: For numerical operations.
- Python version > 3.8
- matplotlib

These dependencies are specified in the `requirements.txt` file and will be installed during the installation process.

## Running the Project

To run the RRT path-finding algorithm and visualize the results, use the `main.py` script as explained in the [How to Use](#how-to-use) section.

## Results

Upon successful execution of the `main.py` script, the resulting map image will be saved in the same directory as the main.py file. The path will be drawn on the image, indicating the trajectory from the starting point to the goal point while avoiding obstacles.
