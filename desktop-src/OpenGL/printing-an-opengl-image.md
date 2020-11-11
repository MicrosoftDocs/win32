---
title: Printing an OpenGL Image
description: You can print OpenGL images rendered in enhanced metafiles.
ms.assetid: 6099cbe2-82f9-46ec-a3ca-74486c111639
keywords:
- OpenGL on Windows,printing
- printing OpenGL images OpenGL
ms.topic: article
ms.date: 05/31/2018
---

# Printing an OpenGL Image

You can print OpenGL images rendered in enhanced metafiles. When you render to a printer device (HDC) it must be backed by a metafile spooler. OpenGL uses memory for depth, color, and other buffers to store graphics output to a printer. Because typical printer resolution requires a significant amount of memory to store the graphics output, printing an OpenGL image might require more memory than is available in the system. To overcome this limitation, the current implementation of OpenGL prints OpenGL graphics in bands. However, this increases the time it takes to print OpenGL images.

Before you print an OpenGL image, you must call the [StartDoc](/windows/desktop/api/wingdi/nf-wingdi-startdoca) function to complete the initialization of a printer device context (DC). After calling **StartDoc**, you can create rendering contexts (HGLRC) to render to the printer device. If you create rendering contexts before calling **StartDoc**, there is no way to determine whether a metafile is spooled.

The following code sample shows how to print an OpenGL image:

``` syntax
HDC            hDC;
DOCINFO        di;
HGLRC          hglrc;

// Call StartDoc to start the document 
StartDoc( hDC, &di );

// Prepare the printer driver to accept data 
StartPage(hDC);

// Create a rendering context using the metafile DC 
hglrc = wglCreateContext ( hDCmetafile );

// Do OpenGL rendering operations here 
    . . .
wglMakeCurrent(NULL, NULL); // Get rid of rendering context 
    . . .
EndPage(hDC); // Finish writing to the page 
EndDoc(hDC); // End the print job
```

For more information on using metafiles, see [Enhanced Metafile Operations](/windows/desktop/gdi/enhanced-metafile-operations).

 

 