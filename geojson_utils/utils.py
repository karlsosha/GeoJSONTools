import geojson
from typing import List, Set, Mapping, Dict

from geojson import Feature, FeatureCollection

from geojson_utils.support_classes import GeoCoord


def read_geojson(filename: str):
    with open(filename, "r", encoding="utf-8") as f:
        features = geojson.load(f)

    return features


def sort_and_split(features: List[Feature], max_rows: int) -> List[FeatureCollection]:
    segment_starts: Dict[GeoCoord, List[int]] = dict()
    segment_ends: Dict[GeoCoord, List[int]] = dict()
    segment_names: Dict[str, List[int]] = dict()
    for idx in range(0, len(features)):
        segment_name = features[idx]["properties"]["name"]
        if segment_name is not None and len(segment_name) > 0:
            if segment_name in segment_names:
                segment_names[segment_name].append(idx)
            else:
                segment_names[segment_name] = [idx]
            continue
        start_coord = GeoCoord(features[idx]["geometry"]["coordinates"][0])
        end_coord = GeoCoord(features[idx]["geometry"]["coordinates"][-1])
        if start_coord in segment_starts:
            segment_starts[start_coord].append(idx)
        else:
            segment_starts[start_coord] = [idx]
        if end_coord in segment_ends:
            segment_ends[end_coord].append(idx)
        else:
            segment_ends[end_coord] = [idx]

    result: List[FeatureCollection] = []
    new_features: List[Feature] = []
    for name in segment_names:
        for idx in segment_names[name]:
            new_features.append(features[idx])
            if len(new_features) >= max_rows:
                new_feature_collection: FeatureCollection = FeatureCollection(
                    features=new_features, type="FeatureCollection"
                )
                result.append(new_feature_collection)
                new_features = []

    start_coord_list: List[GeoCoord] = list(segment_starts.keys())
    start_coord_list.sort()
    new_features = []
    for start_coord in start_coord_list:
        segment_feature_indices: List[int] = segment_starts[start_coord]
        for idx in range(0, len(segment_feature_indices)):
            new_features.append(features[segment_feature_indices[idx]])
            if len(new_features) >= max_rows:
                new_feature_collection: FeatureCollection = FeatureCollection(
                    features=new_features, type="FeatureCollection"
                )
                result.append(new_feature_collection)

    new_feature_collection: FeatureCollection = FeatureCollection(
        features=new_features,
        type="FeatureCollection",
    )
    result.append(new_feature_collection)

    return result
