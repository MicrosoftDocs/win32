---
title: Color-Index Mode and Windows Palette Management
description: The color-index mode specifies colors in a logical palette with an index to a specific logical-palette entry.
ms.assetid: 8cf07c3e-8a8b-4f28-a363-34d3c0d33890
keywords:
- OpenGL on Windows,palette management
- OpenGL on Windows,color-index mode
- color-index mode OpenGL
- palette management OpenGL
ms.topic: article
ms.date: 05/31/2018
---

# Color-Index Mode and Windows Palette Management

The color-index mode specifies colors in a logical palette with an index to a specific logical-palette entry. Most GDI programs use color-index palettes, but the RGBA mode works better for OpenGL for several effects, such as shading, lighting, fog, and texture mapping. If having the truest color isn't critical for your OpenGL application, you might choose to use the color-index mode (for example, for a topographic map that uses "false color" to emphasize the elevation gradient).

## Color-Index Mode Palette Sample

The following code sets up a [**PIXELFORMATDESCRIPTOR**](/windows/win32/api/wingdi/ns-wingdi-pixelformatdescriptor) structure that sets the flag of the **iPixelType** member to PFD\_TYPE\_COLORINDEX. This specifies that the application use a color-index palette.


```C++
BOOL bSetupPixelFormat(HDC hdc) 
{ 
    PIXELFORMATDESCRIPTOR pfd, *ppfd; 
    int pixelformat; 
 
    ppfd = &pfd; 
 
    ppfd->nSize = sizeof(PIXELFORMATDESCRIPTOR); 
    ppfd->nVersion = 1; 
    ppfd->dwFlags = PFD_DRAW_TO_WINDOW | PFD_SUPPORT_OPENGL |  
                        PFD_DOUBLEBUFFER; 
    ppfd->dwLayerMask = PFD_MAIN_PLANE; 
 
    /* Set to color-index mode and use the default color palette. */ 
    ppfd->iPixelType = PFD_TYPE_COLORINDEX;  
 
    ppfd->cColorBits = 8; 
    ppfd->cDepthBits = 16; 
    ppfd->cAccumBits = 0; 
    ppfd->cStencilBits = 0; 
 
    pixelformat = ChoosePixelFormat(hdc, ppfd); 
 
    if ( (pixelformat = ChoosePixelFormat(hdc, ppfd)) == 0 ) 
    { 
        MessageBox(NULL, "ChoosePixelFormat failed", "Error", MB_OK); 
        return FALSE; 
    } 
 
    if (SetPixelFormat(hdc, pixelformat, ppfd) == FALSE) 
    { 
        MessageBox(NULL, "SetPixelFormat failed", "Error", MB_OK); 
        return FALSE; 
    } 
 
    return TRUE; 
}
```



 

 




