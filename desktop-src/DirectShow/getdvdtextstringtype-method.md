---
description: The GetDVDTextStringType method retrieves a value that indicates the type of information contained in the specified DVD text string.
ms.assetid: 8e22fa2e-e7eb-4dd8-b365-631986bad03e
title: GetDVDTextStringType Method
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# GetDVDTextStringType Method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> This component is available for use in the Microsoft Windows 2000, Windows XP, and Windows Server 2003 operating systems. It may be altered or unavailable in subsequent versions.

 

The `GetDVDTextStringType` method retrieves a value that indicates the type of information contained in the specified DVD text string.

``` syntax
[ iStringType = ] MSWebDVD.GetDVDTextStringType(iLangIndex, iStringIndex)
```

## Parameters

<dl> <dt>

<span id="iLangIndex"></span><span id="ilangindex"></span><span id="ILANGINDEX"></span>*iLangIndex*
</dt> <dd>

Specifies the language of the text string as an Integer.

</dd> <dt>

<span id="iStringIndex"></span><span id="istringindex"></span><span id="ISTRINGINDEX"></span>*iStringIndex*
</dt> <dd>

Specifies the index number of the text string as an Integer.

</dd> </dl>

## Return Value

Returns an integer value that indicates the type of information contained in the string.

## See also

<dl> <dt>

[MSWebDVD Object](mswebdvd-object.md)
</dt> </dl>

 

 



