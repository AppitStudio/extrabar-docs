Examples
========

Real-world examples of what you can build with ExtraBar's deep links, scripts, and shortcuts. Each example shows the action type and URL or command — add them as actions on any app or widget in your bar.

Keyboard Maestro
----------------

*The front door to all your macros*

Trigger any Keyboard Maestro macro from your bar using the ``kmtrigger://`` URL scheme. Use the **Deep Link** action with these templates:

- **Launch Morning Setup** — ``kmtrigger://macro=Launch%20Morning%20Setup``
- **Rename Last Screenshot** — ``kmtrigger://macro=Rename%20Last%20Screenshot``
- **Restart Chosen App** — ``kmtrigger://macro=Restart%20Chosen%20App&value={appName}``
- **Restart KM Engine** — ``kmtrigger://macro=Restart%20KM%20Engine``

Replace the macro name with your own. You can find the exact trigger URL for any macro in Keyboard Maestro's trigger settings. Use the ``&value=`` parameter to pass data into the macro.

BetterTouchTool
---------------

*The command center for your triggers*

Trigger any named trigger using the ``btt://`` URL scheme. Use the **Deep Link** action:

- **Snap Window Left** — ``btt://trigger_named/?trigger_name=Snap%20Window%20Left``
- **Three-Finger Screenshot** — ``btt://trigger_named/?trigger_name=Three-Finger%20Screenshot``
- **Swipe Mute Mic** — ``btt://trigger_named/?trigger_name=Swipe%20Mute%20Mic``
- **Tap Toggle AirPods** — ``btt://trigger_named/?trigger_name=Tap%20Toggle%20AirPods``

Create named triggers in BetterTouchTool first, then reference them by name. Right-click any trigger to copy its UUID if you prefer ``btt://execute_assigned_actions_for_trigger/?uuid={uuid}``.

Raycast
-------

*Make ExtraBar your Raycast dashboard*

Launch Raycast extensions directly from your bar. Use the **Deep Link** action:

- **Google Quick Translate** — ``raycast://extensions/gebeto/translate/quick-translate``
- **Decrypt Base64** — ``raycast://extensions/DanielSinclair/base64/decode``
- **Spotify Volume Control** — ``raycast://extensions/raycast/system/turn-volume-up``
- **Kill Process** — ``raycast://extensions/rolandleth/kill-process/index``

Extension URLs follow the format ``raycast://extensions/{author}/{extension}/{command}``. Find the exact URL in Raycast's extension store or by right-clicking an extension.

Apple Shortcuts
---------------

*Run any shortcut from your menu bar*

Run shortcuts using the ``shortcuts://`` URL scheme or the built-in **Run Shortcut** action. Use the **Deep Link** action for URL-based triggers:

- **Start Meeting Focus** — ``shortcuts://run-shortcut?name=Start%20Meeting%20Focus``
- **Text Wife "OMW"** — ``shortcuts://run-shortcut?name=Text%20Wife%20OMW``
- **Resize for Instagram** — ``shortcuts://run-shortcut?name=Resize%20for%20Instagram``
- **Split PDF Pages** — ``shortcuts://run-shortcut?name=Split%20PDF%20Pages``

Pass input with ``&input=text&text={value}`` or ``&input=clipboard`` to use clipboard contents. Or skip the URL scheme entirely and use the **Run Shortcut** action type, which lets you pick a shortcut by name.

Obsidian
--------

*Your second brain deserves quick access*

Jump to any vault, note, or search using the ``obsidian://`` URL scheme. Use the **Deep Link** action:

- **Open Daily Note** — ``obsidian://open?vault={vaultName}&file=Daily%20Note``
- **Log Quick Idea** — ``obsidian://open?vault={vaultName}&file=Quick%20Ideas``
- **Open Weekly Review** — ``obsidian://open?vault={vaultName}&file=Weekly%20Review``
- **Search Meeting Notes** — ``obsidian://search?vault={vaultName}&query=meeting``

