---
description: Per-Pixel Alpha Blending
ms.assetid: 68661dc5-1423-47b2-a0df-858e5eb7f02b
title: Per-Pixel Alpha Blending
ms.topic: article
ms.date: 05/31/2018
---

# Per-Pixel Alpha Blending

Four media subtypes have been defined for per-pixel alpha blending. These subtypes are only supported when the VMR is in mixing mode. The VMR will reject the connection if it is not in mixing mode when an upstream filter attempts to connect using one of these subtypes. These subtypes are defined in uuids.h:

-   MEDIASUBTYPE\_ARGB1555
-   MEDIASUBTYPE\_ARGB4444
-   MEDIASUBTYPE\_ARGB32
-   MEDIASUBTYPE\_AYUV

For more information, see [Uncompressed RGB Video Subtypes](uncompressed-rgb-video-subtypes.md) and [**YUV Video Subtypes**](yuv-video-subtypes.md).

 

 



