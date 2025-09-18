import json
import os
import csv

# Paths to needed files
imgs = "BTT_Data/8e0a5d2d-3ae0-4ff0-b6ee-2d85f7da4fee/images"
coco_json = "BTT_Data/8e0a5d2d-3ae0-4ff0-b6ee-2d85f7da4fee/coco.json"
output_json = "BTT_Data/clean/clean_coco.json"
dropped_csv = "BTT_Data/clean/dropped_annotations.csv"

subset_limit = None

# Load coco.json
with open(coco_json, 'r') as f:
    data = json.load(f)

# index images by id (easy look up)
img_dict = {img["id"]: img for img in data.get("images", [])}

# limit for testing
annotations = data.get("annotations", [])
if subset_limit:
    annotations = annotations[:subset_limit]

clean_annotations = []
dropped_annotations = []


# process annotations
for ann in annotations:
    ann_id = ann.get("id")
    image_id = ann.get("image_id")
    bbox = ann.get("bbox", None)

    # check if image exists
    img_entry = img_dict.get(image_id)
    if not img_entry or not os.path.exists(os.path.join(imgs, img_entry["file_name"])):
        ann["drop_reason"] = "missing image"
        dropped_annotations.append(ann)
        continue

    # check if bbox exists
    if not bbox or len(bbox) != 4:
        ann["drop_reason"] = "missing bbox"
        dropped_annotations.append(ann)
        continue

    x, y, w, h = bbox

    # validate bbox
    if w <= 0 or h <= 0:
        ann["drop_reason"] = "zero/negative width or height"
        dropped_annotations.append(ann)
        continue
    if x < 0 or y < 0:
        ann["drop_reason"] = "negative x or y"
        dropped_annotations.append(ann)
        continue

    # passed all checks
    clean_annotations.append(ann)

# update json
data["annotations"] = clean_annotations

with open(output_json, 'w') as f:
    json.dump(data, f, indent=4)

# save dropped annotations (this is the flag list)
with open(dropped_csv, "w", newline="") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=["id", "image_id", "category_id", "bbox", "drop_reason"])
    writer.writeheader()
    for ann in dropped_annotations:
        writer.writerow({
            "id": ann.get("id"),
            "image_id": ann.get("image_id"),
            "category_id": ann.get("category_id"),
            "bbox": ann.get("bbox"),
            "drop_reason": ann.get("drop_reason")
        })

print(f"Saved cleaned annotations to {output_json}")
print(f"Dropped {len(dropped_annotations)} annotations (see {dropped_csv})")