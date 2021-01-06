---
description: The ColorKey property sets or retrieves the color key used in closed captioning.
ms.assetid: 4d4b38e6-bd29-4e16-8f82-a5da9312d272
title: ColorKey Property
ms.topic: reference
ms.date: 05/31/2018
---

# ColorKey Property

> [!Note]  
> This component is available for use in the Microsoft Windows 2000, Windows XP, and Windows Server 2003 operating systems. It may be altered or unavailable in subsequent versions.

 

The `ColorKey` property sets or retrieves the color key used in closed captioning.

``` syntax
[ iColorKey = ] MSWebDVD.ColorKey
```

## Return Value

Returns an integer value representing the color to use as a transparent background for closed-captioned text. The default value in 256 colors is magenta, and off-black in any other color depth.

## Remarks

This property is read/write. This property applies only to the closed-captions, if any exist, not to the subpicture stream.

 

 



