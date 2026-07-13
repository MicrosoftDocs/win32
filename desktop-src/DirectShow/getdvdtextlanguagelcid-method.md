---
description: The GetDVDTextLanguageLCID method retrieves the locale identifier (LCID) for the specified text string block.
ms.assetid: feaa1db8-2d33-4c32-8491-f3aa5555e3d3
title: GetDVDTextLanguageLCID Method
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# GetDVDTextLanguageLCID Method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

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

 

 



