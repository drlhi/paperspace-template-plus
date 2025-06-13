import pathlib


def find_files_with_endashO():
    root = pathlib.Path(__file__).resolve().parents[1]
    problematic = []
    for path in root.rglob('*'):
        if path.is_file() and '.git' not in path.parts:
            try:
                text = path.read_text(encoding='utf-8')
            except Exception:
                try:
                    text = path.read_text(encoding='latin-1')
                except Exception:
                    continue
            if '–' + 'O' in text:
                problematic.append(str(path.relative_to(root)))
    return problematic


def test_no_endash_O():
    problematic = find_files_with_endashO()
    en_dash = '–'
    sequence = en_dash + 'O'
    assert not problematic, f"Found forbidden sequence {sequence!r} in files: {problematic}"
