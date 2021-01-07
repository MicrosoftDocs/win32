---
description: Internally, a metafile is an array of variable-length structures called metafile records.
ms.assetid: 222f9b8b-d759-49f9-a3ea-ac59f85263b8
title: About Metafiles
ms.topic: article
ms.date: 05/31/2018
---

# About Metafiles

Internally, a metafile is an array of variable-length structures called *metafile records*. The first records in the metafile specify general information such as the resolution of the device on which the picture was created, the dimensions of the picture, and so on. The remaining records, which constitute the bulk of any metafile, correspond to the graphics device interface (GDI) functions required to draw the picture. These records are stored in the metafile after a special metafile device context is created. This metafile device context is then used for all drawing operations required to create the picture. When the system processes a GDI function associated with a metafile DC, it converts the function into the appropriate data and stores this data in a record appended to the metafile.

After a picture is complete and the last record is stored in the metafile, you can pass the metafile to another application by:

-   Using the clipboard
-   Embedding it within another file
-   Storing it on disk
-   Playing it repeatedly

A metafile is *played* when its records are converted to device commands and processed by the appropriate device.

There are two types of metafiles:

-   [Enhanced-format metafiles](enhanced-format-metafiles.md)
-   [Windows-format metafiles](windows-format-metafiles.md)

 

 



