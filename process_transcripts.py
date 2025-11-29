import re
from pathlib import Path


def read_transcript(file_path: Path) -> str:
    """
    Reads a transcript from a text file and returns its content.
    """
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    return content


def process_transcript(file_path: Path) -> list[str]:
    """
    Processes a transcript file to extract relevant contents

    Args:
        file_path: Path to the transcript text file.

    Returns:
        A list of lines from the transcript omitting the metadata section and any titles.
    """
    transcript = read_transcript(file_path)
    res: list[str] = []

    punctuation = {".", "!", "?", ":", ";", ","}
    for line in transcript.splitlines():
        # Skip lines that don't end with punctuation. These are things like section
        #   titles, headings, speaker, etc.
        if not any(line.strip().endswith(p) for p in punctuation):
            continue
        # Split the line on punctuation but don't match abbreviations and titles
        parts = re.split(r"(?<!\b[A-Za-z])(?<!\bDr\.)(?<=[.!?])\s+(?=[A-Z])", line)
        res.extend(parts)

    return res


if __name__ == "__main__":
    path = Path(".") / "transcripts" / "lly-2025-q3.txt"
    process_transcript(path)
