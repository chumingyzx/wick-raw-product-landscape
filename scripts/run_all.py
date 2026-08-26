from __future__ import annotations

import os
import shutil
import subprocess
import sys
from pathlib import Path


def run(args: list[str], cwd: Path) -> None:
    print('+', ' '.join(args))
    subprocess.run(args, cwd=cwd, check=True, env={**os.environ, 'PYTHONPATH': str(cwd)})


def build_manuscript(root: Path) -> None:
    paper = root / 'paper'
    for _ in range(2):
        run(['pdflatex', '-interaction=nonstopmode', '-halt-on-error', 'main.tex'], paper)
    built = paper / 'main.pdf'
    target = paper / 'Wick_Raw_Product_Landscape_Preprint_v0.3.1.pdf'
    shutil.copy2(built, target)
    built.unlink(missing_ok=True)


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    run([sys.executable, '-m', 'pytest', '-q'], root)
    run([sys.executable, '-m', 'src.audit'], root)
    run([sys.executable, 'scripts/generate_results.py'], root)
    run([sys.executable, 'scripts/make_plots.py'], root)
    build_manuscript(root)


if __name__ == '__main__':
    main()
