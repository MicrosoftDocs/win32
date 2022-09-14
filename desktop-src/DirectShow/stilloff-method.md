---
description: The StillOff method resumes playback, canceling still mode.
ms.assetid: 62091aad-8a78-4543-a844-a4227aed81df
title: StillOff Method
ms.topic: reference
ms.date: 05/31/2018
---

# StillOff Method

> [!Note]  
> This component is available for use in the Microsoft Windows 2000, Windows XP, and Windows Server 2003 operating systems. It may be altered or unavailable in subsequent versions.

 

The `StillOff` method resumes playback, canceling still mode.

``` syntax
MSWebDVD.StillOff()
```

## Return Value

No return value.

## Remarks

The [DVD Navigator](dvd-navigator-filter.md) goes into still mode when it encounters a still frame authored on the disc. It notifies your application by sending an EC\_DVD\_STILL\_ON event. Still mode is different from the DVD Navigator being in a paused state because of a user operation. Calling `StillOff` resumes playback from still mode but does not restart the DVD Navigator when it is in a paused state.

 

 



