# dotfiles

Personal scripts and system configuration for my Mac.


## Scripts

### focus-timer
Terminal focus timer for macOS with a live progress bar, pause/resume, and an audio alert when the session ends. Defaults to 15 minutes; pass a number of minutes as the first argument.

```bash
focus-timer       # 15 minutes
focus-timer 25    # 25 minutes
```

Symlink or copy `scripts/focus-timer` onto your `PATH` to run it from anywhere.

### voiceink-update
Checks for updates to the open-source macOS voice-to-text app [VoiceInk](https://github.com/Beingpax/VoiceInk) by comparing the local build against the latest GitHub commits. If updates are found, it displays the changelog and prompts you to pull and rebuild the app locally — no paid license or automatic updater required.

### downloads-cleanup
Sorts loose files in `~/Downloads` into subfolders by extension (PDFs, Images, Archives, Spreadsheets, etc.), skipping hidden files and anything already filed into a subfolder. Shows a macOS notification when done, with a breakdown of what moved and the folder's total size. Requires Python 3; `notifier.py` must sit alongside it.

```bash
downloads-cleanup             # organize ~/Downloads
downloads-cleanup --dry-run   # preview without moving anything
downloads-cleanup --dir path  # target a different folder
downloads-cleanup --no-notify # skip the notification
```
