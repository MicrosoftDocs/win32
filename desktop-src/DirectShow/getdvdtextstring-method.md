---
description: The GetDVDTextString method retrieves the specified text string.
ms.assetid: 2b8cea1e-b0b7-4ef7-90a5-aef2978e8098
title: GetDVDTextString Method
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# GetDVDTextString Method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> This component is available for use in the Microsoft Windows 2000, Windows XP, and Windows Server 2003 operating systems. It may be altered or unavailable in subsequent versions.

 

The `GetDVDTextString` method retrieves the specified text string.

``` syntax
[ sText = ] MSWebDVD.GetDVDTextString(iLangIndex, iStringIndex)
```

## Parameters

<dl> <dt>

<span id="iLangIndex"></span><span id="ilangindex"></span><span id="ILANGINDEX"></span>*iLangIndex*
</dt> <dd>

Specifies the index of the language as an Integer.

</dd> <dt>

<span id="iStringIndex"></span><span id="istringindex"></span><span id="ISTRINGINDEX"></span>*iStringIndex*
</dt> <dd>

Specifies the index number of the text string as an Integer.

</dd> </dl>

## Return Value

Returns the String specified by *iStringIndex*.

## See also

<dl> <dt>

[MSWebDVD Object](mswebdvd-object.md)
</dt> <dt>

[**GetDVDTextNumberOfLanguages**](getdvdtextnumberoflanguages-method.md)
</dt> </dl>

 

 