Replace ``{vaultName}`` and file names with your own. File paths are relative to the vault root.

Notion
------

*Every Notion page at your fingertips*

Open any page, database, or block using the ``notion://`` URL scheme. Use the **Deep Link** action:

- **Open Sprint Board** — ``notion://www.notion.so/{pageId}``
- **Open Company Wiki** — ``notion://www.notion.so/{pageId}``
- **Open Team Roadmap** — ``notion://www.notion.so/{pageId}?v={viewId}``
- **Add New Task** — ``notion://www.notion.so/{pageId}``

Get the page ID from any Notion URL — it's the long string at the end. You can also paste the full Notion URL and ExtraBar extracts the IDs automatically.

Things 3
--------

*Every project and view, instantly reachable*

Control Things from your bar using the ``things:///`` URL scheme. Use the **Deep Link** action:

- **Add New To-Do** — ``things:///add?title={title}&notes={notes}``
- **Open Today View** — ``things:///show?id=today``
- **Open Work Project** — ``things:///show?query={projectName}``
- **Open Someday/Maybe** — ``things:///show?id=someday``

Things supports ``inbox``, ``today``, ``upcoming``, ``anytime``, ``someday``, and ``logbook`` as built-in view IDs.

Drafts
------

*Your quickest capture just got quicker*

Capture and process text using the ``drafts://`` URL scheme. Use the **Deep Link** action:

- **Capture Quick Note** — ``drafts://x-callback-url/create?text={text}``
- **Send to Obsidian** — ``drafts://x-callback-url/runAction?text={text}&action=Send%20to%20Obsidian``
- **New Blog Draft** — ``drafts://x-callback-url/create?text={text}&tag=blog``
- **Append Daily Log** — ``drafts://x-callback-url/append?uuid={draftUUID}&text={text}``

The ``runAction`` command triggers any Drafts action by name — set up your workflows in Drafts first, then trigger them from ExtraBar.

Fantastical
-----------

*Add events and check your calendars instantly*

Create events using Fantastical's natural language parsing. Use the **Deep Link** action:

- **Show Today's Events** — ``x-fantastical3://show?date=today``
- **Quick Add Event** — ``x-fantastical3://parse?sentence={event}``
- **Open Week View** — ``x-fantastical3://show/calendar/{yyyy-MM-dd}``
- **Open Team Calendar** — ``x-fantastical3://show/set?name={calendarSetName}``

The ``parse`` command understands natural language — pass something like "Meeting with Alex tomorrow at 2pm" and Fantastical creates the event.

DEVONthink
----------

*Your knowledge base deserves a control panel*

Access databases and documents using the ``x-devonthink://`` URL scheme. Use the **Deep Link** action:

- **Open Research DB** — ``x-devonthink-item://{databaseUUID}``
- **Search All Databases** — ``x-devonthink://search?query={searchTerm}``
- **Open Client Contracts** — ``x-devonthink-item://{groupUUID}``
- **Run OCR Inbox** — Use a **Run Script** action with AppleScript to trigger DEVONthink's OCR on the inbox

Get item UUIDs by selecting a database or group in DEVONthink and choosing Edit > Copy Item Link.

OmniFocus
---------

*Your task system deserves a command center*

Navigate perspectives using the ``omnifocus:///`` URL scheme. Use the **Deep Link** action:

- **Open Inbox** — ``omnifocus:///inbox``
- **Open Projects** — ``omnifocus:///projects``
- **Open Tags** — ``omnifocus:///tags``
- **Show Flagged Tasks** — ``omnifocus:///flagged``
- **Open Review Perspective** — ``omnifocus:///review``
- **Open Forecast** — ``omnifocus:///forecast``

Custom perspectives work too: ``omnifocus:///perspective/{perspectiveName}`` (encode spaces as ``%20``).

Bear
----

*Quick access to your entire library*

Open notes, search, and create using the ``bear://`` URL scheme. Use the **Deep Link** action:

