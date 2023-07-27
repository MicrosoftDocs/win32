---
description: The CAMSchedule class implements a scheduler for reference clocks.
ms.assetid: 67aacffb-b781-4323-8973-355a76821401
title: CAMSchedule class (Dsschedule.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CAMSchedule
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CAMSchedule class

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `CAMSchedule` class implements a scheduler for reference clocks.



| Public Methods                                             | Description                                                                          |
|------------------------------------------------------------|--------------------------------------------------------------------------------------|
| [**CAMSchedule**](camschedule-camschedule.md)             | Constructor method.                                                                  |
| [**~CAMSchedule**](camschedule--camschedule.md)           | Destructor method. Virtual.                                                          |
| [**GetAdviseCount**](camschedule-getadvisecount.md)       | Retrieves the number of pending advise requests.                                     |
| [**GetNextAdviseTime**](camschedule-getnextadvisetime.md) | Retrieves the time of the next advise request.                                       |
| [**AddAdvisePacket**](camschedule-addadvisepacket.md)     | Adds an advise request to the list of pending requests.                              |
| [**Unadvise**](camschedule-unadvise.md)                   | Removes an advise request.                                                           |
| [**Advise**](camschedule-advise.md)                       | Dispatches all requests that are scheduled for a specified time or earlier.          |
| [**GetEvent**](camschedule-getevent.md)                   | Retrieves an event handle, which is used to signal a change in the next advise time. |



 

## Remarks

This helper object maintains a list of advise requests for a reference clock. The [**CBaseReferenceClock**](cbasereferenceclock.md) class uses it to help schedule advise requests. Clocks use this object in the following manner:

1.  The clock creates a worker thread to handle scheduling.
2.  The worker thread calls the [**CAMSchedule::GetEvent**](camschedule-getevent.md) method to retrieve an event handle from the scheduler. It waits on this event, initially with an infinite time-out.
3.  To schedule a new advise request, the clock calls the [**CAMSchedule::AddAdvisePacket**](camschedule-addadvisepacket.md) method. An advise request can be one-shot or periodic. The scheduler keeps the list of requests in time order.
4.  If a request is added to the front of the list, the scheduler signals the event. (The list is empty at first, so the first request is guaranteed to signal the event.)
5.  When the event is signaled, the worker thread calls the [**CAMSchedule::Advise**](camschedule-advise.md) method, specifying the current reference time. If any pending requests have expired, the scheduler dispatches them.
6.  The Advise method returns the time of the next request. The worker thread uses this value to calculate a new time-out value.
7.  Steps 2 6 repeat indefinitely.
8.  To terminate the worker thread, the clock sets an internal flag and signals the event.

In step 2, either the event is signaled, or the wait times out. If the event is signaled, it means that a new request was added to the front of the list. The worker thread must calculate a new time-out value. On the other hand, if the wait times out, it means that an advise request has come due and must be dispatched. The call to Advise in step 5 handles both cases.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Dsschedule.h (include Streams.h)</dt> </dl>                                                                                |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



 

 




