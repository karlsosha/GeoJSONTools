import os
from typing import List

import click
import geojson

from geojson_utils.utils import read_geojson, sort_and_split


@click.group()
def geojson():
    pass


@geojson.command()
@click.option(
    "-m",
    "--max-rows",
    default=20000,
    type=int,
    help="Number of Rows to split file into",
)
@click.option(
    "-d", "--destination-dir", type=str, help="Destination directory for split files"
)
@click.argument("filename")
def split_geojson(max_rows, destination_dir, filename):
    print("Splitting GeoJSON file")
    print(f"max Rows: {max_rows}")
    print(f"filename: {filename}")
    feature_colletion = read_geojson(filename=filename)

    feature_name: str = feature_colletion.name
    features = feature_colletion.features
    new_collection: List[geojson.FeatureCollection] = sort_and_split(
        features=features, max_rows=max_rows
    )
    for idx in range(len(new_collection)):
        new_collection[idx].name = feature_colletion.name + "_part" + str(idx)
        output_filename: str = new_collection[idx].name + ".geojson"
        dest_path: str = output_filename
        if len(destination_dir) > 0:
            dest_path = os.path.join(destination_dir, output_filename)
            os.makedirs(os.path.dirname(destination_dir), exist_ok=True)

        with open(dest_path, "w") as f:
            geojson.dump(new_collection[idx], f)


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    geojson()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
