---
title: Pixel Format Functions
description: The following Windows functions manage pixel formats.
ms.assetid: '78a6be75-72f6-4aef-a6bc-5f052c6fe2e9'
keywords: ["WGL functions,pixel format"]
---

# Pixel Format Functions

The following Windows functions manage pixel formats.



| Windows Function                                               | Description                                                                                                                                                           |
|----------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ChoosePixelFormat**](choosepixelformat.md)                 | Obtains the device context's pixel format that is the closest match to a specified pixel format.                                                                      |
| [**SetPixelFormat**](setpixelformat.md)                       | Sets a device context's current pixel format to the pixel format specified by a pixel format index.                                                                   |
| [**GetPixelFormat**](getpixelformat.md)                       | Obtains the pixel format index of a device context's current pixel format.                                                                                            |
| [**DescribePixelFormat**](describepixelformat.md)             | Given a device context and a pixel format index, fills in a [**PIXELFORMATDESCRIPTOR**](pixelformatdescriptor.md) data structure with the pixel format's properties. |
| [**GetEnhMetaFilePixelFormat**](getenhmetafilepixelformat.md) | Retrieves pixel format information for an enhanced metafile.                                                                                                          |



 

The [**ChoosePixelFormat**](choosepixelformat.md) function returns a one-based pixel format index that identifies the best match from the device context's supported pixel formats.

The [**SetPixelFormat**](setpixelformat.md) function identifies the desired format using a one-based pixel format index. Typically, you call **ChoosePixelFormat** to find a best-match pixel format, and then call **SetPixelFormat** with the result of **ChoosePixelFormat**.

If you call **SetPixelFormat** for a device context that references a window, **SetPixelFormat** also changes the pixel format of the window. Setting the pixel format of a window more than once can lead to significant complications for the Window Manager and for multithread applications, so it is not allowed. You can set the pixel format of a window only one time; after that, the window's pixel format cannot be changed.

The [**GetPixelFormat**](getpixelformat.md) function returns a one-based pixel format index.

The [**DescribePixelFormat**](describepixelformat.md) function takes the following as parameters:

-   A handle to a device context
-   A pixel format index
-   A pointer to a [**PIXELFORMATDESCRIPTOR**](pixelformatdescriptor.md) data structure

The [**DescribePixelFormat**](describepixelformat.md) function returns with the members of **PIXELFORMATDESCRIPTOR** appropriately set.

The **GetEnhMetaFilePixelFormat** function returns the size of a metafile's pixel format and retrieves the pixel format information of the metafile.

 

 




