---
description: While the functions discussed in the preceding work well for many languages, they may not deal with the needs of complex scripts.
ms.assetid: a60b50c8-13e8-4c61-989f-187bb67cf929
title: Complex Scripts
ms.topic: article
ms.date: 05/31/2018
---

# Complex Scripts

While the functions discussed in the preceding work well for many languages, they may not deal with the needs of complex scripts. *Complex scripts* are languages whose printed form is not rendered in a simple way. For example, a complex script may allow bidirectional rendering, contextual shaping of glyphs, or combining characters. Due to these special requirements, the control of text output must be very flexible.

Functions that display text [**TextOut**](/windows/desktop/api/Wingdi/nf-wingdi-textouta), [**ExtTextOut**](/windows/desktop/api/Wingdi/nf-wingdi-exttextouta), [**TabbedTextOut**](/windows/desktop/api/Winuser/nf-winuser-tabbedtextouta), [**DrawText**](/windows/desktop/api/Winuser/nf-winuser-drawtext), and [**GetTextExtentExPoint**](/windows/desktop/api/Wingdi/nf-wingdi-gettextextentexpointa) have been extended to support complex scripts. In general, this support is transparent to the application. However, applications should save characters in a buffer and display a whole line of text at one time, so that the complex script shaping modules can use context to reorder and generate glyphs correctly. In addition, because the width of a glyph can vary by context, applications should use [**GetTextExtentExPoint**](/windows/win32/api/wingdi/nf-wingdi-gettextextentexpointa) to determine line length rather than using cached character widths.

In addition, complex script-aware applications should consider adding support for right-to-left reading order and right alignment to their applications. You can toggle the reading order or alignment between left and right with the following code:


```C++
// Save lAlign (this example uses static variables) 
static LONG lAlign = TA_LEFT;

// When user toggles alignment (assuming TA_CENTER is not supported). 

lAlign = TA_RIGHT;

// When the user toggles reading order. 

lAlign = TA_RTLREADING;

// Before calling ExtTextOut, for example, when processing WM_PAINT  

SetTextAlign (hDc, lAlign);
```



To toggle both attributes at once, execute the following statement and then call [**SetTextAlign**](/windows/desktop/api/Wingdi/nf-wingdi-settextalign) and [**ExtTextOut**](/windows/desktop/api/Wingdi/nf-wingdi-exttextouta), as shown previously:


```C++
lAlign = TA_RIGHT^TA_RTLREADING;  //pre-inline !
```



You can also process complex scripts with Uniscribe. Uniscribe is a set of functions that allow a fine degree of control for complex scripts. For more information, see [Uniscribe](../intl/uniscribe.md) and [Processing Complex Scripts](../intl/processing-complex-scripts.md).

 

 
