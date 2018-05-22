---
Description: 'A number of functions use the brush currently selected into a device context to perform bitmap operations.'
ms.assetid: '98fb2fd5-9cf4-4016-9e30-ec724e77cebc'
title: Bitmaps as Brushes
---

# Bitmaps as Brushes

A number of functions use the brush currently selected into a device context to perform bitmap operations. For example, the [**PatBlt**](patblt.md) function replicates the brush in a rectangular region within a window, and the [**FloodFill**](floodfill.md) function replicates the brush inside an area in a window bounded by the specified color (unlike **PatBlt**, **FloodFill** does fill nonrectangular shapes).

The [**FloodFill**](floodfill.md) function replicates the brush within a region bounded by a specified color. However, unlike the [**PatBlt**](patblt.md) function, **FloodFill** does not combine the color data for the brush with the color data for the pixels on the display; it simply sets the color of all pixels within the enclosed region on the display to the color of the brush that is currently selected into the device context.

 

 



