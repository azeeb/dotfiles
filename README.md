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
