---
description: The DVDAdm.GetParentalCountry method retrieves the parental country/region that was last saved to the registry.
ms.assetid: 947c5e2a-dfd5-4900-87d4-0ec967b99a22
title: GetParentalCountry Method (Segment.h)
ms.topic: reference
ms.date: 05/31/2018
---

# GetParentalCountry Method

> [!Note]  
> This component is available for use in the Microsoft Windows 2000, Windows XP, and Windows Server 2003 operating systems. It may be altered or unavailable in subsequent versions.

 

The `DVDAdm.GetParentalCountry` method retrieves the parental country/region that was last saved to the registry.

``` syntax
[ iParentalCountry = ] DVD.DVDAdm.GetParentalCountry()
```

## Return Value

Returns an Integer indicating the default country/region code stored in the registry.

## Remarks

The parental country/region this method retrieves is not necessarily the same country/region currently stored in the MSWebDVD object.

## Requirements



| Requirement | Value |
|-------------------|--------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Segment.h</dt> </dl> |



## See also

<dl> <dt>

[MSDVDAdm Object](msdvdadm-object.md)
</dt> </dl>

 

 




