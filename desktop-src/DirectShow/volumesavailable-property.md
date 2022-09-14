---
description: The VolumesAvailable property retrieves the number of volumes in a multivolume set.
ms.assetid: d056b6d5-f4a4-480b-96a5-8e95dce23dfb
title: VolumesAvailable Property
ms.topic: reference
ms.date: 05/31/2018
---

# VolumesAvailable Property

> [!Note]  
> This component is available for use in the Microsoft Windows 2000, Windows XP, and Windows Server 2003 operating systems. It may be altered or unavailable in subsequent versions.

 

The `VolumesAvailable` property retrieves the number of volumes in a multivolume set.

``` syntax
[ iVolumes = ] MSWebDVD.VolumesAvailable
```

## Return Value

Returns the number of volumes in the set as an Integer.

## Remarks

This property is read-only with no default value. Some DVD titles might be released as a multidisc set or series. Use this method to determine the volume number for the current disc.

 

 



