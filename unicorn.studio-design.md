---
version: alpha
name: Unicorn Studio Dark
description: A cinematic dark interface with neon violet accents, restrained chrome UI, and editorial typography.
colors:
  primary: "#8E6CE4"
  primary-strong: "#AB8FF1"
  primary-soft: "#62626F"
  secondary: "#25252D"
  tertiary: "#31313A"
  neutral: "#08080A"
  surface: "#25252D"
  on-surface: "#DAD7DE"
  text: "#AEAAC0"
  muted: "#62626F"
  border: "#31313A"
  highlight: "#DAD7DE"
  error: "#E46C8E"
typography:
  headline-display:
    fontFamily: "Overused Grotesk"
    fontSize: 64px
    fontWeight: 500
    lineHeight: 64px
    letterSpacing: "-2.56px"
  headline-lg:
    fontFamily: "Overused Grotesk"
    fontSize: 48px
    fontWeight: 500
    lineHeight: 48px
    letterSpacing: "-1.92px"
  headline-md:
    fontFamily: "Overused Grotesk"
    fontSize: 32px
    fontWeight: 500
    lineHeight: 32px
    letterSpacing: "-0.96px"
  headline-sm:
    fontFamily: "Overused Grotesk"
    fontSize: 26px
    fontWeight: 500
    lineHeight: 26px
    letterSpacing: "-0.78px"
  body-lg:
    fontFamily: "-apple-system"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 25px
  body-md:
    fontFamily: "-apple-system"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 24px
  body-sm:
    fontFamily: "-apple-system"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 20px
  label-lg:
    fontFamily: "-apple-system"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 20px
  label-md:
    fontFamily: "-apple-system"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 18px
  label-sm:
    fontFamily: "-apple-system"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 16px
    letterSpacing: "0.02em"
  caption:
    fontFamily: "-apple-system"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 16px
  nav:
    fontFamily: "-apple-system"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 20px
rounded:
  none: 0px
  sm: 3px
  md: 5px
  lg: 8px
  xl: 12px
  full: 9999px
spacing:
  xs: 8px
  sm: 16px
  md: 26px
  lg: 40px
  xl: 116px
  gutter: 24px
  margin: 32px
components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-surface}"
    typography: "{typography.label-lg}"
    rounded: "{rounded.sm}"
    padding: "10px 20px"
    height: "40px"
  button-primary-hover:
    backgroundColor: "{colors.primary-strong}"
    textColor: "{colors.on-surface}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.on-surface}"
    typography: "{typography.label-lg}"
    rounded: "{rounded.sm}"
    padding: "10px 20px"
    height: "40px"
  button-link:
    backgroundColor: "transparent"
    textColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: "0px"
  card:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.muted}"
    rounded: "{rounded.md}"
    padding: "12px"
  input:
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.on-surface}"
    rounded: "{rounded.sm}"
    padding: "10px 12px"
    height: "40px"
  chip:
    backgroundColor: "transparent"
    textColor: "{colors.text}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
  navbar:
    backgroundColor: "{colors.neutral}"
    textColor: "{colors.text}"
    height: "68px"
  hero-panel:
    backgroundColor: "{colors.neutral}"
    textColor: "{colors.on-surface}"
    rounded: "{rounded.lg}"
---

# Unicorn Studio Dark

## Overview
This system feels cinematic, futuristic, and product-led: a dark canvas punctuated by violet light and crisp chrome controls. It targets creative technologists and design-forward builders who want an interface that feels premium without becoming ornate. The emotional tone is restrained and confident, with spacious composition and a strong focus on the hero message.

