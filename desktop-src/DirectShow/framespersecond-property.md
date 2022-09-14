---
description: The FramesPerSecond property retrieves the video frame rate for the current DVD title.
ms.assetid: c5d36308-1447-4636-9b3a-4a3f93d27789
title: FramesPerSecond Property
ms.topic: reference
ms.date: 05/31/2018
---

# FramesPerSecond Property

> [!Note]  
> This component is available for use in the Microsoft Windows 2000, Windows XP, and Windows Server 2003 operating systems. It may be altered or unavailable in subsequent versions.

 

The `FramesPerSecond` property retrieves the video frame rate for the current DVD title.

``` syntax
[ iFramesPerSec = ] MSWebDVD.FramesPerSecond
```

## Return Value

Returns an integer value representing the video frame rate; either 25 or 30 frames per second.

## Remarks

This property is read-only with no default value. NTSC video signals are displayed at 30 frames per second. PAL is displayed at 25 frames per second. A disc is encoded to play on either NTSC or PAL, but cannot play on both.

 

 



