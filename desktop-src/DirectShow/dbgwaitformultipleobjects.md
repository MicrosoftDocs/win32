---
description: Waits for any (or all) of the specified objects to be signaled.
ms.assetid: e60c98b6-a4d2-40de-8297-727404e3c387
title: DbgWaitForMultipleObjects function (Wxdebug.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- DbgWaitForMultipleObjects
api_type: 
- LibDef
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# DbgWaitForMultipleObjects function

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Waits for any (or all) of the specified objects to be signaled.

In a debug build, this function triggers an assert if the time-out interval expires before the objects are signaled. To set the time-out interval, call the [**DbgSetWaitTimeout**](dbgsetwaittimeout.md) function.

In a retail build, this function is equivalent to the **WaitForMultipleObjects** function with a time-out interval of INFINITE.

## Syntax


```C++
DWORD DbgWaitForMultipleObjects(
   DWORD         nCount,
   CONST HANDLE  *lpHandles,
   BOOL          bWaitAll
);
```



## Parameters

<dl> <dt>

*nCount* 
</dt> <dd>

Number of objects.

</dd> <dt>

*lpHandles* 
</dt> <dd>

Array of handles to objects, of size *nCount*.

</dd> <dt>

*bWaitAll* 
</dt> <dd>

Boolean value that specifies whether to wait for all of the objects. If **TRUE**, the function waits for all of the objects to be signaled. Otherwise, it waits for at least one object to be signaled.

</dd> </dl>

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Wxdebug.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[Wait Debugging Functions](wait-debugging-functions.md)
</dt> </dl>

 

 




