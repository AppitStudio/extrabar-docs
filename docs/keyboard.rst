Keyboard Navigation
====================

ExtraBar is built for keyboard-driven workflows. You can navigate the bar, open menus, and execute actions entirely from the keyboard — in both floating bar and menu bar modes.

Activating keyboard mode
-------------------------

There are two ways to enter keyboard mode:

- ``⌥ + ⌘ + B`` — Toggle bar visibility and activate keyboard mode
- ``⌥ + ⌘ + F`` — Activate keyboard mode when the bar is already visible

When keyboard mode is active, hotkey badges appear on each icon showing its shortcut key.

Keyboard mode automatically deactivates after 10 seconds of inactivity. Any key press resets the timer.

Quick selection
---------------

Once keyboard mode is active, use number and letter keys to jump directly to an item:

- ``1`` – ``9`` — Select items 1 through 9
- ``A`` – ``Z`` — Select items 10 through 35

Selecting an item opens its action menu immediately.

Navigation
----------

- **Left / Right arrow** — Move focus between items
- **Tab** — Move to the next item
- **Shift + Tab** — Move to the previous item
- **Enter** or **Space** — Open the menu for the focused item
- **Escape** — Exit keyboard mode

In-menu navigation
-------------------

When an action menu is open:

- ``1`` – ``9`` — Select and execute action 1 through 9
- **Enter** — Execute the highlighted action
- **Escape** — Close the menu

Click behavior modes
---------------------

ExtraBar has two click behavior modes that control what happens when you click or select an item:

Open Menu
   The action menu opens showing all configured actions. This is the default.

Launch App
   The app launches directly. The menu still opens with "Open" as the first option — press ``1`` or Enter to launch quickly.

Change this in ExtraBar → **Settings** (⚙) → **Keyboard**.

Menu bar mode
--------------

Keyboard navigation also works in menu bar mode. Pressing the toggle or focus hotkey activates keyboard navigation directly on the menu bar status items. Hotkey badges and focus indicators appear on the icons.

Accessibility permission
-------------------------

Full keyboard navigation works without any permissions when ExtraBar is the active app. For global keyboard shortcuts that work from any app, grant Accessibility permission:

**System Settings** → **Privacy & Security** → **Accessibility** → add ExtraBar.

Global hotkeys
--------------

Open ExtraBar → **Settings** (⚙) → **Hotkeys** to customize them.

- ``⌥ + ⌘ + B`` — Toggle bar visibility (customizable)
- ``⌥ + ⌘ + F`` — Activate keyboard focus (customizable)
- ``⌥ + ⌘ + M`` — Switch between floating bar and menu bar mode (customizable)
- ``⇧ + ⌘ + B`` — Open Bookmark Manager

Preset hotkeys
--------------

Assign keyboard shortcuts to presets for instant switching. Three trigger types are available:

Single Press
   A standard shortcut (e.g., ``⌥ + ⌘ + 1``).

Key Sequence
   Press a leader key to enter scope mode, then press an action key to switch to the preset. Configure the leader key and scope timeout (1–10 seconds) in the advanced settings.

Multi-Press
   Tap a key multiple times quickly (e.g., double-tap ``⌥``). Configure the detection window (200–1000ms) in the advanced settings.

Configure preset hotkeys in ExtraBar → **Settings** (⚙) → **Keyboard** → **Preset Hotkeys**.
