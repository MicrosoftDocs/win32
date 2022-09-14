---
description: The GetDVDTextLanguageLCID method retrieves the locale identifier (LCID) for the specified text string block.
ms.assetid: feaa1db8-2d33-4c32-8491-f3aa5555e3d3
title: GetDVDTextLanguageLCID Method
ms.topic: reference
ms.date: 05/31/2018
---

# GetDVDTextLanguageLCID Method

> [!Note]  
> This component is available for use in the Microsoft Windows 2000, Windows XP, and Windows Server 2003 operating systems. It may be altered or unavailable in subsequent versions.

 

The `GetDVDTextLanguageLCID` method retrieves the locale identifier (LCID) for the specified text string block.

``` syntax
[ iLCID = ] MSWebDVD.GetDVDTextLanguageLCID(iLangIndex)
```

## Parameters

<dl> <dt>

<span id="iLangIndex"></span><span id="ilangindex"></span><span id="ILANGINDEX"></span>*iLangIndex*
</dt> <dd>

Specifies the text language block on the disc as an Integer.

</dd> </dl>

## Return Value

Returns an LCID value that contains information specifying the language the strings are written in.

## Remarks

Supplemental text strings are stored in contiguous blocks on the disc. Each language has one block of strings. An application specifies these blocks by an index, which must be less than the value returned by [**GetDVDTextNumberOfLanguages**](getdvdtextnumberoflanguages-method.md).

## See also

<dl> <dt>

[MSWebDVD Object](mswebdvd-object.md)
</dt> <dt>

[**GetLangFromLangID**](getlangfromlangid-method.md)
</dt> </dl>

 

 



