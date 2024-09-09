---
description: Setting the Playback Rate
ms.assetid: 74ae45d3-4fea-491c-af1f-46768df41c5f
title: Setting the Playback Rate
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Setting the Playback Rate

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

To change the playback rate, call the [**IMediaSeeking::SetRate**](/windows/desktop/api/Strmif/nf-strmif-imediaseeking-setrate) method. Specify the new rate as a fraction of the original rate. For example, to play at twice-normal speed, use the following:


```C++
pSeek->SetRate(2.0)
```



Rates greater than one are faster than normal. Rates between zero and one are slower than normal. Negative rates are defined as backward playback, but in practice most filters do not support it. Currently none of the standard DirectShow filters support reverse playback.

Regardless of the playback rate, the current position and the stop position are always expressed relative to the original source. For example, if a source file is 20 seconds long at normal playback rate, setting the current position to 10 seconds will seek to the middle of the file. If the playback rate is 2.0, the stop position is 20 seconds, and you seek to the 10-second position, the file will play for 5 seconds of real time: 10 seconds' worth, at twice the normal playback speed. At a playback rate of 2.0, the current position increases at twice the rate of the reference clock.

 

 



