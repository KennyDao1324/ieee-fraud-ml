from pathlib import Path


def test_team_workflow_folders_exist():
    root = Path(__file__).resolve().parents[1]
    required = {
        "checkpoint",
        "dataset",
        "evaluation",
        "preprocess_data",
        "preprocessed_df",
        "training_model",
        "utils",
    }
    assert all((root / name).is_dir() for name in required)
    assert (root / "dataset" / "raw").resolve() == (root / "data" / "raw").resolve()
    assert (root / "evaluation" / "results").resolve() == (root / "outputs").resolve()

