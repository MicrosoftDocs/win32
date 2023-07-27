---
description: Critical Section Debugging Functions
ms.assetid: 2e58ff06-d9b2-45fe-bd40-d637aa434339
title: Critical Section Debugging Functions
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Critical Section Debugging Functions

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

These functions help to debug critical sections in your code, which can make it easier to find the cause of a deadlock. These functions use the [**CCritSec**](ccritsec.md) helper class.



| Function                             | Description                                                                  |
|--------------------------------------|------------------------------------------------------------------------------|
| [**CritCheckIn**](critcheckin.md)   | Returns **TRUE** if the current thread owns the specified critical section.  |
| [**CritCheckOut**](critcheckout.md) | Returns **FALSE** if the current thread owns the specified critical section. |
| [**DbgLockTrace**](dbglocktrace.md) | Enables or disables debug logging for a given critical section.              |



 

## Related topics

<dl> <dt>

[Debugging Utilities](debugging-utilities.md)
</dt> </dl>

 

 



