---
description: The ExcludeUpdateRgn function excludes the update region from the clipping region for the display device context.
ms.assetid: e652122b-a3b7-4d1b-8afd-9648d5ee3d42
title: Excluding the Update Region
ms.topic: article
ms.date: 05/31/2018
---

# Excluding the Update Region

The [**ExcludeUpdateRgn**](/windows/desktop/api/Winuser/nf-winuser-excludeupdatergn) function excludes the update region from the clipping region for the display device context. This function is useful when drawing in a window other than when a WM\_PAINT message is processing. It prevents drawing in the areas that will be updated during the next WM\_PAINT message.

 

 



