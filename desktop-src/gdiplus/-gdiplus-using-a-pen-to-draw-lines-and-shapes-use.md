---
Description: 'The Graphics class provides a variety of drawing methods including those shown in the following list:'
ms.assetid: d3c8d16c-858a-42a9-a512-3fcfa144f5fc
title: Using a Pen to Draw Lines and Shapes
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Using a Pen to Draw Lines and Shapes

The [**Graphics**](/windows/desktop/api/gdiplusgraphics/nl-gdiplusgraphics-graphics) class provides a variety of drawing methods including those shown in the following list:

-   [DrawLine Methods](/windows/desktop/api/gdiplusgraphics/nf-gdiplusgraphics-graphics-drawline(in const pen,in const point &,in const point &))
-   [DrawRectangle Methods](/windows/desktop/api/gdiplusgraphics/nf-gdiplusgraphics-graphics-drawrectangle(in const pen,in const rect &))
-   [DrawEllipse Methods](/windows/desktop/api/gdiplusgraphics/nf-gdiplusgraphics-graphics-drawellipse(in const pen,in const rect &))
-   [DrawArc Methods](/windows/desktop/api/gdiplusgraphics/nf-gdiplusgraphics-graphics-drawarc(in const pen,in const rect &,in real,in real))
-   [**Graphics::DrawPath**](/windows/desktop/api/Gdiplusgraphics/nf-gdiplusgraphics-graphics-drawpath)
-   [DrawCurve Methods](/windows/desktop/api/gdiplusgraphics/nf-gdiplusgraphics-graphics-drawcurve(in const pen,in const point,in int))
-   [DrawBezier Methods](/windows/desktop/api/gdiplusgraphics/nf-gdiplusgraphics-graphics-drawbezier(in const pen,in const point &,in const point &,in const point &,in const point &))

One of the arguments that you pass to such a drawing method is the address of a [**Pen**](/windows/desktop/api/gdipluspen/nl-gdipluspen-pen) object.

The following topics cover the use of pens in more detail:

-   [Using a Pen to Draw Lines and Rectangles](-gdiplus-using-a-pen-to-draw-lines-and-rectangles-use.md)
-   [Setting Pen Width and Alignment](-gdiplus-setting-pen-width-and-alignment-use.md)
-   [Drawing a Line with Line Caps](-gdiplus-drawing-a-line-with-line-caps-use.md)
-   [Joining Lines](-gdiplus-joining-lines-use.md)
-   [Drawing a Custom Dashed Line](-gdiplus-drawing-a-custom-dashed-line-use.md)
-   [Drawing a Line Filled with a Texture](-gdiplus-drawing-a-line-filled-with-a-texture-use.md)

 

 



