import csv
import os
import shutil
from collections import defaultdict

import supervisely as sly
from dataset_tools.convert import unpack_if_archive
from supervisely.io.fs import (
    file_exists,
    get_file_name,
    get_file_name_with_ext,
    get_file_size,
)
from tqdm import tqdm

import src.settings as s


def convert_and_upload_supervisely_project(
    api: sly.Api, workspace_id: int, project_name: str
) -> sly.ProjectInfo:
    # Possible structure for bbox case. Feel free to modify as you needs.

    images_path = "/home/alex/DATASETS/TODO/pistachios/Pesteh-Set Images"
    ann_path = "/home/alex/DATASETS/TODO/pistachios/annotation.csv"
    batch_size = 30
    ds_name = "ds"

    def create_ann(image_path):
        labels = []

        # image_np = sly.imaging.image.read(image_path)[:, :, 0]
        img_height = 600  # image_np.shape[0]
        img_wight = 1070  # image_np.shape[1]

        ann_data = im_name_to_data[get_file_name_with_ext(image_path)]
        for curr_ann_data in ann_data:
            coords = list(map(int, curr_ann_data))
            if coords[-1] == 0:
                tag = sly.Tag(close_meta)
            else:
                tag = sly.Tag(open_meta)
            left = int(coords[0])
            top = int(coords[1])
            right = int(coords[2])
            bottom = int(coords[3])
            rect = sly.Rectangle(left=left, top=top, right=right, bottom=bottom)
            label = sly.Label(rect, obj_class, tags=[tag])
            labels.append(label)

        return sly.Annotation(img_size=(img_height, img_wight), labels=labels)

    obj_class = sly.ObjClass("pistachio", sly.Rectangle)
    open_meta = sly.TagMeta("open", sly.TagValueType.NONE)
    close_meta = sly.TagMeta("close", sly.TagValueType.NONE)

    project = api.project.create(workspace_id, project_name, change_name_if_conflict=True)
    meta = sly.ProjectMeta(obj_classes=[obj_class], tag_metas=[open_meta, close_meta])
    api.project.update_meta(project.id, meta.to_json())

    im_name_to_data = defaultdict(list)
    with open(ann_path, "r") as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            im_name_to_data[row[0]].append(row[1:])

    dataset = api.dataset.create(project.id, ds_name, change_name_if_conflict=True)

    images_names = os.listdir(images_path)

    progress = sly.Progress("Create dataset {}".format(ds_name), len(images_names))

    for images_names_batch in sly.batched(images_names, batch_size=batch_size):
        img_pathes_batch = [
            os.path.join(images_path, image_name) for image_name in images_names_batch
        ]

        img_infos = api.image.upload_paths(dataset.id, images_names_batch, img_pathes_batch)
        img_ids = [im_info.id for im_info in img_infos]

        anns = [create_ann(image_path) for image_path in img_pathes_batch]
        api.annotation.upload_anns(img_ids, anns)

        progress.iters_done_report(len(images_names_batch))

    return project
