---
description: The DefaultSubpictureLanguageExt property retrieves the default DVD subpicture language extension.
ms.assetid: bd437844-6e5c-4237-a968-700a53e18635
title: DefaultSubpictureLanguageExt Property
ms.topic: reference
ms.date: 05/31/2018
---

# DefaultSubpictureLanguageExt Property

> [!Note]  
> This component is available for use in the Microsoft Windows 2000, Windows XP, and Windows Server 2003 operating systems. It may be altered or unavailable in subsequent versions.

 

The `DefaultSubpictureLanguageExt` property retrieves the default DVD subpicture language extension.

``` syntax
[ iLangExt = ] MSWebDVD.DefaultSubpictureLanguageExt
```

## Return Value

Returns an Integer value indicating the default DVD subpicture language extension.

## Remarks

This property is read-only with no default value. The following table shows the possible values.



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



 

## See also

<dl> <dt>

[**SelectDefaultSubpictureLanguage**](selectdefaultsubpicturelanguage-method.md)
</dt> </dl>

 

 