- **Open Pinned Notes** — ``bear://x-callback-url/open-note?title=Pinned``
- **Search #work Tag** — ``bear://x-callback-url/search?term=%23work``
- **Create New Note** — ``bear://x-callback-url/create?title={title}&text={text}``
- **Open Dev Snippets** — ``bear://x-callback-url/search?term=%23snippets``

Use ``%23`` for the ``#`` character when searching by tag.

Craft
-----

*Jump to any project doc instantly*

Open spaces, documents, and daily notes using the ``craftdocs://`` URL scheme. Use the **Deep Link** action:

- **Open Team Space** — ``craftdocs://openspace?spaceId={spaceId}``
- **New Meeting Notes** — ``craftdocs://createdocument?spaceId={spaceId}&title=Meeting%20Notes&folderId={folderId}``
- **Open Design Brief** — ``craftdocs://open?spaceId={spaceId}&blockId={blockId}``
- **Search All Docs** — ``craftdocs://opensearch?spaceId={spaceId}&query={query}``

Get space and document IDs by using File > Copy Deeplink in Craft.

Todoist
-------

*Every project and filter, one click away*

Navigate views and add tasks using the ``todoist://`` URL scheme. Use the **Deep Link** action:

- **Add Quick Task** — ``todoist://addtask?content={taskContent}``
- **Open Today View** — ``todoist://today``
- **Show Priority 1** — ``todoist://filter?id={filterId}``
- **Open Work Project** — ``todoist://project?id={projectId}``

On desktop, you can also use Todoist's global Quick Add shortcut instead of the URL scheme. Find project and filter IDs in Todoist's settings.

1Password
---------

*Your vault, faster than the shortcut*

Search and access items using the ``onepassword://`` URL scheme. Use the **Deep Link** action:

- **Search Vault** — ``onepassword://search/{query}``
- **Copy WiFi Password** — ``onepassword://search/WiFi``
- **Open Secure Notes** — ``onepassword://search/Secure%20Note``
- **Generate New Password** — ``onepassword://extension/generate-password``

GoodTask
--------

*Every list, board and Kanban, one click away*

Open views and add tasks using the ``goodtask3://`` URL scheme. Use the **Deep Link** action:

- **Show Today's Tasks** — ``goodtask3://view?title=Today&view=2``
- **Open Weekly Kanban** — ``goodtask3://view?title=Week&view=11``
- **Add Quick Reminder** — ``goodtask3://add?title={title}&dueAfter=10``
- **Open Board View** — ``goodtask3://view?title=Board&view=12``

View numbers: 1=List, 2=Day, 3=Week, 4=Month, 11=Board (Date), 12=Board (Priority), 13=Board (List), 14=Board (Tag).

Spark Mail
----------

*Email actions without the context switch*

Compose and navigate using the ``readdle-spark://`` URL scheme. Use the **Deep Link** action:

- **Compose New Email** — ``readdle-spark://compose?subject={subject}&recipient={email}``
- **Email Work Contact** — ``readdle-spark://compose?recipient={workEmail}``
- **Open Spark** — ``readdle-spark://``

Spark's URL scheme supports composing emails and opening the app. Specific views like Priority Inbox or search are not available via URL — use Spark's built-in navigation after opening.

Ulysses
-------

*Every sheet and group, instantly reachable*

Open sheets, create new ones, and navigate groups using the ``ulysses://`` URL scheme. Use the **Deep Link** action:

- **Open Current Manuscript** — ``ulysses://x-callback-url/open?id={sheetId}``
- **Create New Sheet** — ``ulysses://x-callback-url/new-sheet?text={text}&group=/My%20Group``
- **Open Blog Drafts** — ``ulysses://x-callback-url/open?id=/Blog%20Drafts``
- **Open Recent Sheets** — ``ulysses://x-callback-url/open-recent``

Get sheet IDs by right-clicking a sheet in Ulysses and copying its callback URL. Group paths use ``/`` as the separator.
