# YRIKKA 1A - Bridging the Synthetic to Real Data Gap

## 🏗️ **Project Overview**

This project was completed as part of the Break Through Tech AI Program in collaboration with the host company YRIKKA. The focus of the project was to address the synthetic-to-real (syn2real) data gap in object detection, where models trained on synthetic data often struggle on real-world images. We used a YOLO-based object detection model to detect five everyday objects: potted plant, chair, cup, vase, and book. The model’s performance was evaluated on synthetic data with intentionally noisy or missing annotations to better reflect real-world labeling challenges. Labels were corrected using CVAT, and model behavior was analyzed using a set of challenging real-world test images. New synthetic data was then generated using YRIKKA’s engine to refine the model and improve its real-world performance.

---

### 👥 **Team Members**


| Name             | GitHub Handle | Contribution                                                             |
|------------------|---------------|--------------------------------------------------------------------------|
| Milderd Nwachukwu-Innocent   | @Mildred1999 | Model training and evaluation, hyperparameter tuning, correct CVAT annotation, EDA, Image collection |
| Katherin Cuautli   | @KatherinCuautli  | Image collection, correct CVAT annotation |
| Taanyaa Haridass Prasad  | @taanyaaharidassprasad06  | Image collection, correct CVAT annotation |
| Idranne Naike      | @    | Image Collection, correct CVAT annotation  |
| Dedeepya Pidaparthi       | @dpidaparthi | Image Collection, correct CVAT annotation |
| Md. Mashiur Rahman Khan   | @mashcodes10 | Collect images from data engine, collect real world images |
| Maha Shanawaz Syeda     | @mahashanawaz | Data Cleaning, Data Preprocessing, Baseline model comparison, Model Optimization, EDA, Image collection |


---
## 🎯 **Project Highlights**

**Example:**

- Developed a YOLO-based object detection model to study the synthetic-to-real data gap in detecting everyday objects.
- Evaluated model performance using noisy and corrected synthetic labels, showing how label quality affects real-world results.
- Used CVAT for label correction and YRIKKA’s synthetic data engine to improve training data and model reliability.

---

## 📊 **Data Exploration**

### Dataset Structure

We have two BTT datasets with comprehensive contextual annotations:

#### Dataset 1: `852a64c6-4bd3-495f-8ff7-f5cc85e34316`
- **Images**: 497 PNG files
- **Annotations**: COCO format JSON with contextual metadata
- **Categories**: 10 object classes

#### Dataset 2: `8e0a5d2d-3ae0-4ff0-b6ee-2d85f7da4fee`
- **Images**: 496 PNG files  
- **Annotations**: COCO format JSON with contextual metadata
- **Categories**: 10 object classes

### Object Categories

The datasets include the following object categories:
- **Chair** - Furniture seating
- **Potted Plant** - Plants in containers
- **Cup** - Drinking vessels
- **Vase** - Decorative containers
- **Book** - Reading materials
- **Pot** - Cooking/storage containers

### Contextual Information

Each image includes rich contextual metadata:

### Context Types
- **Scene**: Environment type (indoor living room, outdoor garden, kitchen, library, etc.)
- **Lighting Conditions**: bright lighting, backlit, spotlight, etc.
- **Blur Effect**: background blur, motion blur, or not specified
- **Occlusion**: object visibility (covered with cloth, behind translucent screen, shadows, etc.)
- **Object Classes**: List of detected objects in the image

### Sample Data Structure
```json
{
    "id": 1,
    "file_name": "example_image.png",
    "labels": ["chair", "cup", "potted plant"],
    "contexts": {
        "blur effect": ["background blur"],
        "scene": ["indoor living room"],
        "occlusion": ["covered with a cloth"],
        "object classes": ["chair", "cup", "potted plant"],
        "lighting conditions": ["bright lighting"]
    }
}
```

## Visualizations

<img width="628" height="351" alt="Screenshot 2025-12-06 120209" src="https://github.com/user-attachments/assets/75feb504-725e-4019-83f6-82a1d9111a49" />


---
## Repository Structure

```
yrikka/
├── README.md                           # This file
├── BTT_Data/                          # Main dataset directory
│   ├── 852a64c6-4bd3-495f-8ff7-f5cc85e34316/
│   │   ├── coco.json                  # COCO annotations with contexts
│   │   └── images/                    # 497 PNG images
│   └── 8e0a5d2d-3ae0-4ff0-b6ee-2d85f7da4fee/
│       ├── coco.json                  # COCO annotations with contexts
│       └── images/                    # 496 PNG images
├── docs/                              # Documentation
│   └── project_specifications.pdf     # Original project overview
├── src/                               # Source code (to be developed)
├── notebooks/                         # Jupyter notebooks for analysis
├── requirements.txt                   # Python dependencies
└── .gitignore                         # Git ignore file
```

## Getting Started

### Prerequisites
```bash
pip install -r requirements.txt
```

### Loading the Dataset

```python
import json
import os
from PIL import Image

def load_dataset(dataset_id):
    """Load BTT dataset with COCO annotations"""
    base_path = f"BTT_Data/{dataset_id}"
    
    # Load annotations
    with open(f"{base_path}/coco.json", 'r') as f:
        annotations = json.load(f)
    
    # Get image paths
    image_dir = f"{base_path}/images"
    
    return annotations, image_dir

# Example usage
dataset1, img_dir1 = load_dataset("852a64c6-4bd3-495f-8ff7-f5cc85e34316")
print(f"Dataset 1: {len(dataset1['images'])} images")
```
---

## 👩🏽‍💻 **Setup and Installation**

### Setting up the repository
1. Clone this repository
2. Create a virtual environment
3. Install dependencies
4. Start working on your assigned tasks

### How to Run the Project

This project is fully contained in a Colab notebook.

1. Open `newYrikkaProject.ipynb` in [Google Colab](https://colab.research.google.com/).
2. Install dependencies by running the first cell.
3. Load the datasets using `dataset_loader.py`.
4. Run all cells sequentially to train and evaluate the model.
5. Results will appear in the notebook output.

---

### Git Workflow
1. Create feature branches for new work
2. Make small, focused commits
3. Use descriptive commit messages
4. Submit pull requests for review

## Project Goals

Bridging the synthetic-to-real (syn2real) data gap in object detection:  
- **Object Detection**: Identifying and localizing objects in images
- **Contextual Understanding**: Leveraging scene context, lighting, and occlusion information
- **Multi-label Classification**: Handling images with multiple objects
- **Robust Recognition**: Working with various lighting conditions and occlusions
- Improve YOLO’s mAP@50 by +0.10 over the baseline model  

## Data Analysis Tasks

1. **Exploratory Data Analysis**
   - Analyze distribution of object categories
   - Study contextual patterns
   - Examine lighting and occlusion effects

2. **Model Development**
   - Implement object detection models
   - Incorporate contextual information
   - Handle multi-label scenarios

3. **Evaluation**
   - Define appropriate metrics
   - Test robustness across contexts
   - Compare different approaches

## Contributing

Please follow these guidelines when contributing:
- Use clear, descriptive commit messages
- Document your code thoroughly
- Include tests for new functionality
- Update documentation as needed


## Results and Key Findings
coming soon....


## Potential Next Steps
1. Correct the class imbalance found in our data
2. Fine tune the model further by utilizing the synthetic images from the YRIKKA data engine  

## Acknowledgements
We would like to thank our Challenge Advisors as well as our AI Studio Coach for all of their help and support throughout the entire project.

