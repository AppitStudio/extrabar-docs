Actions
=======

Actions are what ExtraBar executes when you click an item or press its shortcut. Every app in your bar has a menu of actions — open, quit, run a script, open a deep link, and more.

Adding an action
----------------

1. Open ExtraBar and click **Manage** on a preset
2. Click the app settings icon (⚙) on any item
3. Click **+ Add** to open the Action Library
4. Choose an action type

If the app has a built-in preset, you will also see app-specific actions at the top of the library with smart defaults ready to use.

Action types
------------

ExtraBar provides 17 action types. Here is every action and what it does.

**Basic**

- **Open** — Opens the application or folder.
- **Quit** — Quits the running application. Only available for apps.
- **Force Quit** — Force quits the application. Use when an app is unresponsive.
- **Show in Finder** — Reveals the item in Finder.
- **Copy Path** — Copies the file path to the clipboard.

**Window Management**

- **New Window** — Opens a new window for the application.
- **Hide** — Hides the running application.
- **Show** — Shows a previously hidden application.
- **Close All Windows** — Closes all windows but keeps the app running.

**Open With**

- **Open Item With** — Opens the item with a specific application. Requires you to choose the target app.
- **Open Using App** — Opens a specific file or folder using this application. Useful for IDEs — for example, open a project folder with VS Code.
- **Open In Terminal** — Opens the folder in Terminal. Works with folders and applications (opens the app's parent directory).

**Deep Links**

- **Deep Link** — Opens a deep link URL in the target application. Requires a template URL with parameters. See the Deep Links section for details on supported apps and URL formats.

**Automation**

- **Run Script** — Executes a custom script. Supports shell scripts and AppleScript. You can provide a script file or write the script inline. Configure the script source, arguments, shell environment, and output window.
- **Run Shortcut** — Runs a macOS Shortcut by name.
- **Keyboard Shortcut** — Simulates pressing a keyboard shortcut in the target application. Configure the key, modifiers (Command, Option, Control, Shift), and whether to restore app focus after execution.

**File Operations**

- **Duplicate** — Duplicates the file or folder.

Which actions are available
---------------------------

Not every action works with every item type:

- **Apps** — All actions are available
- **Folders** — Open, Show in Finder, Open in Terminal, Duplicate, Copy Path, and automation actions
- **Widgets** — Actions depend on the widget type

Some actions require parameters before they can run. The Action Library marks these and guides you through configuration.

Menu search
-----------

Menus with many actions can be made **searchable** — enable the search toggle in the menu toolbar to get a search field at the top of the action menu.

Trigger actions from outside ExtraBar
-------------------------------------

Any configured action can be copied as an ``extrabar://`` deep link from its context menu and triggered from other tools — see :doc:`deeplinks` for details.
