"""
This is a boilerplate pipeline 'stacking_regressor_trained_with_all_data'
generated using Kedro 0.17.5
"""

from kedro.pipeline import Pipeline, node
from .nodes import get_stacking_final_model


def create_pipeline():
    return Pipeline(
        [
            node(
                func=get_stacking_final_model,
                inputs=["voting_regressor_BA", "xgbr", "X", "y"],
                outputs="final_model",
                name="final_model_node",
            ),
        ]
    )
