---
description: The installer sets the value of the PrimaryVolumeSpaceRemaining property to a string representing the total number of bytes remaining on the volume referenced by the PrimaryVolumePath property, if all currently selected features were installed.
ms.assetid: 8a59d22f-b8a1-47bf-90f3-f8cadfae8ecd
title: PrimaryVolumeSpaceRemaining property
ms.topic: reference
ms.date: 05/31/2018
---

# PrimaryVolumeSpaceRemaining property

The installer sets the value of the **PrimaryVolumeSpaceRemaining** property to a string representing the total number of bytes remaining on the volume referenced by the [**PrimaryVolumePath**](primaryvolumepath.md) property, if all currently selected features were installed. As with the [**PrimaryVolumeSpaceAvailable**](primaryvolumespaceavailable.md) property, this number is expressed in units of 512 bytes.

## Remarks

Note if this value is to be displayed within a static [Text control](text-control.md), the [FormatSize](formatsize-control-attribute.md) bit can be used to automatically format and label this number in units of kilobytes or megabytes as appropriate.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP<br/> |



## See also

<dl> <dt>

[Properties](properties.md)
</dt> </dl>

 

 




