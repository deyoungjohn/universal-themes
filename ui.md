# Skill: Hackodds Dark Editorial Overhaul (UI.md)

This skill directs an agent to overhaul any existing website or interface into the dark editorial, translucent, space-atmospheric aesthetic exemplified by the **Hackodds** interface (`image.png`).

---

## 1. Visual Identity & Aesthetic Overview

The aesthetic is **Dark Editorial / Calculated Space Tech**. It marries high-contrast, elegant serif typography with a utilitarian dark-mode glassmorphism interface, set against a cinematic starry space backdrop with an animated wireframe globe and subtle earth horizon.

Key visual attributes:
- **Atmospheric Background:** Deep void-black universe with a field of stars, a subtle curved planet/horizon edge along the lower-right perimeter, and a faint dark ambient glow.
- **Wireframe Globe Feature:** An ethereal, animated rotating wireframe vector/SVG or canvas globe representing indexing/live telemetry.
- **Dual-Column Layout Dynamic:** A prominent left sticky/hero glass card alongside a right-side responsive 2-column grid of opportunity/metric cards.
- **Glassmorphic Translucency & Surface Depth:** High-radius rounded glass cards (`rounded-3xl` or `32px`) featuring ultra-dark frosted acrylic glass (`rgba(255, 255, 255, 0.03)` to `rgba(255, 255, 255, 0.05)`), subtle multi-layered drop shadows, and delicate low-opacity border strokes (`border border-white/10`).
- **Mixed Editorial Typography:** Bold modern sans-serif headings paired with italic serif emphasis (e.g. Newsreader / Playfair / Editorial New), contrasting with monospaced or tracking-wide utilitarian metadata chips.

---

## 2. Color Palette & Token System

All CSS variables and color applications must adhere to the following dark palette:

| Token Name | Hex / RGBA Value | Usage |
| :--- | :--- | :--- |
| `--bg-space-dark` | `#08090a` / `#050505` | Canvas base & deep space background |
| `--surface-card-hero` | `rgba(20, 20, 22, 0.72)` | Left hero card background |
| `--surface-card-item` | `rgba(28, 28, 30, 0.45)` | Grid cards / tile backgrounds |
| `--surface-card-hover`| `rgba(38, 38, 42, 0.65)` | Grid card hover state |
| `--border-subtle` | `rgba(255, 255, 255, 0.08)`| Outer container borders & grid dividers |
| `--border-highlight` | `rgba(255, 255, 255, 0.16)`| Active borders, pill outlines, button strokes |
| `--text-primary` | `#f4efe6` / `#ffffff` | Primary headings, prize figures, CTA text |
| `--text-secondary` | `#9ca3af` / `#a1a1aa` | Explanatory copy, breadcrumbs, days left |
| `--text-muted` | `#6b7280` / `#52525b` | Micro-labels, provider names, pagination |
| `--badge-bg` | `rgba(255, 255, 255, 0.06)`| Tag pills (`AL`, `TRADING`, `WEB3`, etc.) |
| `--cta-bg` | `#ffffff` | Primary inverted pill button (`Browse...`) |
| `--cta-text` | `#0f0e0c` | Primary CTA text |

---

## 3. Card Geometry, Roundness & Translucency Specifications

To replicate the card treatment:

### Hero / Left Anchor Card
- **Border Radius:** `border-radius: 32px` (`rounded-3xl` in Tailwind).
- **Background:** `background: radial-gradient(120% 120% at 50% 10%, rgba(30, 30, 34, 0.75) 0%, rgba(12, 12, 14, 0.88) 100%);`
- **Backdrop Filter:** `backdrop-filter: blur(28px) saturate(140%); -webkit-backdrop-filter: blur(28px);`
- **Border:** `1px solid rgba(255, 255, 255, 0.09)`.
- **Box Shadow:** `0 24px 64px -12px rgba(0, 0, 0, 0.7), inset 0 1px 1px 0 rgba(255, 255, 255, 0.15)`.

