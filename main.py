import os
from ultralytics import YOLO

def main():
    print("Current working directory:", os.getcwd())

    # Load your trained YOLO model
    model = YOLO("models/best.pt")  # Update if needed

    # Run tracking with stream=True for memory efficiency
    results = model.track(
        source="data/input/15sec_input_720p.mp4",  # Update your input video path
        stream=True,
        save=True,
        show=True,                 # Set to False if you don't want a popup window
        save_dir="runs/track"      # Explicit output folder
    )

    # 'results' is a generator of Results objects, print saved paths per frame
    print("Tracking complete.")
    print("Output files saved:")

    for i, r in enumerate(results):
        if hasattr(r, 'path'):
            print(f"Frame {i} saved to: {r.path}")

if __name__ == "__main__":
    main()
