---
title: Pixel Format Functions
description: The following Windows functions manage pixel formats.
ms.assetid: 78a6be75-72f6-4aef-a6bc-5f052c6fe2e9
keywords:
- WGL functions,pixel format
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Pixel Format Functions

The following Windows functions manage pixel formats.



| Windows Function                                               | Description                                                                                                                                                           |
|----------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ChoosePixelFormat**](/windows/win32/wingdi/nf-wingdi-choosepixelformat?branch=master)                 | Obtains the device context's pixel format that is the closest match to a specified pixel format.                                                                      |
| [**SetPixelFormat**](/windows/win32/wingdi/nf-wingdi-setpixelformat?branch=master)                       | Sets a device context's current pixel format to the pixel format specified by a pixel format index.                                                                   |
| [**GetPixelFormat**](/windows/win32/wingdi/nf-wingdi-getpixelformat?branch=master)                       | Obtains the pixel format index of a device context's current pixel format.                                                                                            |
| [**DescribePixelFormat**](/windows/win32/wingdi/nf-wingdi-describepixelformat?branch=master)             | Given a device context and a pixel format index, fills in a [**PIXELFORMATDESCRIPTOR**](/windows/win32/Wingdi/ns-wingdi-tagpixelformatdescriptor?branch=master) data structure with the pixel format's properties. |
| [**GetEnhMetaFilePixelFormat**](/windows/win32/wingdi/nf-wingdi-getenhmetafilepixelformat?branch=master) | Retrieves pixel format information for an enhanced metafile.                                                                                                          |



 

The [**ChoosePixelFormat**](/windows/win32/wingdi/nf-wingdi-choosepixelformat?branch=master) function returns a one-based pixel format index that identifies the best match from the device context's supported pixel formats.

The [**SetPixelFormat**](/windows/win32/wingdi/nf-wingdi-setpixelformat?branch=master) function identifies the desired format using a one-based pixel format index. Typically, you call **ChoosePixelFormat** to find a best-match pixel format, and then call **SetPixelFormat** with the result of **ChoosePixelFormat**.

If you call **SetPixelFormat** for a device context that references a window, **SetPixelFormat** also changes the pixel format of the window. Setting the pixel format of a window more than once can lead to significant complications for the Window Manager and for multithread applications, so it is not allowed. You can set the pixel format of a window only one time; after that, the window's pixel format cannot be changed.

The [**GetPixelFormat**](/windows/win32/wingdi/nf-wingdi-getpixelformat?branch=master) function returns a one-based pixel format index.

The [**DescribePixelFormat**](/windows/win32/wingdi/nf-wingdi-describepixelformat?branch=master) function takes the following as parameters:

-   A handle to a device context
-   A pixel format index
-   A pointer to a [**PIXELFORMATDESCRIPTOR**](/windows/win32/Wingdi/ns-wingdi-tagpixelformatdescriptor?branch=master) data structure

The [**DescribePixelFormat**](/windows/win32/wingdi/nf-wingdi-describepixelformat?branch=master) function returns with the members of **PIXELFORMATDESCRIPTOR** appropriately set.

The **GetEnhMetaFilePixelFormat** function returns the size of a metafile's pixel format and retrieves the pixel format information of the metafile.

 

 




