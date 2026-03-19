# AI/ML Football Analysis System 

This repository contains an AI-powered football analysis system that utilizes Computer Vision to track players, referees, and the football in match footage. Built using **YOLO (You Only Look Once)**, **OpenCV**, and **Python**, this system provides automated insights into player movement and match dynamics.

---

## Features

-   **Object Detection**: Real-time detection of players, referees, and the ball using YOLOv2626
-   **Tracking**: Persistent tracking of individuals across frames (ByteTrack/BoTSORT compatibility).
-   **Team Assignment**: Automated team identification based on jersey color analysis.
-   **Ball Possession**: Logic to determine which player/team has control of the ball.
-   **Perspective Transformation**: Map 2D video coordinates to a top-down tactical "birds-eye" view of the pitch.
-   **Speed & Distance Calculation**: Measure player metrics based on pitch scaling.

##  Tech Stack

-   **Language**: Python 3.x
-   **Object Detection**: Ultralytics YOLO
-   **Computer Vision**: OpenCV
-   **Data Handling**: NumPy, Pandas, Scikit-learn (for jersey color clustering)

##  Project Structure

```text
├── input_videos/      # Source match footage
├── runs/              # YOLO output and inference results
├── yolo_learning.py   # Experimental scripts and model testing
├── yolo26l.pt         # Custom/Pre-trained YOLO weights
└── README.md          # Project documentation
```

##  Installation

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/Calvinky-Lee/AI_ML-Sports-Analysis-System.git
    cd AI_ML-Sports-Analysis-System
    ```

2.  **Install dependencies**:
    ```bash
    pip install ultralytics opencv-python numpy pandas scikit-learn
    ```

## Usage

To run the basic inference on your sample video:

```bash python yolo_learning.py```

*Note: Ensure you have a video file located at `input_videos/sample.mp4` or update the path in the script.*

## Reference

This project is inspired by the comprehensive guide by [Code of a Programmer](https://www.youtube.com/watch?v=neBZ6huolkg).

## License
  
[MIT](LICENSE) (or your preferred license)
