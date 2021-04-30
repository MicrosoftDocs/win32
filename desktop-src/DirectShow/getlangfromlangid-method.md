---
description: The GetLangFromLangID method retrieves a human-readable string when given a primary language ID.
ms.assetid: 73cff3df-bfcd-4e51-bd41-51545ed82f09
title: GetLangFromLangID Method
ms.topic: reference
ms.date: 05/31/2018
---

# GetLangFromLangID Method

> [!Note]  
> This component is available for use in the Microsoft Windows 2000, Windows XP, and Windows Server 2003 operating systems. It may be altered or unavailable in subsequent versions.

 

The `GetLangFromLangID` method retrieves a human-readable string when given a primary language ID.

``` syntax
[ sLanguage = ] MSWebDVD.GetLangFromLangID(iPrimaryLangID)
```

## Parameters

<dl> <dt>

<span id="iPrimaryLangID"></span><span id="iprimarylangid"></span><span id="IPRIMARYLANGID"></span>*iPrimaryLangID*
</dt> <dd>

Specifies the primary language ID as an Integer.

</dd> </dl>

## Return Value

Returns a String representation of the language that can be displayed in the application's user interface.

## Remarks

Although this method is named `GetLangFromLangID`, the parameter that you pass is actually the primary language ID, not the language ID.

## See also

<dl> <dt>

[**GetAudioLanguage**](getaudiolanguage-method.md)
</dt> <dt>

[**GetDVDTextLanguageLCID**](getdvdtextlanguagelcid-method.md)
</dt> </dl>

 

 



