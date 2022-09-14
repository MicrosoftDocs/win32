---
description: The GetVideoSize method retrieves the native video dimensions.
ms.assetid: 50db2c15-4064-4d18-94f0-f6cf05f1d236
title: GetVideoSize Method
ms.topic: reference
ms.date: 05/31/2018
---

# GetVideoSize Method

> [!Note]  
> This component is available for use in the Microsoft Windows 2000, Windows XP, and Windows Server 2003 operating systems. It may be altered or unavailable in subsequent versions.

 

The `GetVideoSize` method retrieves the native video dimensions.

``` syntax
[ oSizeRect = ] MSWebDVD.GetVideoSize()
```

## Return Value

Returns a [DVDRect](dvdrect-object.md) object containing four read/write properties: (top left) x; (top left) y, Width, and Height. The **x** and **y** properties are set to zero and the other two properties reflect the width and height of the video rectangle as authored on the disc.

 

 



