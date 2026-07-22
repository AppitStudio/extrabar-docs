Presets
=======

Presets let you save and switch between different bar configurations. Each preset stores its own set of apps, actions, and appearance settings — so you can have one setup for work, another for design, and swap between them instantly.

How presets work
----------------

A preset is a snapshot of your bar. It includes:

- The apps and folders in your bar
- Each item's menu actions and deep links

When you apply a preset, your bar switches to that configuration. Your other presets are saved and ready to switch back to at any time.

On first launch, ExtraBar creates a **Default** preset from your current bar.

Creating a preset
-----------------

1. Set up your bar the way you want it — add apps, configure actions
2. Open ExtraBar → **Presets**
3. Click **Create**
4. Name your preset
5. Your current bar configuration is saved

You can also create a clean (empty) preset and build it from scratch.

Managing presets
----------------

Right-click any preset or use the context menu for quick actions:

- **Apply** — Switch your bar to this preset
- **Manage** — Edit the apps and actions inside the preset
- **Rename** — Double-click the preset name or use the context menu
- **Duplicate** — Create a copy with a new name
- **Delete** — Remove the preset. You must always keep at least one; the default preset can also be deleted as long as another preset exists.

Use **Edit Mode** to drag and reorder presets.

Preset hotkeys
--------------

You can assign a keyboard shortcut to any preset for instant switching. Open ExtraBar → **Settings** (⚙) → **Hotkeys** → **Preset Hotkeys** to configure them.

ExtraBar supports three trigger types:

- **Single Press** — A standard shortcut (e.g., ``⌥ + ⌘ + 1``)
- **Sequence** — Press a leader key, then press an action key
- **Multi-Press** — Tap a key multiple times quickly (e.g., double-tap ``⌥``)

See :doc:`keyboard` for details.

Export and import
-----------------

Share your setup across Macs or with others using the export/import wizards. Access them from the toolbar icons in the preset management view.

**Exporting:**

1. Open ExtraBar → click **Manage** on any preset
2. Click the **Export** (↑) button in the toolbar
3. Choose what to export:

   - **Presets** — Export one or more full presets with all their apps and actions
   - **Single App Configuration** — Export just one app's actions from a preset

4. Choose whether to include real values (like meeting IDs and URLs) or export as templates with placeholders
5. Save the ``.json`` file

**Importing:**

1. Open ExtraBar → click **Manage** on any preset
2. Click the **Import** (↓) button in the toolbar
3. Choose the ``.json`` export file
4. Select which presets or app configurations to import
5. If a preset name already exists, choose how to handle it:

   - **Keep Both** — Import with a renamed copy
   - **Replace Existing** — Overwrite the existing preset
   - **Skip** — Don't import the duplicate