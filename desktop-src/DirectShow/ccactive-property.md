---
description: The CCActive property sets or retrieves the current status of closed captioning.
ms.assetid: e12db685-b58e-4dc1-8ddd-e6ee1da28d08
title: CCActive Property
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# CCActive Property

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> This component is available for use in the Microsoft Windows 2000, Windows XP, and Windows Server 2003 operating systems. It may be altered or unavailable in subsequent versions.

 

The `CCActive` property sets or retrieves the current status of closed captioning.

``` syntax
[ bCCActive = ] MSWebDVD.CCActive
```

## Return Value

Returns a Boolean value indicating whether closed captioning is turned on.

## Remarks

This property is read/write with a default value of false.

## See also

<dl> <dt>

[**CurrentCCService**](currentccservice-property.md)
</dt> </dl>

 

 



