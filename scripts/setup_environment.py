#!/usr/bin/env python3
"""
Environment setup script for YRIKKA Challenge project.

This script helps set up the development environment and verifies
that all required dependencies are installed correctly.
"""

import sys
import subprocess
import importlib
import os
from pathlib import Path


def check_python_version():
    """Check if Python version is compatible."""
    print("Checking Python version...")
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print(f"❌ Python {version.major}.{version.minor} detected. Python 3.8+ required.")
        return False
    print(f"✅ Python {version.major}.{version.minor}.{version.micro} is compatible")
    return True


def install_requirements():
    """Install required packages from requirements.txt."""
    requirements_file = Path(__file__).parent.parent / "requirements.txt"
    if not requirements_file.exists():
        print("❌ requirements.txt not found")
        return False
    
    print("Installing requirements...")
    try:
        subprocess.check_call([
            sys.executable, "-m", "pip", "install", "-r", str(requirements_file)
        ])
        print("✅ Requirements installed successfully")
        return True
    except subprocess.CalledProcessError:
        print("❌ Failed to install requirements")
        return False


def verify_imports():
    """Verify that key packages can be imported."""
    required_packages = [
        'numpy', 'pandas', 'matplotlib', 'seaborn', 'PIL', 
        'torch', 'torchvision', 'cv2', 'sklearn'
    ]
    
    print("Verifying package imports...")
    failed_imports = []
    
    for package in required_packages:
        try:
            if package == 'PIL':
                importlib.import_module('PIL')
            elif package == 'cv2':
                importlib.import_module('cv2')
            else:
                importlib.import_module(package)
            print(f"✅ {package}")
        except ImportError:
            print(f"❌ {package}")
            failed_imports.append(package)
    
    if failed_imports:
        print(f"\n❌ Failed to import: {', '.join(failed_imports)}")
        return False
    
    print("✅ All required packages imported successfully")
    return True


def check_dataset_structure():
    """Check if dataset files are properly structured."""
    print("Checking dataset structure...")
    project_root = Path(__file__).parent.parent
    btt_data_path = project_root / "BTT_Data"
    
    if not btt_data_path.exists():
        print("❌ BTT_Data directory not found")
        return False
    
    # Check for dataset directories
    dataset_dirs = [d for d in btt_data_path.iterdir() if d.is_dir() and not d.name.startswith('.')]
    
    if len(dataset_dirs) == 0:
        print("❌ No dataset directories found in BTT_Data")
        return False
    
    print(f"✅ Found {len(dataset_dirs)} dataset directories")
    
    # Check each dataset
    for dataset_dir in dataset_dirs:
        coco_file = dataset_dir / "coco.json"
        images_dir = dataset_dir / "images"
        
        if not coco_file.exists():
            print(f"❌ Missing coco.json in {dataset_dir.name}")
            return False
            
        if not images_dir.exists():
            print(f"❌ Missing images directory in {dataset_dir.name}")
            return False
        
        # Count images
        image_files = list(images_dir.glob("*.png"))
        print(f"✅ Dataset {dataset_dir.name}: {len(image_files)} images")
    
    return True


def create_directory_structure():
    """Create any missing directories."""
    print("Checking directory structure...")
    project_root = Path(__file__).parent.parent
    
    required_dirs = [
        "src", "notebooks", "scripts", "docs", 
        "models", "results", "logs"
    ]
    
    for dir_name in required_dirs:
        dir_path = project_root / dir_name
        if not dir_path.exists():
            dir_path.mkdir(exist_ok=True)
            print(f"✅ Created directory: {dir_name}")
        else:
            print(f"✅ Directory exists: {dir_name}")


def run_basic_tests():
    """Run basic functionality tests."""
    print("Running basic tests...")
    
    try:
        # Test dataset loader
        sys.path.insert(0, str(Path(__file__).parent.parent / "src"))
        from dataset_loader import BTTDatasetLoader
        
        loader = BTTDatasetLoader("../BTT_Data")
        datasets = loader.list_datasets()
        
        if not datasets:
            print("❌ No datasets found")
            return False
        
        print(f"✅ Found datasets: {datasets}")
        
        # Test loading first dataset
        first_dataset = datasets[0]
        stats = loader.get_dataset_stats(first_dataset)
        print(f"✅ Loaded dataset {first_dataset} with {stats['num_images']} images")
        
        return True
        
    except Exception as e:
        print(f"❌ Test failed: {str(e)}")
        return False


def main():
    """Run all setup and verification steps."""
    print("🚀 Setting up YRIKKA Challenge environment...\n")
    
    steps = [
        ("Python version", check_python_version),
        ("Dataset structure", check_dataset_structure),
        ("Directory structure", create_directory_structure),
        ("Package installation", install_requirements),
        ("Import verification", verify_imports),
        ("Basic functionality", run_basic_tests),
    ]
    
    failed_steps = []
    
    for step_name, step_func in steps:
        print(f"\n{'='*50}")
        print(f"Step: {step_name}")
        print(f"{'='*50}")
        
        try:
            if not step_func():
                failed_steps.append(step_name)
        except Exception as e:
            print(f"❌ Error in {step_name}: {str(e)}")
            failed_steps.append(step_name)
    
    print(f"\n{'='*50}")
    print("Setup Summary")
    print(f"{'='*50}")
    
    if failed_steps:
        print(f"❌ Setup failed. Issues with: {', '.join(failed_steps)}")
        print("Please resolve these issues before proceeding.")
        return False
    else:
        print("✅ Environment setup completed successfully!")
        print("You can now start working with the YRIKKA Challenge datasets.")
        print("\nNext steps:")
        print("1. Open notebooks/dataset_exploration.ipynb to explore the data")
        print("2. Check out src/dataset_loader.py for data loading utilities")
        print("3. Review the README.md for project overview")
        return True


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
