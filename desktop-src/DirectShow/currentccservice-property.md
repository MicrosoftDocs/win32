---
description: The CurrentCCService property sets or retrieves the current closed captioning service.
ms.assetid: 094cf812-3122-4d5f-af8a-afd1c2264a2b
title: CurrentCCService Property
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# CurrentCCService Property

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> This component is available for use in the Microsoft Windows 2000, Windows XP, and Windows Server 2003 operating systems. It may be altered or unavailable in subsequent versions.

 

The `CurrentCCService` property sets or retrieves the current closed captioning service.

``` syntax
[ iService = ] MSWebDVD.CurrentCCService
```

## Return Value

Returns an integer value indicating the type of closed captioning service enabled.

## Remarks

The possible values of this property are:



| Value | Description                                                          |
|-------|----------------------------------------------------------------------|
| 0x0   | No current service. This is the default value.                       |
| 0x1   | True captioning, first field. Default service.                       |
| 0x2   | Captioning for secondary language, second field. Generally not used. |



 

This property is read/write.

## See also

<dl> <dt>

[**CCActive**](ccactive-property.md)
</dt> </dl>

 

 



