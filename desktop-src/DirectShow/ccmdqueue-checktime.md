---
description: The CheckTime method determines if a specified time is due.
ms.assetid: 522bc7ae-f998-4a7d-8bc3-caf09b4108a6
title: CCmdQueue.CheckTime method (Winutil.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CCmdQueue.CheckTime
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CCmdQueue.CheckTime method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `CheckTime` method determines if a specified time is due.

## Syntax


```C++
BOOL CheckTime(
   CRefTime time,
   BOOL     bStream
);
```



## Parameters

<dl> <dt>

*time* 
</dt> <dd>

Time to check.

</dd> <dt>

*bStream* 
</dt> <dd>

**TRUE** if the *time* parameter is a stream-time value; **FALSE** if *time* is a presentation-time value.

</dd> </dl>

## Return value

Returns **TRUE** if the specified time has not yet passed.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Winutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CCmdQueue Class**](ccmdqueue.md)
</dt> </dl>

 

 




