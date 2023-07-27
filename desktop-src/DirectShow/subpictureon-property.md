---
description: The SubpictureOn property sets or retrieves the current subpicture state (on or off).
ms.assetid: fa4500bc-48b4-41ed-8b88-0011a0e51c6f
title: SubpictureOn Property
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# SubpictureOn Property

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> This component is available for use in the Microsoft Windows 2000, Windows XP, and Windows Server 2003 operating systems. It may be altered or unavailable in subsequent versions.

 

The `SubpictureOn` property sets or retrieves the current subpicture state (on or off).

``` syntax
[ bState = ] MSWebDVD.SubpictureOn
```

## Return Value

Returns a Boolean value indicating whether the subpicture is displayed.

## Remarks

This property does not affect display of Closed Captions. Closed Captions are embedded within the video stream. DVD subpictures are transported on a separate stream.

When the subpicture stream is changed using [**CurrentSubpictureStream**](currentsubpicturestream-property.md), the `SubpictureOn` property toggles to **True**.

This property is read/write with a default value of false.

 

 



