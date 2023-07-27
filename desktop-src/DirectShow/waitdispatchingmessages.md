---
description: The WaitDispatchingMessages function waits for an object to be signaled, while dispatching window messages.
ms.assetid: d15f6736-d141-47a3-b767-fbf774982fb4
title: WaitDispatchingMessages function (Wxutil.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- WaitDispatchingMessages
api_type: 
- LibDef
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# WaitDispatchingMessages function

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `WaitDispatchingMessages` function waits for an object to be signaled, while dispatching window messages.

## Syntax


```C++
DWORD WINAPI WaitDispatchingMessages(
   HANDLE hObject,
   DWORD  dwWait,
   HWND   hwnd = NULL,
   UINT   uMsg = 0,
   HANDLE hEvent = NULL
);
```



## Parameters

<dl> <dt>

*hObject* 
</dt> <dd>

Handle of the object to wait for.

</dd> <dt>

*dwWait* 
</dt> <dd>

Time-out interval, in milliseconds.

</dd> <dt>

*hwnd* 
</dt> <dd>

Optional handle to a window.

</dd> <dt>

*uMsg* 
</dt> <dd>

Optional window message, specifying a message to dispatch.

</dd> <dt>

*hEvent* 
</dt> <dd>

Optional handle to an event to wait for.

</dd> </dl>

## Return value

Returns the value from the **WaitForMultipleObjects** function.

## Remarks

If an object owns a window, it should dispatch window messages while waiting. This function enables the object to wait for an event, semaphore, or other mutual exclusion object while dispatching messages.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Wxutil.h (include Streams.h)</dt> </dl>                                                                                    |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[Miscellaneous Helper Functions](miscellaneous-helper-functions.md)
</dt> </dl>

 

 




