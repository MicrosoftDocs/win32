---
description: 'There are two types of brushes: logical and physical.'
ms.assetid: 2e15376d-6b4c-41c5-aef8-0dbb91b81505
title: About Brushes
ms.topic: article
ms.date: 05/31/2018
---

# About Brushes

There are two types of brushes: logical and physical. A *logical brush* is a description of the ideal bitmap that an application uses to paint shapes. A *physical brush* is the actual bitmap that a device driver creates based on an application's logical-brush definition. For more information about bitmaps, see [Bitmaps](bitmaps.md).

When an application calls one of the functions that creates a brush, it retrieves a handle that identifies a logical brush. When the application passes this handle to the [**SelectObject**](/windows/desktop/api/Wingdi/nf-wingdi-selectobject) function, the device driver for the corresponding display or printer creates the physical brush.

The following topics describe brushes:

-   [Brush Origin](brush-origin.md)
-   [Logical Brush Types](logical-brush-types.md)
-   [Pattern Block Transfer](pattern-block-transfer.md)
-   [ICM-Enabled Brush Functions](icm-enabled-brush-functions.md)

 

 



