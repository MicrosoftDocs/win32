---
description: The GetNumberOfChapters method retrieves the number of chapters in the specified title.
ms.assetid: d1291f6d-9296-486f-adad-d8819a4e54d6
title: GetNumberOfChapters Method
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# GetNumberOfChapters Method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> This component is available for use in the Microsoft Windows 2000, Windows XP, and Windows Server 2003 operating systems. It may be altered or unavailable in subsequent versions.

 

The `GetNumberOfChapters` method retrieves the number of chapters in the specified title.

``` syntax
[iChapters = ] MSWebDVD.GetNumberOfChapters(iTitle)
```

## Parameters

<dl> <dt>

<span id="iTitle"></span><span id="ititle"></span><span id="ITITLE"></span>*iTitle*
</dt> <dd>

Specifies the title as an Integer.

</dd> </dl>

## Return Value

Returns an integer value from 1 through 999 indicating the number of chapters.

 

 



