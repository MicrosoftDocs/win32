---
description: The SelectOrActivatButton event is sent when the disc enables or disables the selection or activation of menu buttons.
ms.assetid: 23d49847-36d2-4cfe-bfcf-8b9ac4b920f3
title: SelectOrActivatButton
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# SelectOrActivatButton

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> This component is available for use in the Microsoft Windows 2000, Windows XP, and Windows Server 2003 operating systems. It may be altered or unavailable in subsequent versions.

 

The `SelectOrActivatButton` event is sent when the disc enables or disables the selection or activation of menu buttons.

``` syntax
SelectOrActivatButton(bEnabled)
```

## Parameters

<dl> <dt>

<span id="bEnabled"></span><span id="benabled"></span><span id="BENABLED"></span>*bEnabled*
</dt> <dd>

Specifies whether the operation is enabled or disabled as a Boolean.

</dd> </dl>

 

 



