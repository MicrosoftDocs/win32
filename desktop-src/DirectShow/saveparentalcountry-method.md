---
description: The DVDAdm.SaveParentalCountry method saves the application's new parental country/region to the registry.
ms.assetid: 2185ad7d-c7c1-4d8b-82e7-5ed5fffaff26
title: SaveParentalCountry Method (Segment.h)
ms.topic: reference
ms.date: 05/31/2018
---

# SaveParentalCountry Method

> [!Note]  
> This component is available for use in the Microsoft Windows 2000, Windows XP, and Windows Server 2003 operating systems. It may be altered or unavailable in subsequent versions.

 

The `DVDAdm.SaveParentalCountry` method saves the application's new parental country/region to the registry.

``` syntax
DVD.DVDAdm.SaveParentalCountry(iCountry, sUserName, sPassword)
```

## Parameters

<dl> <dt>

<span id="iCountry"></span><span id="icountry"></span><span id="ICOUNTRY"></span>*iCountry*
</dt> <dd>

Specifies the parental country/region as an Integer.

</dd> <dt>

<span id="sUserName"></span><span id="susername"></span><span id="SUSERNAME"></span>*sUserName*
</dt> <dd>

Specifies the user name as a String. (Currently ignored.)

</dd> <dt>

<span id="sPassword"></span><span id="spassword"></span><span id="SPASSWORD"></span>*sPassword*
</dt> <dd>

Specifies the password as a String.

</dd> </dl>

## Return value

No return value.

## Remarks

This method enables a user who knows the current password to save a new parental country/region setting to the registry. As with all the methods of **MSDVDAdm**, this method does not affect the current level in the player; it changes only the registry setting, so that the next time the MSWebDVD object is created, it will open with the new country/region. To change the parental country/region in the player, call [**SelectParentalCountry**](selectparentalcountry-method.md), which does not change the registry setting.

## Requirements



| Requirement | Value |
|-------------------|--------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Segment.h</dt> </dl> |



## See also

<dl> <dt>

[**SaveParentalLevel**](saveparentallevel-method.md)
</dt> <dt>

[MSDVDAdm Object](msdvdadm-object.md)
</dt> </dl>

 

 




