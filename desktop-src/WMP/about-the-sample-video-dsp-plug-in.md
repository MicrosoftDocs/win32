---
title: About the Sample Video DSP Plug-in
description: About the Sample Video DSP Plug-in
ms.assetid: f2ba8e9d-a0e4-4679-99dc-2bfe9e451ffd
keywords:
- Windows Media Player plug-ins,samples
- plug-ins,samples
- digital signal processing plug-ins,samples
- DSP plug-ins,samples
- Windows Media Player plug-ins,video DSP
- plug-ins,video DSP
- digital signal processing plug-ins,video samples
- DSP plug-ins,video samples
- samples,DSP plug-ins
- video DSP plug-ins,samples
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# About the Sample Video DSP Plug-in

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The sample video DSP plug-in provides a simple processing implementation that scales the color saturation of the video by a factor provided by the user in the property page. The plug-in accepts values between zero and 1. The default value is 1. A value of 1 has no effect upon the video image; other scale factors desaturate the image color. For instance, a value of .5 would result in 50 percent color saturation. A value of zero results in grayscale video.

The sample video DSP plug-in works with the following video formats:

-   NV12
-   YV12
-   YUY2
-   UYVY
-   RGB32
-   RGB24
-   RGB555
-   RGB565

## Related topics

<dl> <dt>

[**Building a DSP Plug-in**](building-a-dsp-plug-in.md)
</dt> </dl>

 

 




