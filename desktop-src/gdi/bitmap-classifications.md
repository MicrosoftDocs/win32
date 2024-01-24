---
description: Bitmap Classifications
ms.assetid: 669ffaef-55c5-4cbc-b23a-de3d66bd6ab2
title: Bitmap Classifications
ms.topic: article
ms.date: 05/31/2018
---

# Bitmap Classifications

There are two classes of bitmaps:

-   [Device-independent bitmaps](device-independent-bitmaps.md) (DIB). The DIB file format was designed to ensure that bitmapped graphics created using one application can be loaded and displayed in another application, retaining the same appearance as the original.

-   [Device-dependent bitmaps](device-dependent-bitmaps.md) (DDB), also known as GDI bitmaps, were the only bitmaps available in early versions of 16-bit Microsoft Windows (prior to version 3.0). However, as display technology improved and as the variety of available display devices increased, certain inherent problems surfaced which could only be solved using DIBs. For example, there was no method of storing (or retrieving) the resolution of the display type on which a bitmap was created, so a drawing application could not quickly determine whether a bitmap was suitable for the type of video display device on which the application was running.

    Despite these problems, DDBs (also known as compatible bitmaps) are still useful for better GDI performance and for other situations.

 

 



