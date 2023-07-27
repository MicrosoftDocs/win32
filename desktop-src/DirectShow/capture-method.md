---
description: The Capture method captures a still image from the video frame when the MSWebDVD object is in windowless mode.
ms.assetid: 704e64ef-3593-403c-8ecf-625fb4983882
title: Capture Method
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Capture Method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> This component is available for use in the Microsoft Windows 2000, Windows XP, and Windows Server 2003 operating systems. It may be altered or unavailable in subsequent versions.

 

The `Capture` method captures a still image from the video frame when the MSWebDVD object is in windowless mode.

``` syntax
MSWebDVD.Capture()
```

## Remarks

This method captures the current frame from the DVD-Video image and pastes it into a window from which the user can save or edit the image. The MSWebDVD object must be in windowless mode for this method to succeed.

 

 



