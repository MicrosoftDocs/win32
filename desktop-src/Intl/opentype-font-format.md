---
description: The Unicode-based OpenType font format extends the TrueType font file format.
ms.assetid: 0d67481a-79ff-448c-b77c-a55bf935a22a
title: OpenType Font Format
ms.topic: article
ms.date: 05/31/2018
---

# OpenType Font Format

The Unicode-based OpenType font format extends the TrueType font file format. OpenType fonts allow mapping between characters and [glyphs](uniscribe-glossary.md), enabling support for ligatures, positional forms, alternates, and other substitutions. OpenType fonts can also include information that supports two-dimensional glyph positioning and glyph attachment, and can contain either TrueType or PostScript outlines.

Layout features within OpenType fonts are organized by scripts and languages, allowing a single font to support multiple writing systems, even within the same script. To ensure consistency in text layout operations and to avoid unnecessary overhead in font files or applications, many of the text layout and language semantic algorithms are included in Uniscribe. This relieves the font developer from having to define generalized script rules within a font.

Applications can introduce specific knowledge or preferences regarding script layout. OpenType layout fonts might even contain layout rules that duplicate or supersede those applied by operating system services. The layered structure of operating system services supporting text layout allows an application to choose the layout information to use, and select how to apply it. For additional information, see the [Microsoft Typography Specifications overview](https://www.microsoft.com/typography/SpecificationsOverview.mspx) or the [OpenType Specification](https://www.microsoft.com/typography/otspec/).

## Related topics

<dl> <dt>

[About Uniscribe](about-uniscribe.md)
</dt> </dl>

 

 



