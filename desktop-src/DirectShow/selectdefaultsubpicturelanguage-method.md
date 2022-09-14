---
description: The SelectDefaultSubpictureLanguage method sets the current default subpicture language in the MSWebDVD object.
ms.assetid: e83980d1-c7cd-4755-9a27-3b0c2548009e
title: SelectDefaultSubpictureLanguage Method
ms.topic: reference
ms.date: 05/31/2018
---

# SelectDefaultSubpictureLanguage Method

> [!Note]  
> This component is available for use in the Microsoft Windows 2000, Windows XP, and Windows Server 2003 operating systems. It may be altered or unavailable in subsequent versions.

 

The `SelectDefaultSubpictureLanguage` method sets the current default subpicture language in the **MSWebDVD** object.

``` syntax
MSWebDVD.SelectDefaultSubpictureLanguage(iLang,iExt)
```

## Parameters

<dl> <dt>

<span id="iLang"></span><span id="ilang"></span><span id="ILANG"></span>*iLang*
</dt> <dd>

Specifies the language as an Integer.

</dd> <dt>

<span id="iExt"></span><span id="iext"></span><span id="IEXT"></span>*iExt*
</dt> <dd>

Specifies the subpicture language extension as an Integer.



| Value | Description                    |
|-------|--------------------------------|
| 0     | Extension Not Specified        |
| 1     | Normal Captions                |
| 2     | Big Captions                   |
| 3     | Children's Captions            |
| 5     | Normal Closed Captions         |
| 6     | Big Closed Captions            |
| 7     | Children's Closed Captions     |
| 9     | Forced                         |
| 13    | Normal Director's Comments     |
| 14    | Big Director's Comments        |
| 15    | Children's Director's Comments |



 

</dd> </dl>

## Return Value

No return value.

## Remarks

The subpicture language extension provides further information about the subpicture.

 

 



