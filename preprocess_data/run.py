from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from utils.paths import DATASET_RAW, EVALUATION_RESULTS


def main() -> None:
    environment = os.environ.copy()
    environment["PYTHONPATH"] = os.pathsep.join(
        [str(ROOT / "src"), environment.get("PYTHONPATH", "")]
    )
    subprocess.run(
        [
            sys.executable,
            "-m",
            "ieee_fraud.profiling",
            "--data-dir",
            str(DATASET_RAW),
            "--output",
            str(EVALUATION_RESULTS / "dataset_profile.json"),
        ],
        check=True,
        env=environment,
    )


if __name__ == "__main__":
    main()

