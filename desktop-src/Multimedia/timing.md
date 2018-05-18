---
title: Timing
description: Timing
ms.assetid: '9ab284c7-eebc-4b44-b9e1-cc95efde22c1'
keywords: ["DrawDib,timing", "DrawDibTime function", "DrawDib,debugging", "debugging DrawDib"]
---

# Timing

As part of debugging an application, you can obtain information about the amount of time required to complete repetitive DrawDib operations. The [**DrawDibTime**](drawdibtime.md) function returns timing information for the following operations:

-   Drawing a bitmap
-   Decompressing a bitmap
-   Dithering a bitmap
-   Stretching a bitmap
-   Transferring a bitmap by using the [**BitBlt**](https://msdn.microsoft.com/library/windows/desktop/dd183370) function
-   Transferring a bitmap by using the [**StretchDIBits**](https://msdn.microsoft.com/library/windows/desktop/dd145121) function

After retrieving a set of values, [**DrawDibTime**](drawdibtime.md) resets the count and value for each operation.

The [**DrawDibTime**](drawdibtime.md) function is available only in the debug version of the DrawDib functions.

## Related topics

<dl> <dt>

[Image Rendering](image-rendering.md)
</dt> </dl>

 

 




