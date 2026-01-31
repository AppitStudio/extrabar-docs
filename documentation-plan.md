# ExtraBar Documentation Plan

## Research Summary

This plan is based on research from the following sources:
- [ExtraBar Official Website](https://extrabar.app/)
- [Hacker News Discussion](https://news.ycombinator.com/item?id=46659943)
- [Mac Power Users Forum](https://talk.macpowerusers.com/t/1-for-extrabar/43938)
- [AppAddict Review](https://appaddict.app/post/extrabar-is-the-app-of-my-dreams)
- [FunBlocks Review](https://www.funblocks.net/aitools/reviews/extrabar)
- [MacMenuBar.com](https://macmenubar.com/extrabar/)
- [On My Menubar](https://onmymenubar.app/extrabar/)
- [Firsto](https://firsto.co/projects/extrabar)
- [YouTube Demo](https://youtu.be/TCZoetKXfJY)

---

## Proposed Documentation Structure

### 1. Introduction (`introduction.rst`)

**Purpose:** Explain what ExtraBar is and why users need it.

**Content:**
- **What is ExtraBar?**
  - A customizable macOS menu bar app for quick access to apps, deep links, and custom actions
  - Transforms your menu bar from passive icon storage into an active workflow launcher
  - Created by AppitStudio (also behind ExtraDock and DockFlow)

- **The Problem ExtraBar Solves**
  - Menu fatigue and navigational inefficiency
  - Opening apps → navigating menus → finding what you need takes too long
  - Frequent context switching between multiple apps slows productivity

- **Who is ExtraBar For?**
  - Designers working with Figma, Photoshop
  - Developers using IDEs, Terminal, VS Code
  - Managers juggling Zoom meetings, Slack channels
  - Power users who want keyboard-driven workflows
  - Anyone managing complex multi-app workflows

- **How ExtraBar is Different from Bartender/Ice**
  - Bartender and Ice help *hide* icons
  - ExtraBar helps you *do* things faster
  - Focus on actions, not icon management
  - Quote: "Bartender removes stuff from the menu bar; ExtraBar adds to the menu bar"

- **Key Highlights**
  - Zero permissions required (accessibility optional)
  - Works entirely offline
  - No analytics, no telemetry, no data collection
  - Configuration stays on your Mac
  - Export/import to sync across Macs

---

### 2. Installation (`installation.rst`)

**Purpose:** Get users set up quickly.

**Content:**
- **System Requirements**
  - macOS 12.4 (Monterey) or later
  - Supports macOS 13 Ventura, macOS 14 Sonoma, macOS 15 Sequoia, macOS 26 Tahoe
  - Works on both Intel and Apple Silicon Macs

- **Download**
  - Download from [extrabar.app](https://extrabar.app)
  - File is a standard `.dmg` disk image

- **Installation Steps**
  1. Open the downloaded `.dmg` file
  2. Drag ExtraBar to your Applications folder
  3. Open ExtraBar from Applications
  4. Enter your license key when prompted (requires internet for activation only)

- **License Activation**
  - One-time internet connection required for activation
  - After activation, ExtraBar works completely offline
  - License is tied to your purchase email

- **Optional: Enable Accessibility**
  - Not required for basic functionality
  - Enables enhanced keyboard navigation
  - System Settings → Privacy & Security → Accessibility → Add ExtraBar

- **Uninstallation**
  - Drag ExtraBar from Applications to Trash
  - Configuration stored in Application Support folder (optional cleanup)

---

### 3. Quick Start (`quickstart.rst`)

**Purpose:** Get users productive in 5 minutes.

**Content:**
- **Your First Action (Step-by-Step)**
  1. Open ExtraBar
  2. Click the ExtraBar icon in your menu bar
  3. Click "Add Action" or the + button
  4. Choose an app from the preset list (e.g., Slack, Zoom, Figma)
  5. Configure the action (name, icon, URL/deep link)
  6. Save and test by clicking your new action

- **Understanding the Interface**
  - Menu bar icon location
  - Action list view
  - Settings/preferences access
  - Right-click menu options

- **Try These First Actions**
  - Open a specific website
  - Launch an app
  - Open a Slack channel (if you use Slack)
  - Open a Figma file (if you use Figma)

- **Set Your Global Hotkey**
  - Go to Settings → Keyboard
  - Assign a global hotkey (e.g., `⌥ + Space`)
  - Now you can open ExtraBar instantly from anywhere

- **Navigate with Keyboard**
  - Use number keys (1-9) to select actions quickly
  - Use arrow keys to navigate menus
  - Press Enter to execute an action

---

### 4. Core Features (`features.rst`)

**Purpose:** Deep dive into what ExtraBar can do.

**Content:**

#### 4.1 Deep Links
- **What are Deep Links?**
  - URLs that open specific content inside an app
  - Skip navigation and go directly where you need
  - Example: Open a specific Slack channel, not just Slack

- **Deep Link Examples by App**
  - **Zoom:** Join specific meetings directly
  - **Slack:** Open specific channels or DMs
  - **Figma:** Open specific files, frames, prototypes, assets, folders
  - **Spotify:** Open playlists, albums, artists
  - **VS Code:** Open specific projects
  - **Things 3:** Open specific lists or projects
  - **Obsidian:** Open specific vaults or notes
  - **Raycast:** Trigger specific extensions

- **Finding Deep Links**
  - Some apps expose them easily (Slack, Zoom)
  - Others require research (check app documentation)
  - Community resources for deep link URLs

#### 4.2 Display Modes
- **Inline Mode (Default)**
  - Actions appear in your native macOS menu bar
  - Blends with existing menu bar icons
  - Best for: Users with menu bar space available

- **Floating Bar Mode**
  - Separate customizable window
  - Appears on demand with keyboard shortcut
  - Auto-hide when not in use
  - Best for: Users with crowded menu bars or laptop screens

- **Switching Between Modes**
  - How to toggle in settings
  - Customizing floating bar appearance

#### 4.3 Keyboard Shortcuts
- **Global Hotkey**
  - One hotkey to summon ExtraBar from anywhere
  - Recommended: `⌥ + Space` or `⌃ + Space`

- **Navigation**
  - Number keys (1-9) for quick action selection
  - Arrow keys for menu navigation
  - Enter to execute
  - Escape to close

- **Per-Action Shortcuts**
  - Assign custom shortcuts to specific actions
  - Execute actions without opening ExtraBar menu

#### 4.4 Action Types (16 Types Available)
- Open App
- Open File/Folder
- Open URL/Deep Link
- Run Shell Script
- Trigger macOS Shortcut
- Execute Terminal Command
- Open System Preferences pane
- And more...

#### 4.5 App Presets
- **36+ Built-in Presets**
  - Design: Figma, Photoshop, Sketch
  - Development: VS Code, Terminal, Cursor
  - Communication: Slack, Zoom, WhatsApp, Messages
  - Productivity: Things 3, Obsidian, Raycast, Notion
  - Utilities: Speedtest, Color Picker, Emoji Picker, Timer

- **Using Presets**
  - Select app from list
  - Preset provides common actions
  - Customize or add more as needed

#### 4.6 Right-Click Actions
- Every item has a customizable right-click menu
- Add secondary actions to any item
- Quick access to related functions

#### 4.7 Export & Import
- Export your entire configuration to a file
- Import on another Mac
- Sync setups across multiple machines
- Backup your configuration

---

### 5. Additional Sections to Consider

#### 5.1 Use Cases / Examples (`examples.rst`)
Real-world workflows from actual users:

- **Developer Workflow**
  - Quick access to VS Code projects
  - Terminal sessions
  - GitHub repos
  - Documentation sites

- **Designer Workflow**
  - Figma files and frames
  - Photoshop actions
  - Asset folders
  - Client project folders

- **Manager Workflow**
  - Zoom meeting quick-join
  - Slack channel shortcuts
  - Calendar deep links
  - Report dashboards

- **Power User Workflow**
  - Keyboard Maestro macro triggers
  - Raycast extension organization
  - Apple Shortcuts launcher
  - Multi-app batch operations

#### 5.2 FAQ (`faq.rst`)
Common questions from Hacker News and forums:

- **Why no free trial?**
  - 14-day money-back guarantee instead
  - Developer rationale: paid users test more thoroughly

- **How is this different from Alfred/Raycast?**
  - ExtraBar works *alongside* these tools
  - Persistent menu bar access vs. command palette
  - Deep link focus

- **Do I need to give it permissions?**
  - No permissions required for basic use
  - Accessibility is optional for enhanced keyboard features

- **Does it work offline?**
  - Yes, completely offline after activation
  - No analytics, no telemetry

- **Can I transfer my license?**
  - One license per user
  - Contact support for device transfers

#### 5.3 Troubleshooting (`troubleshooting.rst`)
- Action not working
- Deep link not opening correctly
- Keyboard shortcuts not responding
- Menu bar icon not appearing
- Export/import issues

---

## Content Guidelines

### Tone & Style
- Clear, concise, and practical
- Focus on getting users productive quickly
- Use screenshots and visual examples
- Include code blocks for deep link URLs and scripts

### What to Include
- Step-by-step instructions with numbered lists
- Screenshots of the interface
- Real examples with actual deep link URLs
- Tips and best practices

### What to Avoid
- Marketing language (keep it factual)
- Overly technical jargon
- Assumptions about user expertise
- Made-up features or capabilities

---

## File Structure

```
docs/
├── index.rst                    # Landing page
├── introduction.rst             # What is ExtraBar
├── installation.rst             # Download & setup
├── quickstart.rst               # 5-minute getting started
├── features/
│   ├── index.rst               # Features overview
│   ├── deep-links.rst          # Deep links explained
│   ├── display-modes.rst       # Inline vs floating
│   ├── keyboard-shortcuts.rst  # Keyboard navigation
│   ├── action-types.rst        # 16 action types
│   ├── app-presets.rst         # Built-in presets
│   └── export-import.rst       # Sync configurations
├── examples/
│   ├── index.rst               # Use cases overview
│   ├── developer.rst           # Developer workflow
│   ├── designer.rst            # Designer workflow
│   └── power-user.rst          # Power user workflow
├── faq.rst                      # Frequently asked questions
└── troubleshooting.rst          # Common issues & fixes
```

---

## Priority Order

For the basic structure you requested, implement in this order:

1. **Introduction** - Essential context
2. **Installation** - Get users started
3. **Quick Start** - Immediate value
4. **Core Features** - Main functionality

Optional additions (if time permits):
5. Examples/Use Cases
6. FAQ
7. Troubleshooting

---

## Open Questions for Review

1. Should we include pricing information in the docs, or keep it on the website only?
2. Do you want screenshots embedded, or should I note where they should go?
3. Should deep link examples be generic or include actual working URLs?
4. Is there official documentation or a knowledge base we should reference/link to?
5. Should we include a changelog or version history section?

---

## Next Steps

Upon approval of this plan:
1. Update `index.rst` with new structure
2. Create `introduction.rst` with full content
3. Create `installation.rst` with full content
4. Create `quickstart.rst` with full content
5. Create `features.rst` or `features/` directory with full content
6. Remove placeholder content from existing files
