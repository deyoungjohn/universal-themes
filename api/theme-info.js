export default async function handler(req, res) {
  // Set CORS headers
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');

  if (req.method === 'OPTIONS') {
    return res.status(200).end();
  }

  const { url, slug: slugParam } = req.query;
  const target = (url || slugParam || '').trim();

  if (!target) {
    return res.status(400).json({ success: false, error: "Missing 'url' or 'slug' parameter" });
  }

  // Extract slug
  let slug = target;
  const match = target.match(/addtheme[/:=]([a-zA-Z0-9_-]+)/);
  if (match) {
    slug = match[1];
  } else {
    slug = slug.replace(/[^a-zA-Z0-9_-]/g, '');
  }

  if (!slug) {
    return res.status(400).json({ success: false, error: 'Invalid theme slug or link' });
  }

  const tmeUrl = `https://t.me/addtheme/${slug}`;

  try {
    const response = await fetch(tmeUrl, {
      headers: {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
      },
    });

    if (!response.ok) {
      return res.status(response.status).json({
        success: false,
        error: `Telegram returned HTTP status ${response.status}`,
      });
    }

    const html = await response.text();

    // Extract title
    const titleMatch = html.match(/<meta property="og:title" content="([^"]+)"/);
    let title = titleMatch ? titleMatch[1].replace(/^Telegram Theme:\s*/i, '').trim() : `Theme ${slug}`;

    // Extract colors
    const colorsMatch = html.match(/data-colors="([0-9a-fA-F,]+)"/);
    const colors = colorsMatch ? colorsMatch[1].split(',') : [];

    // Detect dark theme from colors luminance
    function calcLum(c) {
      c = c.replace(/^#/, '');
      if (c.length === 8) c = c.substring(2);
      if (c.length === 6) {
        const r = parseInt(c.substring(0, 2), 16);
        const g = parseInt(c.substring(2, 4), 16);
        const b = parseInt(c.substring(4, 6), 16);
        return (0.299 * r + 0.587 * g + 0.114 * b) / 255.0;
      }
      return 0.5;
    }

    let isDark = false;
    if (colors && colors.length > 0) {
      const avgLum = colors.reduce((sum, c) => sum + calcLum(c), 0) / colors.length;
      isDark = (avgLum * 0.6) < 0.45 || title.toLowerCase().includes('dark') || title.toLowerCase().includes('night');
    } else {
      isDark = title.toLowerCase().includes('dark') || title.toLowerCase().includes('night');
    }

    // Extract description
    const descMatch = html.match(/class="tgme_page_description">([^<]*<strong>.*?<\/strong>[^<]*)/);
    const description = descMatch ? descMatch[1].replace(/<[^>]+>/g, '').trim() : '';

    return res.status(200).json({
      success: true,
      type: 'telegram_slug',
      slug,
      title,
      colors,
      isDark,
      description,
      url: tmeUrl,
    });
  } catch (error) {
    return res.status(500).json({
      success: false,
      error: `Failed to fetch theme from Telegram: ${error.message}`,
    });
  }
}
