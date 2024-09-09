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
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Timing (Windows Multimedia)

\[The feature associated with this page, [DrawDib](/windows/win32/multimedia/drawdib), is a legacy feature. It has been superseded by [MediaComposition class](/uwp/api/Windows.Media.Editing.MediaComposition). **MediaComposition class** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaComposition class** instead of **DrawDib**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

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

 

 
