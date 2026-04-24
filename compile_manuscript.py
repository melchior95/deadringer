"""
Compile Dead Ringer manuscript from individual chapter files.

Concatenates all chapter files and the epilogue into dead_ringer_complete.md.
Run this after editing any chapter file to keep the master manuscript in sync.
"""

from pathlib import Path

CHAPTERS = [
    "preface.md",
    "chapter_01.md",
    "chapter_02.md",
    "chapter_03.md",
    "chapter_04.md",
    "chapter_05.md",
    "chapter_06.md",
    "chapter_07.md",
    "chapter_08.md",
    "chapter_09.md",
    "chapter_10.md",
    "chapter_11.md",
    "chapter_12.md",
    "epilogue.md",
]

OUTPUT = "dead_ringer_complete.md"


def compile_manuscript():
    root = Path(__file__).parent
    sections = []

    for filename in CHAPTERS:
        path = root / filename
        if not path.exists():
            print(f"WARNING: {filename} not found, skipping")
            continue
        text = path.read_text(encoding="utf-8")
        sections.append(text.rstrip())

    manuscript = "\n\n".join(sections) + "\n"

    out_path = root / OUTPUT
    out_path.write_text(manuscript, encoding="utf-8")
    print(f"Compiled {len(sections)} files -> {OUTPUT} ({len(manuscript):,} chars)")


if __name__ == "__main__":
    compile_manuscript()
