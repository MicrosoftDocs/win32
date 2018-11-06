---
title: The PropertySheet Object
description: The PropertySheet Object
ms.assetid: 9d15d198-a4fe-4c05-a7be-0807a179cd9c
ms.topic: article
ms.date: 05/31/2018
---

# The PropertySheet Object

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

The [**PropertySheet**](https://www.bing.com/search?q=**PropertySheet**) object provides several properties you can use if you want to manipulate the character relative to the Microsoft Agent property sheet (also known as the Advanced Character Options window).

-   [**Height**](height-property-pso.md)
-   [**Left**](left-property-pso.md)
-   [**Page**](page-property.md)
-   [**Top**](top-property-pso.md)
-   [**Visible**](visible-property.md)
-   [**Width**](width-property-pso.md)

If you query [**Height**](height-property-pso.md), [**Left**](left-property-pso.md), [**Top**](top-property-pso.md), and [**Width**](width-property-pso.md) properties before the property sheet has ever been shown, their values return as zero (0). Once shown, these properties return the last position and size of the window (relative to your current screen resolution).

 

 




