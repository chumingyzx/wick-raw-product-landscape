from __future__ import annotations

import os
import shutil
import subprocess
import sys
from pathlib import Path


def run(args: list[str], cwd: Path) -> None:
    print('+', ' '.join(args))
    subprocess.run(args, cwd=cwd, check=True, env={**os.environ, 'PYTHONPATH': str(cwd)})


def compile_twice(tex_name: str, cwd: Path, output_name: str) -> None:
    for _ in range(2):
        run(['pdflatex', '-interaction=nonstopmode', '-halt-on-error', tex_name], cwd)
    shutil.copy2(cwd / Path(tex_name).with_suffix('.pdf'), cwd / output_name)


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    run([sys.executable, '-m', 'pytest', '-q'], root)
    run([sys.executable, '-m', 'src.audit'], root)
    run([sys.executable, 'scripts/generate_results.py'], root)
    run([sys.executable, 'scripts/make_plots.py'], root)
    compile_twice('main.tex', root / 'paper', 'Wick_Raw_Product_Landscape_Preprint_v0.3.1.pdf')
    compile_twice('response.tex', root / 'response', 'Response_to_v0.3_Formula_Level_ReAudit_v0.3.1.pdf')


if __name__ == '__main__':
    main()
