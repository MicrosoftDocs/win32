---
description: To edit a picture stored in an enhanced metafile, an application must perform the tasks described in the following procedure.
ms.assetid: 19d9c523-cff8-47e1-bbf2-16d8991dac3b
title: Editing an Enhanced Metafile
ms.topic: article
ms.date: 05/31/2018
---

# Editing an Enhanced Metafile

To edit a picture stored in an enhanced metafile, an application must perform the tasks described in the following procedure.

**To edit a picture stored in an enhanced metafile**

1.  Use hit-testing to capture the cursor coordinates and retrieve the position of the object (line, arc, rectangle, ellipse, polygon, or irregular shape) that the user wants to alter.
2.  Convert these coordinates to logical (or world) units.
3.  Call the [**EnumEnhMetaFile**](/windows/desktop/api/Wingdi/nf-wingdi-enumenhmetafile) function and examine each metafile record.
4.  Determine whether a given record corresponds to a GDI drawing function.
5.  If it does, determine whether the coordinates stored in the record correspond to the line, arc, ellipse, or other graphics element that intersects the coordinates specified by the user.
6.  Upon finding the record that corresponds to the output that the user wants to alter, erase the object on the screen that corresponds to the original record.
7.  Delete the corresponding record from the metafile, saving a pointer to its location.
8.  Permit the user to redraw or replace the object.
9.  Convert the GDI functions used to draw the new object into one or more enhanced-metafile records.
10. Store these records in the enhanced metafile.

 

 



