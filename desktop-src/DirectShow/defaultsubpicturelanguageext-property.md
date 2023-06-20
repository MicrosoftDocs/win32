---
description: The DefaultSubpictureLanguageExt property retrieves the default DVD subpicture language extension.
ms.assetid: bd437844-6e5c-4237-a968-700a53e18635
title: DefaultSubpictureLanguageExt Property
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# DefaultSubpictureLanguageExt Property

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

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

 

 



