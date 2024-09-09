---
description: DVD Drive Spin Down Timeout
ms.assetid: 2295253d-0199-41b4-95a8-cda049ca93c7
title: DVD Drive Spin Down Timeout
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# DVD Drive Spin Down Timeout

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

On laptop computers, to conserve battery life it may be desirable to reduce the length of time that a DVD drive will continue to spin after the user has paused playback. By default, the DVD Navigator keeps the disc spinning for two minutes. This value can be modified in the Windows Registry under this key:


```C++
DWORD HKLM\SOFTWARE\Microsoft\DVDNavigator\DriveSpindown 
[Sec]
```



where


```
Sec
```



is the spin down time in seconds.

## Related topics

<dl> <dt>

[Appendixes](appendixes.md)
</dt> </dl>

 

 



