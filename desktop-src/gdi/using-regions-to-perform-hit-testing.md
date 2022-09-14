---
description: The example in Brushes uses regions to simulate a &\#0034;zoomed&\#0034; view of an 8- by 8-pixel monochrome bitmap.
ms.assetid: a8e0cbfe-f05b-46ae-b420-ae34a5efbff3
title: Using Regions to Perform Hit Testing
ms.topic: article
ms.date: 05/31/2018
---

# Using Regions to Perform Hit Testing

The example in [Brushes](brushes.md) uses regions to simulate a "zoomed" view of an 8- by 8-pixel monochrome bitmap. By clicking on the pixels in this bitmap, the user creates a custom brush suitable for drawing operations. The example shows how to use the [**PtInRegion**](/windows/desktop/api/Wingdi/nf-wingdi-ptinregion) function to perform hit testing and the [**InvertRgn**](/windows/desktop/api/Wingdi/nf-wingdi-invertrgn) function to invert the colors in a region.

 

 



