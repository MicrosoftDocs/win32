---
description: Most applications attempt to support WYSIWYG (what you see is what you get) output.
ms.assetid: 34a1f37c-0fbf-451b-bb55-80ad85bcd4de
title: WYSIWYG Display and Output
ms.topic: article
ms.date: 05/31/2018
---

# WYSIWYG Display and Output

Most applications attempt to support WYSIWYG (what you see is what you get) output. This means that text drawn with a 10-point Helvetica bold font in the application window should have a similar appearance when it is printed. Obtaining true WYSIWYG output is virtually impossible and even undesirable in most cases. This is due, in part, to the differences in video and printer technologies; a pixel on a screen is generally larger than a dot on a common laser printer. Viewing distances are different as well; a computer user typically sits about two feet away from the screen, but a reader's eyes are usually one foot or less from the printed page.

To compensate for legibility differences between screens and the printed page, the system supports a unit called the logical inch that is always specified in pixels. For a video display, the logical inch is always greater than the physical inch to compensate for the longer viewing distance and the (generally) coarser resolution. For printers, the logical inch is always equal to the physical inch.

To obtain a WYSIWYG effect when drawing text, two related issues are involved: making individual characters look the same, and device-independent page layout. To address the first issue, an application can use the [**CreateFont**](/windows/desktop/api/wingdi/nf-wingdi-createfonta) function to specify the font name and size of an ideal (or logical) font and then call the [**SelectObject**](/windows/desktop/api/wingdi/nf-wingdi-selectobject) function to identify the display or printer device context. When the application calls **SelectObject** , the system selects a physical font that is the closest possible match to the specified logical font. When the system selects the display font, it chooses a physical font that is larger than the actual size. This occurs because of the larger logical inch on the display. From the user's perspective, however, it appears to be very close to the correct height. When the system selects the font for the printer, it chooses a physical font that is actually the requested size. For more information about fonts and text output, see [Fonts and Text](/windows/desktop/gdi/fonts-and-text).

The second issue, that of device-independent page layout, can be addressed by the use of TrueType metrics. This is true even when maintaining compatibility with 16-bit versions of Windows. For more information, see [Using Portable TrueType Metrics](/windows/desktop/gdi/using-portable-truetype-metrics).

To obtain a WYSIWYG effect when drawing bitmapped graphics, an application can retrieve the width and height, in logical inches, of the screen and the printed page. Using these values, the application can create horizontal and vertical scaling factors to maintain the proportion of bitmapped images when they are drawn on a printer. For more information about bitmaps and bitmap output, see [Bitmaps](/windows/desktop/gdi/bitmaps).

 

 
