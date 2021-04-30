---
description: The Volume property sets or retrieves the speaker volume for the audio stream output.
ms.assetid: 'b6e22d07-525b-4af2-898c-ce3ed16ea9c1'
title: Volume Property
ms.topic: article
ms.date: 05/31/2018
---

# Volume Property

> [!Note]  
> This component is available for use in the Microsoft Windows 2000, Windows XP, and Windows Server 2003 operating systems. It may be altered or unavailable in subsequent versions.

 

The `Volume` property sets or retrieves the speaker volume for the audio stream output.

``` syntax
[ iVolume = ] MSWebDVD.Volume
```

## Return Value

Returns the volume level as attenuation in decibels as an Integer.

## Remarks

This property is read/write with a default value of 0. Full volume is 0, and 10,000 is silence; the scale is logarithmic. Multiply the desired decibel level by 100 (for example 10,000 = 100 dB).

 

 



