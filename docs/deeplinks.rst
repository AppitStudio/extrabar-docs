Deep Links
==========

Deep links are URL schemes that open specific content inside an app — a Figma file, a Zoom meeting, a Spotify playlist. Instead of just launching the app, you land exactly where you need to be.

Adding a deep link
------------------

1. Open ExtraBar and click **Manage** on a preset
2. Click the app settings icon (⚙) on any item
3. Click **+ Add** → **Deep Link**
4. Choose a built-in template or enter a custom URL

If the app has a built-in preset, deep link templates appear in the action library with parameters ready to fill in.

How templates work
------------------

A deep link template is a URL with ``{placeholders}`` for the parts that change. When you add the action, ExtraBar asks you to fill in each placeholder.

Example — joining a Zoom meeting::

   Template:  zoommtg://zoom.us/join?confno={meetingId}&pwd={password}
   You fill:  meetingId = 85119634551, password = abc123
   Result:    zoommtg://zoom.us/join?confno=85119634551&pwd=abc123

Once saved, clicking the action opens that exact meeting every time.

Built-in templates
------------------

ExtraBar includes ready-made deep link templates for many apps. When you add a deep link to one of these apps, the templates show up automatically. Here are a few examples.

**Zoom**

- **Join Meeting** — ``zoommtg://zoom.us/join?confno={meetingId}&pwd={password}``

Paste a Zoom invite link or meeting details text and ExtraBar extracts the meeting ID and password automatically.

**Figma**

- **Open File** — ``figma://file/{fileKey}``
- **Open File at Node** — ``figma://file/{fileKey}?node-id={nodeId}``

Paste a Figma URL and ExtraBar extracts the file key and node ID. Works with ``/design/``, ``/file/``, ``/proto/``, and ``/board/`` URLs.

**Spotify**

- **Play Track** — ``spotify:track:{trackId}``
- **Play Playlist** — ``spotify:playlist:{playlistId}``
- **Play Album** — ``spotify:album:{albumId}``

**Slack**

- **Open Channel** — ``slack://channel?team={teamId}&id={channelId}``
- **Open DM** — ``slack://user?team={teamId}&id={userId}``

**WhatsApp**

- **Send Message** — ``whatsapp://send?phone={phoneNumber}&text={message}``

Templates are also available for Notion, Discord, Teams, VS Code, Obsidian, Linear, Things, Bear, Raycast, 1Password, FaceTime, Messages, Mail, Apple Music, Fantastical, Safari, and Chrome.

Custom deep links
-----------------

You can create a deep link for any app that supports a URL scheme. Use the Deep Link action and enter your own template URL with ``{placeholders}``.

1. Add a **Deep Link** action to any app
2. Enter the template URL with placeholders in curly braces
3. Fill in the parameter values
4. ExtraBar saves the values so the link works on every click

Any app with a URL scheme works — check the app's documentation for supported URLs.

For more advanced examples like triggering Keyboard Maestro macros, BetterTouchTool actions, Raycast extensions, and Apple Shortcuts, see :doc:`examples`.

Not sure whether an app has a URL scheme? When configuring a deep link, use the **AI prompt** card — ExtraBar builds a research prompt for the app and opens it in the AI assistant of your choice (ChatGPT, Claude, Gemini, Grok, or Perplexity) to help you discover the app's deep link format.

Paste a link
------------

For Figma, Zoom, and Notion, you can paste a regular web URL instead of manually entering parameters. ExtraBar parses the URL and fills in the fields automatically.

For example, paste ``https://www.figma.com/design/ABC123/My-Design?node-id=1-2`` and ExtraBar extracts the file key and node ID for you.

Trigger ExtraBar actions from outside (``extrabar://``)
-------------------------------------------------------

ExtraBar has its own URL scheme, so other tools can trigger your configured actions. Every menu action and widget action can produce a **deep link of its own** — copy it from the action's context menu and use it anywhere that can open a URL: Raycast, Keyboard Maestro, Shortcuts, scripts, or another ExtraBar action.

Links use a friendly format based on your preset, item, and action names, and are secured with a per-install token — a copied link only works on the Mac it was created on.

