---
description: The DVDAdm.DefaultMenuLCID property sets or retrieves the registry setting for the user-specified default LCID for menus.
ms.assetid: 49e64b89-5914-4797-8aa6-2e3f253e494a
title: DefaultMenuLCID Property
ms.topic: reference
ms.date: 05/31/2018
---

# DefaultMenuLCID Property

> [!Note]  
> This component is available for use in the Microsoft Windows 2000, Windows XP, and Windows Server 2003 operating systems. It may be altered or unavailable in subsequent versions.

 

The `DVDAdm.DefaultMenuLCID` property sets or retrieves the registry setting for the user-specified default LCID for menus.

``` syntax
[ iMenuLCID = ] DVD.DVDAdm.DefaultMenuLCID
```

## Return Value

Returns an Integer value representing the LCID as stored in the registry settings for the DVD application. This value is not necessarily the same as the default menu language as authored on the DVD. For the range of valid LCIDs, see the Win32 documentation in the Platform SDK.

## Remarks

This property is read/write with no default value. If no default menu LCID is specified, the MSDVDAdm object will use the language that is marked as the default menu language on the disc.

## See also

<dl> <dt>

[MSDVDAdm Object](msdvdadm-object.md)
</dt> </dl>

 

 



