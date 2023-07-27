---
description: The FullScreenMode property sets or retrieves a value indicating whether the display is in full-screen mode.
ms.assetid: e4682f50-080c-4f38-b2ca-ce4ca6b746d7
title: FullScreenMode Property
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# FullScreenMode Property

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> This component is available for use in the Microsoft Windows 2000, Windows XP, and Windows Server 2003 operating systems. It may be altered or unavailable in subsequent versions.

 

The `FullScreenMode` property sets or retrieves a value indicating whether the display is in full-screen mode.

``` syntax
[ bFullScreen = ] MSWebDVD.FullScreenMode
```

## Return Value

Returns a Boolean value indicating whether to enable or disable full-screen playback.

## Remarks

This property is read/write with a default value of false.



| Value | Description                                            |
|-------|--------------------------------------------------------|
| true  | Enable full-screen playback. This is the default value |
| false | Disable full-screen playback.                          |



 

Full screen mode is only available when the MSWebDVD control is running in windowed mode.

 

 



