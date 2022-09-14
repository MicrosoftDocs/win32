---
description: Enhanced-Format Metafiles
ms.assetid: 8d7015cb-5e1d-4805-a7a8-1f8b693e0681
title: Enhanced-Format Metafiles
ms.topic: article
ms.date: 05/31/2018
---

# Enhanced-Format Metafiles

The *enhanced-format metafile* consists of the following elements:

-   A header
-   A table of handles to GDI objects
-   A private palette
-   An array of metafile records

Enhanced metafiles provide true device independence. You can think of the picture stored in an enhanced metafile as a "snapshot" of the video display taken at a particular moment. This "snapshot" maintains its dimensions no matter where it appears on a printer, a plotter, the desktop, or in the client area of any application.

You can use enhanced metafiles to store a picture created by using the GDI functions (including new path and transformation functions). Because the enhanced metafile format is standardized, pictures that are stored in this format can be copied from one application to another; and, because the pictures are truly device independent, they are guaranteed to maintain their shape and proportion on any output device.

-   [Enhanced Metafile Records](enhanced-metafile-records.md)
-   [Enhanced Metafile Creation](enhanced-metafile-creation.md)
-   [Enhanced Metafile Operations](enhanced-metafile-operations.md)

 

 



