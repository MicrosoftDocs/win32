---
Description: A Graphics object provides methods such as DrawLine, DrawImage, and DrawString for displaying vector images, raster images, and text.
ms.assetid: 721d0c1c-d105-4d9f-b5e9-6ca407b28c4e
title: Using Graphics Containers
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Using Graphics Containers

A [**Graphics**](/windows/win32/gdiplusgraphics/nl-gdiplusgraphics-graphics?branch=master) object provides methods such as [DrawLine](/windows/win32/gdiplusgraphics/nf-gdiplusgraphics-graphics-drawline(in const pen,in const point &,in const point &)?branch=master), [DrawImage](/windows/win32/gdiplusgraphics/nf-gdiplusgraphics-graphics-drawimage(in image,in const point &)?branch=master), and [DrawString](/windows/win32/gdiplusgraphics/nf-gdiplusgraphics-graphics-drawstring(const wchar,int,const font,const pointf &,const brush)?branch=master) for displaying vector images, raster images, and text. A **Graphics** object also has several properties that influence the quality and orientation of the items that are drawn. For example, the smoothing mode property determines whether antialiasing is applied to lines and curves, and the world transformation property influences the position and rotation of the items that are drawn.

A [**Graphics**](/windows/win32/gdiplusgraphics/nl-gdiplusgraphics-graphics?branch=master) object is often associated with a particular display device. When you use a **Graphics** object to draw in a window, the **Graphics** object is also associated with that particular window.

A [**Graphics**](/windows/win32/gdiplusgraphics/nl-gdiplusgraphics-graphics?branch=master) object can be thought of as a container because it holds a set of properties that influence drawing, and it is linked to device-specific information. You can create a secondary container within an existing **Graphics** object by calling the [BeginContainer](/windows/win32/gdiplusgraphics/?branch=master) method of that **Graphics** object.

The following topics cover [**Graphics**](/windows/win32/gdiplusgraphics/nl-gdiplusgraphics-graphics?branch=master) objects and nested containers in more detail:

-   [The State of a Graphics Object](-gdiplus-the-state-of-a-graphics-object-use.md)
-   [Nested Graphics Containers](-gdiplus-nested-graphics-containers-use.md)

 

 



