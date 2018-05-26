---
Description: Like a clipping region, a clip path is another graphics object that an application can select into a device context.
ms.assetid: 35c4052b-3f11-40bc-9cc9-6f999326a656
title: Clip Paths
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Clip Paths

Like a clipping region, a clip path is another graphics object that an application can select into a device context. Unlike a clipping region, a clip path is always created by an application and it is used for clipping to one or more irregular shapes. For example, an application can use the lines and curves that form the outlines of characters in a string of text to define a clip path.

To create a clip path, it's first necessary to create a path that describes the required irregular shape. Paths are created by calling the appropriate graphics device interface (GDI) drawing functions after calling the [**BeginPath**](/windows/win32/Wingdi/nf-wingdi-beginpath?branch=master) function and before calling the [**EndPath**](/windows/win32/Wingdi/nf-wingdi-endpath?branch=master) function. This collection of functions is called a path bracket. For more information about paths and path brackets, see [Paths](paths.md).

After the path is created, it can be converted to a clip path by calling the [**SelectClipPath**](/windows/win32/Wingdi/nf-wingdi-selectclippath?branch=master) function, identifying a device context, and specifying a usage mode. The usage mode determines how the system combines the new clip path with the device context's original clipping region. The following table describes the usage modes.



| Mode      | Description                                                                                                                  |
|-----------|------------------------------------------------------------------------------------------------------------------------------|
| RGN\_AND  | The clip path includes the intersection (overlapping areas) of the device context's clipping region and the current path.    |
| RGN\_COPY | The clip path is the current path.                                                                                           |
| RGN\_DIFF | The clip path includes the device context's clipping region with any intersecting parts of the current path excluded.        |
| RGN\_OR   | The clip path includes the union (combined areas) of the device context's clipping region and the current path.              |
| RGN\_XOR  | The clip path includes the union of the device context's clipping region and the current path but excludes the intersection. |



 

 

 



