# MEETS — Visual Theory Archive

A curated collection of visual essays exploring intersections of philosophy, technology, and culture. Built for browsing, curating, and presenting.

## Quick Start

```bash
cd MEETS
python3 -m http.server 8080
```

Open [http://localhost:8080](http://localhost:8080)

## Tools

| Tool | File | Description |
|------|------|-------------|
| **Gallery** | `slideshow.html` | Main viewer with zoom navigation, timeline editing, presentation mode |
| **Match Viewer** | `v5.html` | Side-by-side comparison for conceptual matchups |
| **Archive Core** | `slideshow-03.html` | Classic archive with search and multi-view |
| **Dark Matter Ring** | `v2.html` | Philosophical wrestling interface |

## Features

### Gallery (slideshow.html)
- **Zoom Navigation**: All Folders → Folder → Image → Present
- **Timeline Editing**: Build custom sequences by tapping images
- **Presentation Mode**: Auto-play, swipe gestures, keyboard controls
- **Import/Export**: Save and load playlists
- **Mobile-First**: Works on phone, tablet, and desktop

### Usage
1. **Browse**: Click folder titles to zoom in
2. **Curate**: Tap images to add to timeline
3. **Present**: Click "▶ Timeline" or play individual folders
4. **Export**: Save your sequence for later

## Collections

25 visual essays covering:

- AI Grief: Five Western Reactions
- Augustine to Language-Games
- Benjamin's Theses on History
- Common Sense as a Cultural System
- Conversational Viscosity
- Cool Radio, Warm Myths
- Culture Re-Engineers Man
- Cybernetics & Ghosts
- Darwin Among the Machines
- Dolphin Talk: Code of Relationship
- Grace, Style & Info in Art
- Heidegger: Questioning Tech's Essence
- Language as Concept Translation
- Molasses Talk: Thick Ekphrasis
- Noise: Between Chaos & Death
- Operative Ekphrasis in AI
- Play, Rules & Serious Muddles
- Satyrs' Meals: Host, Guest, Parasite
- Thick Prompt Alchemy
- Thick Prompts as Cybernetic Molasses
- Turing's Test: Can Machines Think?
- What the Frog's Eye Tells the Brain
- Wittgenstein's Model-Milieu 1914
- Words Assemble Worlds
- Wrestling as Mythic Spectacle

## File Structure

```
MEETS/
├── index.html          # Landing page
├── slideshow.html      # Main gallery app
├── manifest.json       # Collection metadata
├── index.md            # Markdown index
├── slideshow-03.html   # Archive viewer
├── v1-v5.html          # Experimental viewers
├── organize_images.py  # Build script
└── [25 folders]/       # Image collections
```

## Keyboard Shortcuts

| Key | Action |
|-----|--------|
| `←` `→` | Previous/Next slide |
| `Space` | Toggle auto-play |
| `Escape` | Close/Back |

## Data

- `manifest.json` — Machine-readable collection index
- `index.md` — Human-readable collection index
- Playlist format: `number|folder-id|filename`

## Development

### Regenerate manifest
```bash
python3 organize_images.py
```

### Serve locally
```bash
python3 -m http.server 8080
```

## License

Visual essays and images are for educational/research purposes.

---

*MEETS — Memory, Embodiment, Emergence, Translation, Synthesis*
