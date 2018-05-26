---
Description: A path is a sequence of graphics primitives (lines, rectangles, curves, text, and the like) that can be manipulated and drawn as a single unit. A path can be divided into figures that are either open or closed. A figure can contain several primitives.
ms.assetid: dbfe8cea-bd9e-43ad-85c8-37cce3ef97a4
title: Constructing and Drawing Paths
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Constructing and Drawing Paths

A path is a sequence of graphics primitives (lines, rectangles, curves, text, and the like) that can be manipulated and drawn as a single unit. A path can be divided into *figures* that are either open or closed. A figure can contain several primitives.

You can draw a path by calling the [**Graphics::DrawPath**](/windows/win32/Gdiplusgraphics/nf-gdiplusgraphics-graphics-drawpath?branch=master) method of the [**Graphics**](/windows/win32/gdiplusgraphics/nl-gdiplusgraphics-graphics?branch=master) class, and you can fill a path by calling the [**Graphics::FillPath**](/windows/win32/Gdiplusgraphics/nf-gdiplusgraphics-graphics-fillpath?branch=master) method of the **Graphics** class.

The following topics cover paths in more detail:

-   [Creating Figures from Lines, Curves, and Shapes](-gdiplus-creating-figures-from-lines-curves-and-shapes-use.md)
-   [Filling Open Figures](-gdiplus-filling-open-figures-use.md)

 

 



