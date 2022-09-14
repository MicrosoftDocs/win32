---
description: The DefaultAudioLanguageExt property retrieves the default DVD audio language extension.
ms.assetid: 628af2aa-e528-4689-953b-558e13e1d513
title: DefaultAudioLanguageExt Property
ms.topic: reference
ms.date: 05/31/2018
---

# DefaultAudioLanguageExt Property

> [!Note]  
> This component is available for use in the Microsoft Windows 2000, Windows XP, and Windows Server 2003 operating systems. It may be altered or unavailable in subsequent versions.

 

The `DefaultAudioLanguageExt` property retrieves the default DVD audio language extension.

``` syntax
[ iLangExt = ] MSWebDVD.DefaultAudioLanguageExt
```

## Return Value

Returns an integer value indicating the default audio language extension. See Remarks for the possible values.

## Remarks

This property is read-only with no default value. The following table shows the possible values for DVD audio language extensions.



| Value | Description       |
|-------|-------------------|
| 0     | NotSpecified      |
| 1     | Captions          |
| 2     | VisuallyImpaired  |
| 3     | DirectorComments1 |
| 4     | DirectorComments2 |



 

 

 



