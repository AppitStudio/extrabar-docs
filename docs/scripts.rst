Scripts
=======

The Run Script action lets you execute scripts directly from your menu bar. Write a quick shell command, run a Python script, or automate with AppleScript — all triggered with a click or keyboard shortcut.

Adding a script action
----------------------

1. Open ExtraBar and click **Manage** on a preset
2. Click the app settings icon (⚙) on any item
3. Click **+ Add** → **Run Script**
4. Configure the script settings

Script source
-------------

You can provide a script in two ways:

File
   Point to a script file on disk. Use the **Browse** button to select the file, or type the path manually. ExtraBar detects the language from the file extension automatically.

Inline
   Write the script directly in ExtraBar's built-in editor. The editor includes syntax highlighting for all supported languages.

You can also load a file's contents into the inline editor using the **Load from File** button.

Supported languages
-------------------

AppleScript and shell scripts are always available. Other languages are detected automatically — if the interpreter is installed on your Mac, it shows up as an option.

- **AppleScript** — ``.applescript``, ``.scpt``
- **Shell Script** (zsh/bash) — ``.sh``, ``.zsh``, ``.bash``
- **Python** — ``.py``
- **Node.js** — ``.js``, ``.mjs``, ``.cjs``
- **Ruby** — ``.rb``
- **PHP** — ``.php``
- **Perl** — ``.pl``, ``.pm``
- **Lua** — ``.lua``

ExtraBar checks standard paths including ``/usr/bin``, ``/opt/homebrew/bin``, and ``/usr/local/bin`` for interpreters.

Arguments
---------

Add command-line arguments to pass to your script. Each argument is a separate entry — use the arguments editor to add, remove, or reorder them.

Shell environment
-----------------

Control how the shell environment is set up when your script runs. This matters when your script depends on tools installed via Homebrew or custom PATH entries.

Default environment
   No shell profile loading. The script runs with a minimal environment.

zsh (load profile)
   Loads ``.zprofile`` and ``.zlogin``. Use this when your script needs Homebrew or other PATH additions.

zsh (interactive)
   Loads ``.zshrc``. Use this when your script needs aliases or functions from your shell config.

bash (load profile)
   Loads ``.bash_profile`` or ``.profile``.

Output window
-------------

When **Show output window** is enabled (on by default), ExtraBar opens a floating panel that shows live script output as it runs. The window displays:

- Script name and language
- Streaming stdout and stderr output (errors highlighted)
- Exit code when the script finishes
- Auto-closes after 10 seconds on completion (click to keep it open)