## Colors
- **Primary (#8E6CE4):** The signature neon-violet accent used for primary actions, glowing highlights, and the most important interactive moments.
- **Primary strong (#AB8FF1):** A brighter lavender edge tone for borders, hover states, and subtle emphasis around active controls.
- **Secondary (#25252D):** The dominant surface tone for cards, buttons, and UI chrome; it reads as deep graphite rather than pure black.
- **Tertiary (#31313A):** A slightly lighter structural tone for borders, separators, and inset detail.
- **Neutral (#08080A):** The near-black background that gives the entire layout its immersive stage-like quality.
- **On-surface (#DAD7DE):** The bright readable text color for buttons, key labels, and high-priority content.
- **Text (#AEAAC0):** The main body and UI text color; cool, subdued, and intentionally low-contrast for a refined dark-mode feel.
- **Muted (#62626F):** Used for secondary navigation, helper text, and low-emphasis links.
- **Border (#31313A):** Thin structural lines that keep components defined without adding visual noise.
- **Highlight (#DAD7DE):** The brightest neutral accent for contrast, small UI details, and strong legibility.
- **Error (#E46C8E):** A reserved pink-red tone for destructive states and validation feedback.

## Typography
Headings use Overused Grotesk, giving the interface a modern editorial voice with soft geometry and tight tracking. The display scale is intentionally compressed: 64px, 48px, 32px, and 26px all use strong negative letter-spacing to create a premium, polished headline rhythm. Body text relies on the system stack through -apple-system, keeping the interface fast, familiar, and highly legible at 16px to 18px. Labels and navigation are slightly heavier than body text, while small utility text stays quiet and understated. Uppercase styling is not a dominant pattern; emphasis comes from weight, spacing, and contrast rather than caps-lock treatment.

## Layout & Spacing
The layout is center-weighted and hero-first, with a large vertical stage and generous empty space around the focal content. Spacing follows a small set of clear increments: 8px, 16px, 26px, 40px, and 116px, which creates a rhythm that feels controlled and cinematic rather than dense. Cards and controls use compact internal padding, while sections use much larger breathing room to preserve the high-end presentation. The composition behaves like a fixed-max-width landing page with an immersive full-width visual panel inside a dark frame.

## Elevation & Depth
Depth is created mostly through tonal contrast, inset highlights, and layered imagery instead of heavy shadow stacks. The UI is largely flat, with only subtle shadows on primary buttons and an inner top highlight on secondary surfaces. Borders in #31313A define structure more than elevation, which keeps the interface crisp and minimal. The luminous violet hero artwork supplies the strongest sense of depth and motion.

## Shapes
The shape language is modest and technical: small radii dominate, with 3px corners for buttons and 5px for cards. This creates a precise, engineered feel rather than a soft consumer-app look. Larger visual panels can stretch to 8px and 12px when a more cinematic container is needed, but interactive elements stay tight and controlled.

## Components
Primary buttons should use `button-primary` with a violet fill, light text, a 1px border, and compact padding for a dense but premium feel. Keep primary actions visually prominent with the slightly brighter `button-primary-hover` tone on interaction. Secondary buttons should follow `button-secondary`: dark graphite fill, minimal ornament, and subtle inset depth to avoid competing with the primary CTA. Link-style actions should remain understated using `button-link`, with muted text and no filled background.

Cards should follow `card` with a dark surface, 1px border, small radius, and modest padding. Inputs should mirror card surfaces closely, using the same dark tonal family so form fields feel embedded in the interface rather than floating above it. Chips and tags should stay minimal and transparent, using rounded full pills and restrained text color. Navigation items should use quiet body-size typography and muted tones, reserving stronger color only for active or primary actions. Hero panels can use `hero-panel` with the darkest neutral background and rounded corners to frame high-impact visuals.

## Do's and Don'ts
- Do keep the UI dark, quiet, and spacious so the violet accent can carry hierarchy.
- Do use Overused Grotesk for headlines and reserve the system stack for body and UI chrome.
- Do prefer small radii and thin borders over large shadows or glossy effects.
- Do make primary actions violet and secondary actions graphite to preserve contrast in the hero.
- Don't introduce bright, saturated palette colors beyond the established violet accent.
- Don't use heavy drop shadows or soft glassmorphism that would weaken the crisp, technical look.
- Don't over-round buttons or cards; the system should feel precise, not bubbly.
- Don't let body text compete with headlines; keep secondary copy muted and compact.