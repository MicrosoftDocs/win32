---
description: The AddAdvisePacket method adds an advise request to the list of pending requests.
ms.assetid: 138d8404-7d28-47cc-91b4-4733a113ac7a
title: CAMSchedule.AddAdvisePacket method (Dsschedule.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CAMSchedule.AddAdvisePacket
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CAMSchedule.AddAdvisePacket method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `AddAdvisePacket` method adds an advise request to the list of pending requests.

## Syntax


```C++
DWORD_PTR AddAdvisePacket(
  [ref] const REFERENCE_TIME &time1,
  [ref] const REFERENCE_TIME &time2,
              HANDLE         hNotify,
              BOOL           bPeriodic
);
```



## Parameters

<dl> <dt>

*time1* \[ref\]
</dt> <dd>

Requested time for the advise.

</dd> <dt>

*time2* \[ref\]
</dt> <dd>

For periodic advise requests, the time between notifications. This parameter is ignored if *bPeriodic* is **FALSE**.

</dd> <dt>

*hNotify* 
</dt> <dd>

Handle to a semaphore if *bPeriodic* is **TRUE**, or handle to an event if *bPeriodic* is **FALSE**.

</dd> <dt>

*bPeriodic* 
</dt> <dd>

Boolean value that specifies whether to add a periodic notification or a one-shot notification. If **TRUE**, the notification is periodic; the *time2* parameter specifies the time between notifications. If **FALSE**, the notification occurs only once.

</dd> </dl>

## Return value

Returns an identifier for the advise request (the "cookie"). If the method fails, the return value is zero.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Dsschedule.h (include Streams.h)</dt> </dl>                                                                                |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CAMSchedule Class**](camschedule.md)
</dt> </dl>

 

 




