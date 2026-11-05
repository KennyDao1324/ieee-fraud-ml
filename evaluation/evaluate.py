from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from utils.paths import CHECKPOINT


def main() -> None:
    card = json.loads((CHECKPOINT / "model_card.json").read_text(encoding="utf-8"))
    metrics = card["test_metrics"]
    print(f"Selected model: {card['winner']}")
    print(f"ROC-AUC: {metrics['roc_auc']:.4f}")
    print(f"PR-AUC: {metrics['pr_auc']:.4f}")
    print(f"Recall: {metrics['recall']:.4f}")
    print(f"False-positive rate: {metrics['false_positive_rate']:.4f}")
    if "competition_prediction_rows" in card:
        print(f"Competition predictions: {card['competition_prediction_rows']:,}")


if __name__ == "__main__":
    main()

