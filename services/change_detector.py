def detect_changes(old_text, new_text):

    old_lines = set(
        line.strip()
        for line in old_text.splitlines()
        if line.strip()
    )

    new_lines = set(
        line.strip()
        for line in new_text.splitlines()
        if line.strip()
    )

    changes = list(new_lines - old_lines)

    return changes