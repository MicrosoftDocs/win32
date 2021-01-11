---
description: Applications that use the TrueType text metrics can achieve a high degree of printer and document portability; they can use TrueType metrics even if they must maintain compatibility with early 16-bit versions of Windows.
ms.assetid: 29b54315-7c4e-4b8c-ad79-0b85c7386860
title: Using Portable TrueType Metrics
ms.topic: article
ms.date: 05/31/2018
---

# Using Portable TrueType Metrics

Applications that use the TrueType text metrics can achieve a high degree of printer and document portability; they can use TrueType metrics even if they must maintain compatibility with early 16-bit versions of Windows.

Design widths overcome most of the problems of device-dependent text introduced by physical devices. Design widths are a kind of logical width. Independent of any rasterization problems or scaling transformations, each glyph has a logical width and height. Composed to a logical page, each character in a string has a place that is independent of the physical device widths. Although a logical width implies that widths can be scaled linearly at all point sizes, this is not necessarily true for either nonportable or most TrueType fonts. At smaller point sizes, some glyphs are made wider relative to their height for better readability.

The characters in TrueType core fonts are designed against a 2048 by 2048 grid. The design width is the width of a character in these grid units. (TrueType supports any integer grid size up to 16,384 by 16,384; grid sizes that are integer powers of 2 scale faster than other grid sizes.)

The font outline is designed in notional units. The em square is the notional grid against which the font outline is fitted. (You can use the **otmEMSquare** member of [OUTLINETEXTMETRIC](/windows/desktop/api/Wingdi/ns-wingdi-outlinetextmetrica) and the **ntmSizeEM** member of [NEWTEXTMETRIC](/windows/win32/api/wingdi/ns-wingdi-newtextmetrica) to retrieve the size of the em square in notional units.) When a font is created that has a point size (in device units) equal to the size of its em square, the ABC widths for this font are the desired design widths. For example, assume the size of an em square is 1000 and the ABC widths of a character in the font are 150, 400, and 150. A character in this font that is 10 device units high would have ABC widths of 1.5, 4, and 1.5, respectively. Since the MM\_TEXT mapping mode is most commonly used with fonts (and MM\_TEXT is equivalent to device units), this is a simple calculation.

Because of the high resolution of TrueType design widths, applications that use them must take into account the large numeric values that can be created. For more information, see the following topics:

-   [Device vs. Design Units](device-vs--design-units.md)
-   [Metrics for Portable Documents](metrics-for-portable-documents.md)

 

 



