---
description: The GetDVDTextNumberOfStrings method retrieves the number of text strings available for the specified language.
ms.assetid: 84d2b5b7-b474-48a4-9058-ea9da8109398
title: GetDVDTextNumberOfStrings Method
ms.topic: reference
ms.date: 05/31/2018
---

# GetDVDTextNumberOfStrings Method

> [!Note]  
> This component is available for use in the Microsoft Windows 2000, Windows XP, and Windows Server 2003 operating systems. It may be altered or unavailable in subsequent versions.

 

The `GetDVDTextNumberOfStrings` method retrieves the number of text strings available for the specified language.

``` syntax
[ iStrings = ] MSWebDVD.GetDVDTextNumberOfStrings(iLangIndex)
```

## Parameters

<dl> <dt>

<span id="iLangIndex"></span><span id="ilangindex"></span><span id="ILANGINDEX"></span>*iLangIndex*
</dt> <dd>

Specifies the language as an Integer. The value must range from zero through one less than the value returned by [**GetDVDTextNumberOfLanguages**](getdvdtextnumberoflanguages-method.md).

</dd> </dl>

## Return Value

Returns an integer value specifying how many strings the disc contains in the specified language.

## See also

<dl> <dt>

[MSWebDVD Object](mswebdvd-object.md)
</dt> </dl>

 

 



