---
description: The CurrentVolume property retrieves the volume number for the current root directory.
ms.assetid: f8d06a30-d6d5-43b9-b838-741d781f8d01
title: CurrentVolume Property
ms.topic: reference
ms.date: 05/31/2018
---

# CurrentVolume Property

> [!Note]  
> This component is available for use in the Microsoft Windows 2000, Windows XP, and Windows Server 2003 operating systems. It may be altered or unavailable in subsequent versions.

 

The `CurrentVolume` property retrieves the volume number for the current root directory.

``` syntax
[ iCurVolume = ] MSWebDVD.CurrentVolume
```

## Return Value

Returns an integer value representing the current DVD volume. If a disc is part of a multi-volume set, then the integer value should be greater than zero.

## Remarks

This property is read-only with no default value.

## See also

<dl> <dt>

[**VolumesAvailable**](volumesavailable-property.md)
</dt> </dl>

 

 



