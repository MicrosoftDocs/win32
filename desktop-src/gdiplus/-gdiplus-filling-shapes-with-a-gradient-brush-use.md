---
description: You can use a gradient brush to fill a shape with a gradually changing color.
ms.assetid: e37b4c3a-b753-483a-990f-da3bcc70acf5
title: Filling Shapes with a Gradient Brush
ms.topic: article
ms.date: 05/31/2018
---

# Filling Shapes with a Gradient Brush

You can use a gradient brush to fill a shape with a gradually changing color. For example, you can use a horizontal gradient to fill a shape with color that changes gradually as you move from the left edge of the shape to the right edge. Imagine a rectangle with a left edge that is black (represented by red, green, and blue components 0, 0, 0) and a right edge that is red (represented by 255, 0, 0). If the rectangle is 256 pixels wide, the red component of a given pixel will be one greater than the red component of the pixel to its left. The leftmost pixel in a row has color components (0, 0, 0), the second pixel has (1, 0, 0), the third pixel has (2, 0, 0), and so on, until you get to the rightmost pixel, which has color components (255, 0, 0). These interpolated color values make up the color gradient.

A linear gradient changes color as you move horizontally, vertically, or parallel to a specified slanted line. A path gradient changes color as you move about the interior and boundary of a path. You can customize path gradients to achieve a wide variety of effects.

GDI+ provides the [**LinearGradientBrush**](/windows/desktop/api/gdiplusbrush/nl-gdiplusbrush-lineargradientbrush) and [**PathGradientBrush**](/windows/desktop/api/gdipluspath/nl-gdipluspath-pathgradientbrush) classes, both of which inherit from the [**Brush**](/windows/desktop/api/gdiplusbrush/nl-gdiplusbrush-brush) class.

The following topics cover linear and path gradients in more detail:

-   [Creating a Linear Gradient](-gdiplus-creating-a-linear-gradient-use.md)
-   [Creating a Path Gradient](-gdiplus-creating-a-path-gradient-use.md)
-   [Applying Gamma Correction to a Gradient](-gdiplus-applying-gamma-correction-to-a-gradient-use.md)

 

 



