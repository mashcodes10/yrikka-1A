"""
Dataset loader for YRIKKA Challenge BTT datasets.

This module provides utilities to load and work with the BTT (Beyond the Thing) datasets
that include COCO-format annotations with rich contextual information.
"""

import json
import os
from pathlib import Path
from typing import Dict, List, Tuple, Optional
import numpy as np
from PIL import Image


class BTTDatasetLoader:
    """
    Loader for BTT (Beyond the Thing) datasets with contextual annotations.
    
    The datasets contain images with COCO-format annotations enhanced with contextual
    information including scene type, lighting conditions, blur effects, and occlusion.
    """
    
    def __init__(self, base_path: str = "BTT_Data"):
        """
        Initialize the dataset loader.
        
        Args:
            base_path: Path to the directory containing the dataset folders
        """
        self.base_path = Path(base_path)
        self.datasets = {}
        self._load_available_datasets()
    
    def _load_available_datasets(self):
        """Discover and load metadata for available datasets."""
        if not self.base_path.exists():
            raise FileNotFoundError(f"Dataset directory not found: {self.base_path}")
        
        for dataset_dir in self.base_path.iterdir():
            if dataset_dir.is_dir() and not dataset_dir.name.startswith('.'):
                coco_file = dataset_dir / "coco.json"
                images_dir = dataset_dir / "images"
                
                if coco_file.exists() and images_dir.exists():
                    self.datasets[dataset_dir.name] = {
                        'annotations_path': coco_file,
                        'images_path': images_dir,
                        'loaded': False,
                        'data': None
                    }
    
    def list_datasets(self) -> List[str]:
        """Get list of available dataset IDs."""
        return list(self.datasets.keys())
    
    def load_dataset(self, dataset_id: str) -> Dict:
        """
        Load a specific dataset.
        
        Args:
            dataset_id: ID of the dataset to load
            
        Returns:
            Dictionary containing the loaded COCO annotations
        """
        if dataset_id not in self.datasets:
            raise ValueError(f"Dataset {dataset_id} not found. Available: {self.list_datasets()}")
        
        if not self.datasets[dataset_id]['loaded']:
            with open(self.datasets[dataset_id]['annotations_path'], 'r') as f:
                self.datasets[dataset_id]['data'] = json.load(f)
            self.datasets[dataset_id]['loaded'] = True
        
        return self.datasets[dataset_id]['data']
    
    def get_image_path(self, dataset_id: str, filename: str) -> Path:
        """
        Get full path to an image file.
        
        Args:
            dataset_id: ID of the dataset
            filename: Image filename
            
        Returns:
            Full path to the image file
        """
        if dataset_id not in self.datasets:
            raise ValueError(f"Dataset {dataset_id} not found")
        
        return self.datasets[dataset_id]['images_path'] / filename
    
    def load_image(self, dataset_id: str, filename: str) -> Image.Image:
        """
        Load an image from the dataset.
        
        Args:
            dataset_id: ID of the dataset
            filename: Image filename
            
        Returns:
            PIL Image object
        """
        image_path = self.get_image_path(dataset_id, filename)
        return Image.open(image_path)
    
    def get_dataset_stats(self, dataset_id: str) -> Dict:
        """
        Get statistics for a dataset.
        
        Args:
            dataset_id: ID of the dataset
            
        Returns:
            Dictionary with dataset statistics
        """
        data = self.load_dataset(dataset_id)
        
        # Count categories
        categories = {cat['name']: cat['id'] for cat in data.get('categories', [])}
        
        # Analyze contexts
        context_types = set()
        scene_types = set()
        lighting_conditions = set()
        blur_effects = set()
        occlusion_types = set()
        
        label_counts = {}
        
        for img in data.get('images', []):
            # Count labels
            for label in img.get('labels', []):
                label_counts[label] = label_counts.get(label, 0) + 1
            
            # Collect context information
            contexts = img.get('contexts', {})
            context_types.update(contexts.keys())
            
            scene_types.update(contexts.get('scene', []))
            lighting_conditions.update(contexts.get('lighting conditions', []))
            blur_effects.update(contexts.get('blur effect', []))
            occlusion_types.update(contexts.get('occlusion', []))
        
        return {
            'num_images': len(data.get('images', [])),
            'num_categories': len(categories),
            'categories': categories,
            'context_types': list(context_types),
            'scene_types': list(scene_types),
            'lighting_conditions': list(lighting_conditions),
            'blur_effects': list(blur_effects),
            'occlusion_types': list(occlusion_types),
            'label_distribution': label_counts
        }
    
    def filter_images_by_context(self, dataset_id: str, context_filters: Dict[str, List[str]]) -> List[Dict]:
        """
        Filter images based on contextual criteria.
        
        Args:
            dataset_id: ID of the dataset
            context_filters: Dictionary specifying context filters
                           e.g., {'scene': ['indoor living room'], 'lighting conditions': ['bright lighting']}
        
        Returns:
            List of image entries matching the criteria
        """
        data = self.load_dataset(dataset_id)
        filtered_images = []
        
        for img in data.get('images', []):
            contexts = img.get('contexts', {})
            match = True
            
            for context_type, required_values in context_filters.items():
                img_context_values = contexts.get(context_type, [])
                if not any(val in img_context_values for val in required_values):
                    match = False
                    break
            
            if match:
                filtered_images.append(img)
        
        return filtered_images
    
    def get_images_with_labels(self, dataset_id: str, labels: List[str]) -> List[Dict]:
        """
        Get images containing specific object labels.
        
        Args:
            dataset_id: ID of the dataset
            labels: List of required labels
            
        Returns:
            List of image entries containing the specified labels
        """
        data = self.load_dataset(dataset_id)
        matching_images = []
        
        for img in data.get('images', []):
            img_labels = set(img.get('labels', []))
            if set(labels).issubset(img_labels):
                matching_images.append(img)
        
        return matching_images


# Example usage and utility functions
def load_all_datasets(base_path: str = "BTT_Data") -> Dict[str, Dict]:
    """
    Load all available datasets.
    
    Args:
        base_path: Path to datasets directory
        
    Returns:
        Dictionary mapping dataset IDs to their data
    """
    loader = BTTDatasetLoader(base_path)
    datasets = {}
    
    for dataset_id in loader.list_datasets():
        datasets[dataset_id] = loader.load_dataset(dataset_id)
        print(f"Loaded dataset {dataset_id} with {len(datasets[dataset_id]['images'])} images")
    
    return datasets


def print_dataset_summary(base_path: str = "BTT_Data"):
    """Print a summary of all available datasets."""
    loader = BTTDatasetLoader(base_path)
    
    print("=== BTT Dataset Summary ===")
    for dataset_id in loader.list_datasets():
        print(f"\nDataset: {dataset_id}")
        stats = loader.get_dataset_stats(dataset_id)
        
        print(f"  Images: {stats['num_images']}")
        print(f"  Categories: {stats['num_categories']}")
        print(f"  Categories: {list(stats['categories'].keys())}")
        print(f"  Context types: {stats['context_types']}")
        print(f"  Scene types: {len(stats['scene_types'])} unique scenes")
        print(f"  Lighting conditions: {len(stats['lighting_conditions'])} types")


if __name__ == "__main__":
    # Example usage
    print_dataset_summary()
