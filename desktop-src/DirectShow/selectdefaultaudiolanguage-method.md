---
description: The SelectDefaultAudioLanguage method sets the current default audio language in the MSWebDVD object.
ms.assetid: 7d63b7ef-2b03-4929-822a-c4d11fb7a825
title: SelectDefaultAudioLanguage Method
ms.topic: reference
ms.date: 05/31/2018
---

# SelectDefaultAudioLanguage Method

> [!Note]  
> This component is available for use in the Microsoft Windows 2000, Windows XP, and Windows Server 2003 operating systems. It may be altered or unavailable in subsequent versions.

 

The `SelectDefaultAudioLanguage` method sets the current default audio language in the MSWebDVD object.

``` syntax
MSWebDVD.SelectDefaultAudioLanguage(iLang, iExt)
```

## Parameters

<dl> <dt>

<span id="iLang"></span><span id="ilang"></span><span id="ILANG"></span>*iLang*
</dt> <dd>

Specifies the language as an Integer LCID value.

</dd> <dt>

<span id="iExt"></span><span id="iext"></span><span id="IEXT"></span>*iExt*
</dt> <dd>

Specifies the DVD audio language extension as an integer value.



| Value | Description       |
|-------|-------------------|
| 0     | NotSpecified      |
| 1     | Captions          |
| 2     | VisuallyImpaired  |
| 3     | DirectorComments1 |
| 4     | DirectorComments2 |



 

</dd> </dl>

## Return Value

No return value.

## See also

<dl> <dt>

[MSWebDVD Object](mswebdvd-object.md)
</dt> </dl>

 

 



