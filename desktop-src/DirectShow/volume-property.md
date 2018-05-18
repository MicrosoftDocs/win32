---
Description: 'The Volume property sets or retrieves the speaker volume for the audio stream output.'
ms.assetid: 'f8d06a30-d6d5-43b9-b838-741d781f8d01'
title: Volume Property
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

 

 



