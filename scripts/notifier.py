"""macOS notification helper for the Downloads organizer."""

import subprocess


def _escape(text: str) -> str:
    return text.replace("\\", "\\\\").replace('"', '\\"')


def send_notification(title: str, message: str) -> None:
    """Show a macOS notification via osascript. Fails silently if unavailable."""
    script = f'display notification "{_escape(message)}" with title "{_escape(title)}"'
    try:
        subprocess.run(["osascript", "-e", script], check=True, capture_output=True)
    except (FileNotFoundError, subprocess.CalledProcessError):
        pass