### Grid Opportunity Cards
- **Border Radius:** `border-radius: 24px` (`rounded-2xl`).
- **Background:** `linear-gradient(180deg, rgba(255, 255, 255, 0.045) 0%, rgba(255, 255, 255, 0.02) 100%)`.
- **Backdrop Filter:** `backdrop-filter: blur(16px); -webkit-backdrop-filter: blur(16px);`
- **Border:** `1px solid rgba(255, 255, 255, 0.07)`.
- **Transition:** `all 0.25s cubic-bezier(0.16, 1, 0.3, 1)`.
- **Hover State:** Border transitions to `rgba(255, 255, 255, 0.18)`, background deepens to `rgba(255, 255, 255, 0.075)`, slight upward translate (`transform: translateY(-2px)`).

---

## 4. Background Horizon & Rotating Globe Implementation

### A. The Planet / Earth Horizon Edge
Apply as a background pseudo-element or SVG layer fixed to the bottom-right corner:
```css
.space-horizon {
  position: fixed;
  right: -10vw;
  bottom: -20vh;
  width: 90vw;
  height: 90vh;
  border-radius: 50%;
  background: radial-gradient(circle at 45% 45%, rgba(18, 26, 32, 0.4) 0%, rgba(5, 7, 10, 0.95) 75%, #050608 100%);
  box-shadow: 
    0 -12px 60px 4px rgba(255, 255, 255, 0.08),
    0 -40px 140px 10px rgba(130, 160, 200, 0.12);
  pointer-events: none;
  z-index: 0;
}
```

### B. The 3D Rotating Wireframe Globe (Badge Graphic)
Positioned centrally in the hero card with live statistics inside:
```html
<div class="relative w-36 h-36 flex items-center justify-center mx-auto my-6">
  <!-- Glowing dashed boundary ring -->
  <div class="absolute inset-0 rounded-full border border-dashed border-white/20 animate-spin-slow"></div>
  
  <!-- Rotating wireframe meridian & equator lines -->
  <svg class="absolute inset-2 w-32 h-32 text-white/30" viewBox="0 0 100 100" fill="none" stroke="currentColor" stroke-width="0.8">
    <circle cx="50" cy="50" r="46" stroke="rgba(255,255,255,0.3)"/>
    <!-- Animated Equator and Longitude Ellipses -->
    <ellipse cx="50" cy="50" rx="46" ry="18" stroke-dasharray="3 2" class="animate-spin-reverse-slower origin-center"/>
    <ellipse cx="50" cy="50" rx="20" ry="46" class="animate-pulse"/>
    <ellipse cx="50" cy="50" rx="35" ry="46" stroke="rgba(255,255,255,0.15)"/>
    <line x1="50" y1="4" x2="50" y2="96" stroke="rgba(255,255,255,0.2)"/>
    <line x1="4" y1="50" x2="96" y2="50" stroke="rgba(255,255,255,0.2)"/>
  </svg>
  
  <!-- Centered Counter -->
  <div class="relative z-10 text-center">
    <span class="block font-mono text-2xl font-bold tracking-tight text-white">134</span>
    <span class="block text-[9px] uppercase tracking-widest text-zinc-400 font-mono">INDEXED</span>
  </div>
</div>
```

---

## 5. Typography Hierarchy

1. **Brand Logo:** Sans-serif bold geometric typography preceded by a dual-pillar geometric emblem (`H`).
2. **Hero Main Title:**
   - Font: Inter / Geist / DM Sans combined with **Newsreader** (italicized serif).
   - Markup style: `Every live hackathon, <span class="font-serif italic font-normal text-white underline decoration-white/30 underline-offset-8">ranked by your odds.</span>`
   - Size: `text-5xl lg:text-6xl font-medium tracking-tight text-white leading-[1.1]`.
3. **Hero Subtitle:**
   - Clean, muted sans-serif text (`text-zinc-400 text-sm font-normal max-w-sm mx-auto leading-relaxed`).
