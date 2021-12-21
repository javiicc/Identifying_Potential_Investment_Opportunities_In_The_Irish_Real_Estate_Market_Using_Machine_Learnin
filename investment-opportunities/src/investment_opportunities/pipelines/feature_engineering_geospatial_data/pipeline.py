from kedro.pipeline import Pipeline, node

from .nodes import location_feature_engineering, add_geonames



def create_pipeline(**kwargs):
    return Pipeline(
        [
            node(
                func=location_feature_engineering,
                inputs="df_no_outliers",
                outputs="ads_with_location_features",
                name="location_feature_engineering_node",
            ),
            node(
                func=add_geonames,
                inputs=["ads_with_location_features", "geonames"],
                outputs="ads_with_location_features_and_geonames",
                name="add_geonames_node",
            ),
        ]
    )