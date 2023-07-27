---
description: Returns TRUE if the current thread is the owner of the specified critical section.
ms.assetid: 96158f08-07a0-42a9-b173-0a05456a5f3a
title: CritCheckIn function (Wxutil.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CritCheckIn
api_type: 
- LibDef
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CritCheckIn function

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Returns **TRUE** if the current thread is the owner of the specified critical section.

## Syntax


```C++
BOOL WINAPI CritCheckIn(
   CCritSec *pcCrit
);
```



## Parameters

<dl> <dt>

*pcCrit* 
</dt> <dd>

Pointer to a [**CCritSec**](ccritsec.md) critical section.

</dd> </dl>

## Return value

In debug builds, returns **TRUE** if the current thread is the owner of this critical section, or **FALSE** otherwise. In retail builds, always returns **TRUE**.

## Remarks

This function is especially useful within the [**ASSERT**](assert.md) macro, to test whether a thread owns a given lock.

## Examples

The following code example shows how to use this function:


```
{
    CCritSec MyLock;  // Critical section is not locked yet.
    
    ASSERT(CritCheckIn(&MyLock)); // This assert will fire.

    // Lock the critical section.    
    CAutoLock cObjectLock(&MyLock);
     
    ASSERT(CritCheckIn(&MyLock)); // This assert will not fire.

} // Lock goes out of scope here.
```



## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Wxutil.h (include Streams.h)</dt> </dl>                                                                                    |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[Critical Section Debugging Functions](critical-section-debugging-functions.md)
</dt> </dl>

 

 




