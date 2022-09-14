---
description: Raster, Vector, TrueType, and OpenType Fonts
ms.assetid: 4fe98f04-3fb0-4a03-86c3-d0ea6f07f8f0
title: Raster, Vector, TrueType, and OpenType Fonts
ms.topic: article
ms.date: 05/31/2018
---

# Raster, Vector, TrueType, and OpenType Fonts

Applications can use four different kinds of font technologies to display and print text:

-   Raster
-   Vector
-   TrueType
-   Microsoft OpenType

The differences between these fonts reflect the way that the *glyph* for each character or symbol is stored in the respective font-resource file:

-   In raster fonts, a glyph is a bitmap that the system uses to draw a single character or symbol in the font.
-   In vector fonts, a glyph is a collection of line endpoints that define the line segments that the system uses to draw a character or symbol in the font.
-   In TrueType and OpenType fonts, a glyph is a collection of line and curve commands as well as a collection of hints.

The system uses the line and curve commands to define the outline of the bitmap for a character or symbol in the TrueType or Microsoft OpenType font. The system uses the hints to adjust the length of the lines and shapes of the curves used to draw the character or symbol. These hints and the respective adjustments are based on the amount of scaling used to reduce or increase the size of the bitmap. An OpenType font is equivalent to a TrueType font except that an OpenType font allows PostScript glyph definitions in addition to TrueType glyph definitions.

Because the bitmaps for each glyph in a raster font are designed for a specific resolution of device, raster fonts are generally considered to be device dependent. Vector fonts, on the other hand, are not device dependent, because each glyph is stored as a collection of scalable lines. However, vector fonts are generally drawn more slowly than raster or TrueType and OpenType fonts. TrueType and OpenType fonts provide both relatively fast drawing speed and true device independence. By using the hints associated with a glyph, a developer can scale the characters from a TrueType or OpenType font up or down and still maintain their original shape.

As previously mentioned, the glyphs for a font are stored in a font-resource file. A font-resource file is actually a DLL that contains only data, there is no code. For raster and vector fonts, this data is divided into two parts: a header describing the font's metrics and the glyph data. A font-resource file for a raster or vector font is identified by the .fon file name extension. For TrueType and OpenType fonts, there are two files for each font: the first file contains a relatively short header and the second contains the actual font data. The first file is identified by an .fot extension and the second is identified by a .ttf extension.

 

 



