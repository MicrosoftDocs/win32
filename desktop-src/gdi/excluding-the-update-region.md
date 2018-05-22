---
Description: 'The ExcludeUpdateRgn function excludes the update region from the clipping region for the display device context.'
ms.assetid: 'e652122b-a3b7-4d1b-8afd-9648d5ee3d42'
title: Excluding the Update Region
---

# Excluding the Update Region

The [**ExcludeUpdateRgn**](excludeupdatergn.md) function excludes the update region from the clipping region for the display device context. This function is useful when drawing in a window other than when a WM\_PAINT message is processing. It prevents drawing in the areas that will be updated during the next WM\_PAINT message.

 

 