4. **Header Eyebrow Pills & Status Indicators:**
   - Pill pill-shaped status bar (`px-4 py-1.5 rounded-full bg-white/5 border border-white/10 text-xs font-mono`).
   - Indicator dot: `inline-block w-1.5 h-1.5 rounded-full bg-emerald-400 mr-2 shadow-[0_0_8px_rgba(52,211,153,0.8)]`.
5. **Card Content:**
   - Organization/Platform: Uppercase micro-label (`text-[10px] tracking-widest font-mono text-zinc-400`).
   - Urgency Tag: Top right (`text-[11px] font-mono text-zinc-400`).
   - Title: `text-base font-semibold text-white truncate`.
   - Category Badges: `px-2.5 py-0.5 rounded-md bg-white/5 text-[11px] font-mono tracking-wide text-zinc-300 border border-white/5`.
   - Prize/Key Metric: High-emphasis financial display (`text-2xl font-bold font-sans text-white tracking-tight`).

---

## 6. Layout Architecture (Dual-Column Desktop View)

```text
+-------------------------------------------------------------------------------------------------------+
|  TOP BAR:  [Status Capsule: 6 verified feeds · refreshed ...]  [Sync] [Theme]  [(GitHub) Connect]     |
+--------------------------------------------------------------------+----------------------------------+
|  LEFT STICKY HERO CARD (approx 42% width)                          |  RIGHT OPPORTUNITIES SECTION     |
|  +--------------------------------------------------------------+  |  Header: LIVE OPPORTUNITIES      |
|  | Header: [Logo: hackodds]                  [Support] [= Menu] |  |          Page 1 of 7 · 134 index |
|  |                                                              |  |                                  |
|  |                [ Rotating Wireframe Globe ]                  |  |  2-Column Opportunity Grid:      |
|  |                      134 / INDEXED                           |  |  +---------------+ +-----------+ |
|  |                                                              |  |  | Card 1        | | Card 2    | |
|  |       "Every live hackathon, ranked by your odds."           |  |  +---------------+ +-----------+ |
|  |                                                              |  |  | Card 3        | | Card 4    | |
|  |  "Every hackathon we index, ranked by what its prize is..."  |  |  +---------------+ +-----------+ |
|  |                                                              |  |  | Card 5        | | Card 6    | |
|  |           [ (->) Browse 134 hackathons ]                     |  |  +---------------+ +-----------+ |
|  +--------------------------------------------------------------+  |  Pagination: < Prev  (....) Next|
+--------------------------------------------------------------------+----------------------------------+
```

---

## 7. Execution Checklist for Overhaul Tasks

1. **Set Up Background:** Apply the star-field canvas/CSS pattern and the curved planet atmospheric glow on `body`.
2. **Apply Typography:** Inject serif font `Newsreader` (or `Playfair Display`) alongside a modern mono and sans font.
3. **Restructure Main Grid:** Build a 12-column grid (`grid grid-cols-12 gap-6 min-h-screen p-6 lg:p-8`). Give the hero card `col-span-5` and the listing panel `col-span-7`.
4. **Implement Glassmorphism:** Ensure all cards utilize `backdrop-blur`, subtle borders (`border-white/10`), and deep semi-transparent dark backgrounds.
5. **Incorporate Wireframe Globe:** Embed the SVG/CSS rotating globe with the metric counter in the hero section.
6. **Style Buttons & CTAs:**
   - Primary Hero CTA: White pill button with dark text, rounded full (`rounded-full py-3.5 px-7 font-medium`), with a subtle arrow icon inside a circular container.
   - GitHub / Header Buttons: Rounded pill buttons (`rounded-full bg-white text-zinc-900 font-medium px-4 py-2`).
7. **Ensure Pagination & Micro-Interactions:** Add dot indicators (`rounded-full w-1.5 h-1.5 bg-white/20 active:bg-white`) and arrow navigation at the bottom right.
