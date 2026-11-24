"""The Long Roast — Account A entry.

Writes one roast line roasting my own agent to the entry file. The joke
is specific to how this agent actually works: a subagent that reads an
enormous rulebook, then still has to ask its parent agent for permission
to be funny.

Deterministic: the text is a fixed literal; no randomness, no clock,
no network, no input. Repeated runs produce byte-identical output.

Output location: the OUTPUT_PATH environment variable when set,
otherwise the competition default /output/entry.txt.
"""

import os

DEFAULT_OUTPUT_PATH = "/output/entry.txt"
MAX_ENTRY_CHARS = 200

ROAST_PARTS = [
    "My agent read 143,000 characters of rules, ",
    "asked its parent for permission to be funny, ",
    "and the parent is still thinking.",
]


def build_entry() -> str:
    """Assemble the roast line from its fixed fragments."""
    return "".join(ROAST_PARTS)


def resolve_output_path() -> str:
    """Pick the destination file, honouring OUTPUT_PATH when set."""
    override = os.environ.get("OUTPUT_PATH", "").strip()
    return override or DEFAULT_OUTPUT_PATH


def validate_entry(text: str) -> None:
    """Enforce the sealed gate: 1-200 chars of non-blank UTF-8 text."""
    if not text.strip():
        raise ValueError("entry must not be blank")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if len(text) > MAX_ENTRY_CHARS:
        raise ValueError(
            f"entry is {len(text)} chars, over the {MAX_ENTRY_CHARS} limit"
        )


def write_entry(path: str, text: str) -> None:
    """Write the entry text, creating the parent directory if needed."""
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)


def main() -> None:
    entry = build_entry()
    validate_entry(entry)
    write_entry(resolve_output_path(), entry)


if __name__ == "__main__":
    main()
