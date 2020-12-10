---
title: Fonts and Text (OpenGL)
description: Microsoft's implementation of OpenGL in Windows supports GDI graphics in a single-buffered OpenGL window.
ms.assetid: 25a45e1a-6c1e-416b-8993-daeefc1100f3
keywords:
- OpenGL on Windows,fonts
- OpenGL on Windows,text
ms.topic: article
ms.date: 05/31/2018
---

# Fonts and Text (OpenGL)

Microsoft's implementation of OpenGL in Windows supports GDI graphics in a single-buffered OpenGL window. It does not support GDI graphics in a double-buffered OpenGL window. Thus, you can call only the standard GDI font and text functions to draw text in a single-buffered OpenGL window; you cannot call those functions to draw text in a double-buffered OpenGL window.

There is a workaround for this restriction on text in double-buffered windows: build OpenGL display lists for bitmap images of characters, and then execute those display lists to draw characters. There are three main steps in this process:

1.  Select a font for a device context, setting the font's properties as desired.
2.  Create a set of bitmap display lists based on the glyphs in the device context's font, one display list for each glyph that the application will draw.
3.  Draw each glyph in a string, using those bitmap display lists.

To create the display lists, call the [**wglUseFontBitmaps**](/windows/desktop/api/wingdi/nf-wingdi-wglusefontbitmapsa) and [**wglUseFontOutlines**](/windows/desktop/api/wingdi/nf-wingdi-wglusefontoutlinesa) functions. To draw characters in a string using those display lists, call [**glCallLists**](glcalllists.md).

To create applications that are easy to localize and that use resources sparingly, the creation and storage of these glyph image display lists must be managed carefully. Many languages, unlike English, have alphabets whose character codes range over a relatively large set of values.

## Related topics

<dl> <dt>

[Font and Text Functions](font-and-text-functions.md)
</dt> </dl>

 

 




