---
title: Timing (Windows Multimedia)
description: Timing
ms.assetid: 9ab284c7-eebc-4b44-b9e1-cc95efde22c1
keywords:
- DrawDib,timing
- DrawDibTime function
- DrawDib,debugging
- debugging DrawDib
ms.topic: article
ms.date: 05/31/2018
---

# Timing (Windows Multimedia)

As part of debugging an application, you can obtain information about the amount of time required to complete repetitive DrawDib operations. The [**DrawDibTime**](/windows/desktop/api/Vfw/nf-vfw-drawdibtime) function returns timing information for the following operations:

-   Drawing a bitmap
-   Decompressing a bitmap
-   Dithering a bitmap
-   Stretching a bitmap
-   Transferring a bitmap by using the [**BitBlt**](/windows/desktop/api/wingdi/nf-wingdi-bitblt) function
-   Transferring a bitmap by using the [**StretchDIBits**](/windows/desktop/api/wingdi/nf-wingdi-stretchdibits) function

After retrieving a set of values, [**DrawDibTime**](/windows/desktop/api/Vfw/nf-vfw-drawdibtime) resets the count and value for each operation.

The [**DrawDibTime**](/windows/desktop/api/Vfw/nf-vfw-drawdibtime) function is available only in the debug version of the DrawDib functions.

## Related topics

<dl> <dt>

[Image Rendering](image-rendering.md)
</dt> </dl>

 

 
