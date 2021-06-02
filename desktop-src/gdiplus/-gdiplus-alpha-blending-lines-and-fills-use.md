---
description: In Windows GDI+, a color is a 32-bit value with 8 bits each for alpha, red, green, and blue.
ms.assetid: f8c22d1a-b96b-4d16-928e-20adbae4c4a7
title: Alpha Blending Lines and Fills
ms.topic: article
ms.date: 05/31/2018
---

# Alpha Blending Lines and Fills

In Windows GDI+, a color is a 32-bit value with 8 bits each for alpha, red, green, and blue. The alpha value indicates the transparency of the color — the extent to which the color is blended with the background color. Alpha values range from 0 through 255, where 0 represents a fully transparent color, and 255 represents a fully opaque color.

Alpha blending is a pixel-by-pixel blending of source and background color data. Each of the three components (red, green, blue) of a given source color is blended with the corresponding component of the background color according to the following formula:

displayColor = sourceColor × alpha / 255 + backgroundColor × (255 – alpha) / 255

For example, suppose the red component of the source color is 150 and the red component of the background color is 100. If the alpha value is 200, the red component of the resultant color is calculated as follows:

150 × 200 / 255 + 100 × (255 – 200) / 255 = 139

The following topics cover alpha blending in more detail:

-   [Drawing Opaque and Semitransparent Lines](-gdiplus-drawing-opaque-and-semitransparent-lines-use.md)
-   [Drawing with Opaque and Semitransparent Brushes](-gdiplus-drawing-with-opaque-and-semitransparent-brushes-use.md)
-   [Using Compositing Mode to Control Alpha Blending](-gdiplus-using-compositing-mode-to-control-alpha-blending-use.md)
-   [Using a Color Matrix to Set Alpha Values in Images](-gdiplus-using-a-color-matrix-to-set-alpha-values-in-images-use.md)
-   [Setting the Alpha Values of Individual Pixels](-gdiplus-setting-the-alpha-values-of-individual-pixels-use.md)

 

 



