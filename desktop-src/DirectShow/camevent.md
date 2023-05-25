---
description: The CAMEvent class is a wrapper for manual-reset and auto-reset events.
ms.assetid: 228b4e51-afc5-4cb6-b225-309013713983
title: CAMEvent class (Wxutil.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CAMEvent
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CAMEvent class

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

![camevent class hierarchy](images/util06.png)

The **CAMEvent** class is a wrapper for manual-reset and auto-reset events.

This class provides a convenient way to manage events, rather than calling functions such as [**CreateEvent**](/windows/desktop/api/synchapi/nf-synchapi-createeventa), [**WaitForSingleObject**](/windows/desktop/api/synchapi/nf-synchapi-waitforsingleobject), and [**ResetEvent**](/windows/desktop/api/synchapi/nf-synchapi-resetevent).



| Protected Member Variables                          | Description                                                     |
|-----------------------------------------------------|-----------------------------------------------------------------|
| [**m\_hEvent**](camevent-m-hevent.md)              | Event handle.                                                   |
| Public Methods                                      | Description                                                     |
| [**CAMEvent**](camevent-camevent.md)               | Constructor method.                                             |
| [**~CAMEvent**](camevent--camevent.md)             | Destructor method.                                              |
| [**Check**](camevent-check.md)                     | Checks whether the event is set, without blocking.              |
| [**Reset**](camevent-reset.md)                     | Sets the state of the event to nonsignaled.                     |
| [**Set**](camevent-set.md)                         | Signals the event.                                              |
| [**Wait**](camevent-wait.md)                       | Blocks until the event is signaled, or until a time-out occurs. |
| Operators                                           | Description                                                     |
| [**operator HANDLE**](camevent-operator-handle.md) | Retrieves the event handle.                                     |



 

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Wxutil.h (include Streams.h)</dt> </dl>                                                                                    |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



 

