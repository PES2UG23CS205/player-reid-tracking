
Player Re-Identification and Tracking with YOLO

This project implements real-time player tracking and re-identification in videos using the YOLO object detection framework combined with an advanced tracker (BoT-SORT with ReID support). The system assigns consistent IDs to players—even after they leave the frame and reappear.
🚀 Key Features

    Player Detection: Uses a custom YOLOv8 .pt model to detect players in each frame.

    Advanced Tracking: Tracks players frame-by-frame using the BoT-SORT tracker.

    Re-Identification: Maintains consistent player IDs across occlusions and re-entries using appearance features.

    Output: Generates an annotated video with bounding boxes and consistent player IDs.

📁 Project Structure

text
player-reid-project/
│
├── models/
│   └── best.pt                  # Custom YOLO detection model
│
├── trackers/
│   └── botsort_reid.yaml        # Tracker config file with ReID enabled
│
├── data/
│   └── input/
│       └── sample_video.mp4     # Input video for testing
│
├── runs/                        # Output folder for tracking videos
│
├── main.py                      # Main script to run tracking
├── requirements.txt             # Python dependencies
└── README.md                    # Project documentation

🛠️ Requirements

    Python 3.8 or higher

    PyTorch (compatible with your CUDA version or CPU)

    Ultralytics YOLOv8 (pip install ultralytics)

    Other dependencies listed in requirements.txt

⚙️ Setup

    Clone the repository:

bash
git clone <your-repo-url>
cd player-reid-project

Create and activate a virtual environment:

bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/macOS
source venv/bin/activate

Install dependencies:

    bash
    pip install -r requirements.txt

    Add your trained YOLO model:

        Place your best.pt model file inside the models/ directory.

    Tracker config file:

        Ensure botsort_reid.yaml is inside the trackers/ folder.

        This config must have with_reid: True and the correct ReID model path set.

▶️ Running the Project

To run player tracking and re-identification on a video:

bash
python main.py

This will:

    Load the YOLO .pt model

    Run tracking on the input video specified in main.py

    Display the video with live tracking and IDs

    Save the output video to the runs/track folder

🧠 How It Works

    The YOLO model detects players in each frame.

    BoT-SORT tracker with ReID assigns and maintains unique IDs for each player.

    Appearance features from the ReID model help track players who temporarily leave the frame.

    Handles occlusions, exits, and re-entries, maintaining consistent identities.

💡 Troubleshooting & Tips

    If you run out of memory or face slow execution, try running with stream=True in main.py for inference.

    Ensure your botsort_reid.yaml has all necessary attributes for the tracker, including with_reid: True.

    The project currently supports .pt format for YOLO models (not ONNX).

    Make sure your environment’s PyTorch and Ultralytics versions are compatible and up to date.

📦 Dependencies (requirements.txt)

text
ultralytics>=8.0.20
torch>=1.12.0
opencv-python
numpy

📄 License

This project is licensed under the MIT License.
📬 Contact

For questions or suggestions, please open an issue or contact [gowthammourya9@gmail.c
