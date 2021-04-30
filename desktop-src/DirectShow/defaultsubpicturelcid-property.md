---
description: The DVDAdm.DefaultSubpictureLCID property sets or retrieves the registry setting for the user-specified default LCID for the subpicture stream.
ms.assetid: 12dd308e-483b-489d-8d81-8da399bfac4d
title: DefaultSubpictureLCID Property
ms.topic: reference
ms.date: 05/31/2018
---

# DefaultSubpictureLCID Property

> [!Note]  
> This component is available for use in the Microsoft Windows 2000, Windows XP, and Windows Server 2003 operating systems. It may be altered or unavailable in subsequent versions.

 

The `DVDAdm.DefaultSubpictureLCID` property sets or retrieves the registry setting for the user-specified default LCID for the subpicture stream.

``` syntax
[ iSubpictureLCID = ] DVD.DVDAdm.DefaultSubpictureLCID
```

## Return Value

Returns an Integer value representing the user-specified default subpicture LCID as stored in the registry settings for the DVD application. This value is not necessarily the same as the default subpicture stream as authored on the DVD. For the range of valid LCIDs, see the Win32 documentation in the Platform SDK.

## Remarks

This property is read/write with no default value. If no default subpicture LCID is specified, the MSDVDAdm object will play the subpicture stream that is marked as the default stream on the disc.

## See also

<dl> <dt>

[MSDVDAdm Object](msdvdadm-object.md)
</dt> </dl>

 

 



