---
description: The ShowCursor method makes the cursor visible when the MSWebDVD object is in full-screen mode.
ms.assetid: 3a611cc8-7979-473d-bd0f-f4ca43701c63
title: ShowCursor Method
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# ShowCursor Method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> This component is available for use in the Microsoft Windows 2000, Windows XP, and Windows Server 2003 operating systems. It may be altered or unavailable in subsequent versions.

 

The `ShowCursor` method makes the cursor visible when the **MSWebDVD** object is in full-screen mode.

``` syntax
MSWebDVD.ShowCursor(bShow)
```

## Parameters

<dl> <dt>

<span id="bShow"></span><span id="bshow"></span><span id="BSHOW"></span>*bShow*
</dt> <dd>

Specifies whether to show the cursor as a Boolean.



| Value | Description            |
|-------|------------------------|
| true  | Show the cursor        |
| false | Do not show the cursor |



 

</dd> </dl>

## Return Value

No return value.

## Remarks

When the DVD display goes into full-screen mode, the cursor disappears within 3 to 5 seconds. Use this method to make the cursor visible again if your application's control buttons are visible in full-screen mode.

 

 



