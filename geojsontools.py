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
    feature_collection = read_geojson(filename=filename)
    destination_directory = os.path.join(os.path.dirname(filename), destination_dir)

    feature_name: str = feature_collection.name
    features = feature_collection.features
    new_collection: List[geojson.FeatureCollection] = sort_and_split(
        features=features, max_rows=max_rows
    )
    for idx in range(len(new_collection)):
        new_collection[idx].name = feature_name + "_part" + str(idx+1)
        output_filename: str = new_collection[idx].name + ".geojson"
        dest_path: str = os.path.join(str(destination_directory), output_filename)
        os.makedirs(str(destination_directory), exist_ok=True)

        with open(dest_path, "w") as f:
            geojson.dump(new_collection[idx], f)


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    geojson()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
