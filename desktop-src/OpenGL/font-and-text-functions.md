---
title: Font and Text Functions (OpenGL)
description: The following functions can be used to manage fonts and text.
ms.assetid: 42e16967-1eeb-4d37-bbd6-33c473eb2757
keywords:
- WGL functions,text
- WGL functions,font
ms.topic: article
ms.date: 05/31/2018
---

# Font and Text Functions (OpenGL)

The following functions can be used to manage fonts and text.



| Windows Function                                 | Description                                                                                                                                                                                                                      |
|--------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**wglUseFontBitmaps**](/windows/desktop/api/wingdi/nf-wingdi-wglusefontbitmapsa)   | Creates a set of character bitmap display lists. Characters come from a specified device context's current font. Characters are specified as a consecutive run within the font's glyph set.                                      |
| [**wglUseFontOutlines**](/windows/desktop/api/wingdi/nf-wingdi-wglusefontoutlinesa) | Creates a set of display lists, based on the glyphs of the currently selected outline font of a device context, for use with the current rendering context. The display lists are used to draw 3-D characters of TrueType fonts. |



 

The **wglUseFontBitmaps** and **wglUseFontOutlines** functions take a handle to a device context, and use that device context's current font as a source for the bitmaps. It is therefore necessary to set the device context's font and the font's properties before calling **wglUseFontBitmaps** or **wglUseFontOutlines**.

The [**wglUseFontBitmaps**](/windows/desktop/api/wingdi/nf-wingdi-wglusefontbitmapsa) and [**wglUseFontOutlines**](/windows/desktop/api/wingdi/nf-wingdi-wglusefontoutlinesa) functions also take a parameter that turns the first glyph in the font into a bitmap display list, and a parameter that specifies how many glyphs to turn into display lists. The function then creates display lists for the specified consecutive run of glyphs. For example:

-   To create a set of 224 bitmap display lists for all of the Windows character set glyphs, set these two parameters to 32 and 224, respectively.
-   To create a set of 256 bitmap display lists for all of the OEM character set glyphs, set these two parameters to 0 and 256, respectively.
-   To create a single bitmap display list for any single character set glyph, set the second of these parameters to 1.

The **wglUseFontBitmaps** and **wglUseFontOutlines** functions represent a null glyph in a font with an empty display list.

The display lists created by a call to **wglUseFontBitmaps** or **wglUseFontOutlines** are automatically numbered consecutively.

After calling the [**wglUseFontBitmaps**](/windows/desktop/api/wingdi/nf-wingdi-wglusefontbitmapsa) or [**wglUseFontOutlines**](/windows/desktop/api/wingdi/nf-wingdi-wglusefontoutlinesa) function, call [**glCallLists**](glcalllists.md) to draw a string of characters. See [Drawing Text in a Double-Buffered OpenGL Window](drawing-text-in-a-double-buffered-opengl-window.md) for sample code. In this context, **glCallLists** uses each character in a string as an index into the array of consecutively numbered display lists created by **wglUseFontBitmaps** or **wglUseFontOutlines**.

When you finish drawing text, call the [**glDeleteLists**](gldeletelists.md) function to release the contiguous set of display lists created by **wglUseFontBitmaps** and **wglUseFontOutlines**.

 

 




