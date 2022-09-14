---
description: The DVDAdm.SaveParentalLevel method saves a new default parental level to the registry.
ms.assetid: 8ad22098-acbd-41fd-9224-829b3cc5f8ae
title: SaveParentalLevel Method (Segment.h)
ms.topic: reference
ms.date: 05/31/2018
---

# SaveParentalLevel Method

> [!Note]  
> This component is available for use in the Microsoft Windows 2000, Windows XP, and Windows Server 2003 operating systems. It may be altered or unavailable in subsequent versions.

 

The **DVDAdm.SaveParentalLevel** method saves a new default parental level to the registry.

``` syntax
DVD.DVDAdm.SaveParentalLevel(iLevel, sUserName, sPassword)
```

## Parameters

<dl> <dt>

<span id="iLevel"></span><span id="ilevel"></span><span id="ILEVEL"></span>*iLevel*
</dt> <dd>

Specifies the parental level as anInteger value from 1 through 8.

</dd> <dt>

<span id="sUserName"></span><span id="susername"></span><span id="SUSERNAME"></span>*sUserName*
</dt> <dd>

Specifies the user name as a String. (Currently ignored.)

</dd> <dt>

<span id="sPassword"></span><span id="spassword"></span><span id="SPASSWORD"></span>*sPassword*
</dt> <dd>

Specifies the password as a String.

</dd> </dl>

## Return Value

No return value.

## Remarks

This method enables a user who knows the current password to save a new parental level setting to the registry. As with all the methods of **MSDVDAdm**, this method does not affect the current level in the player; it changes only the registry setting, so that the next time the MSWebDVD object is started, it will open with the new level. Specify -1 to disable parental management. To change the parental level in the player, call [**SelectParentalLevel**](selectparentallevel-method.md), which does not change the registry setting.

## Requirements



| Requirement | Value |
|-------------------|--------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Segment.h</dt> </dl> |



## See also

<dl> <dt>

[MSDVDAdm Object](msdvdadm-object.md)
</dt> </dl>

 

 




